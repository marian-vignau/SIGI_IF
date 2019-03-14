import wx
from sqlalchemy.exc import IntegrityError

from wxSQAlch import ListViewObject
from vistas import EdicionCausa
import models
import PanelCausa, EdicionEscrito, EdicionObjeto
from wxSQAlch.Tools import replace_widget


class ctrlEdicionCausa (EdicionCausa):
    def __init__(self,  parent, idCausa=None):
        super().__init__(parent)
        self.paCausaNvo = PanelCausa.ctrlPanelCausa(self)
        replace_widget(self, self.paCausa, self.paCausaNvo)
        self.Layout()
        self.idCausa = idCausa
        self.list = ListViewObject.ListViewObject(
            self.lsEscritos,
            [ListViewObject.Column("Escrito", "idEscrito"),
             ListViewObject.Column("Descripción", "descripcion"),
             ListViewObject.Column("Ubicación", "ubicacionFisica")],
            itemkey="idEscrito"
        )
        self.styles = self.list.styles
        self.error = False

        if idCausa is None:
            self.enable_edicion_lista(False)
            self.model = models.TableCausa()
            self.CreateTreeRoot()
        else:
            s1 = models.sessions()
            self.model = s1.query(models.TableCausa) \
                .filter(models.TableCausa.idCausa == idCausa).first()
            self.paCausaNvo.from_model(self.model)
            s1.expunge(self.model)
            s1 = models.sessions()
            for row in s1.query(models.TableEscrito). \
                    filter(models.TableEscrito.idCausa==idCausa):
                self.list.change_item_list(row)
            self.LoadTree()

    def enable_edicion_lista(self, enabled):
        self.btAddEscrito.Enable(enabled)
        self.btDeleteEscrito.Enable(enabled)
        self.btAddObjeto.Enable(enabled)
        self.btDeleteObjeto.Enable(enabled)

    def btReestablecerOnButtonClick(self, event):
        self.paCausaNvo.from_model(self.model)
        event.Skip()

    def btGuardarOnButtonClick(self, event):
        s1 = models.sessions()

        self.paCausaNvo.to_model(self.model)
        try:
            s1.add(self.model)
            s1.commit()
            self.enable_edicion_lista(True)

        except IntegrityError as e:
            self.error = "La causa no puede ser grabada\n" + str(e)

        if self.error:
            wx.MessageDialog(
                self, "La causa no puede ser grabada\n" + \
                      str(e)
            ).ShowModal()

            s1.rollback()

    def btAddEscritoOnButtonClick(self, event):
        dlg = EdicionEscrito.ctrlEdicionEscrito(self, self.model.idCausa)
        dlg.ShowModal()
        if dlg.resultado:
            self.list.change_item_list(dlg.model, add=True)


    def btDeleteEscritoOnButtonClick(self, event):
        idEscrito = self.list.get_key()
        dlg = EdicionEscrito.ctrlEdicionEscrito(self, self.idCausa, idEscrito, delete=True)
        dlg.ShowModal()
        if dlg.resultado:
            self.list.delete_item()

    def lsEscritosOnLeftDClick(self, event):
        idEscrito = self.list.get_key()
        dlg = EdicionEscrito.ctrlEdicionEscrito(self, self.idCausa, idEscrito)
        dlg.ShowModal()
        if dlg.resultado:
            self.list.change_item_list(dlg.model)

    def CreateTreeRoot(self):
        """On empty tree, create root"""
        self.root = self.trcObjetos.AddRoot("Objetos a peritar")

    def LoadTree(self):
        """Load all objetos in the tree."""
        def allocate_item(parent, row):
            """Add an item in the tree and return the item"""
            child = self.trcObjetos.AppendItem(parent, row.descripcion)
            self.trcObjetos.SetItemData(child, row.idObjeto)
            return child

        q1 = models.objects_rel_causa(self.model.idCausa)
        self.trcObjetos.DeleteAllItems()
        self.CreateTreeRoot()
        allocated = {}  # all allocated items
        unallocated = {}  # all items related to Causa but no allocated
        for row in q1:
            if row.objetoRelacionado is None:
                # allocate objetos related only to cause
                allocated[row.idObjeto] = allocate_item(self.root, row)
            elif row.objetoRelacionado in allocated:
                # allocate objetos with known parent
                parent = allocated[row.objetoRelacionado]
                allocated[row.idObjeto] = allocate_item(parent, row)
            else:
                # left unallocated to next iteration
                unallocated[row.idObjeto] = row

        # iterate trying to allocate all unallocated objetos
        add_allocated = len(unallocated)
        while add_allocated > 0:
            add_allocated = 0  # it remains in 0 if nothing is changed
            for item, row in unallocated.items():
                # when allocate an item, put None in unallocated dict's item
                if not row is None:
                    parent = None
                    if row.objetoRelacionado in allocated:
                        # parent is allocated in tree
                        parent = allocated[row.objetoRelacionado]
                    elif not row.objetoRelacionado in unallocated:
                        # parent is missing, so put it anyway, linked to root
                        parent = self.root
                    if parent:
                        allocated[row.idObjeto] = allocate_item(parent, row)
                        unallocated[row.idObjeto] = None
                        add_allocated += 1  # if something has changed, iterate one more time

        # if some objeto has a broken parent link, add it anyway
        for item, row in unallocated.items():
            if not row is None and not row.objetoRelacionado in allocated:
                allocated[row.idObjeto] = allocate_item(self.root, row)
                unallocated[row.idObjeto] = None
        self.trcObjetos.ExpandAll()

    def btAddObjetoOnButtonClick(self, event):
        parent_item = self.trcObjetos.GetSelection()
        if parent_item:
            idObjetoRelacionado = self.trcObjetos.GetItemData(parent_item)
        else:
            parent_item = self.root
            idObjetoRelacionado = None
        descObjetoRelacionado = self.trcObjetos.GetItemText(parent_item)
        dlg = EdicionObjeto.ctrlEdicionObjeto(self,
                                              idCausa=self.model.idCausa,
                                              ObjetoRelacionado=descObjetoRelacionado,
                                              idObjetoRelacionado=idObjetoRelacionado)
        dlg.ShowModal()
        if not dlg.error:
            child = self.trcObjetos.AppendItem(parent_item, dlg.model.descripcion)
            self.trcObjetos.SetItemData(child, dlg.model.idObjeto)


    def btDeleteObjetoOnButtonClick(self, event):
        item = self.trcObjetos.GetSelection()
        if self.trcObjetos.GetChildrenCount(item):
            wx.MessageDialog(
                self, "Debe borrar los objetos relacionados antes").ShowModal()
        else:
            idObjeto = self.trcObjetos.GetItemData(item)
            dlg = EdicionObjeto.ctrlEdicionObjeto(self,
                                                  idCausa=self.model.idCausa,
                                                  idObjeto=idObjeto,
                                                  delete=True)
            dlg.ShowModal()
            if not dlg.error:
                self.trcObjetos.Delete(item)

    def trcObjetosOnLeftDClick(self, event):
        pt = event.GetPosition()
        item, flags = self.trcObjetos.HitTest(pt)
        if item:
            idObjeto = self.trcObjetos.GetItemData(item)
            if not idObjeto is None:
                dlg = EdicionObjeto.ctrlEdicionObjeto(self,
                                                      idCausa=self.model.idCausa,
                                                      idObjeto=idObjeto)
                dlg.ShowModal()
                try:
                    if not dlg.error:
                        self.trcObjetos.SetItemText(item, dlg.model.descripcion)
                except Exception as e:
                    print(e)
                    print(dlg.model)




    def apply_style_on_tree(self, item, style):
        """Use style attr to update a tree item"""
        use = self.styles["normal"].copy()
        use.update(self.styles[style])
        if use["font-weight"] == "normal":
            self.trcObjetos.SetItemBold(item, False)
        if use["font-weight"] == "bold":
            self.trcObjetos.SetItemBold(item, True)
        self.trcObjetos.SetItemTextColour(item, use["font-color"])
        self.trcObjetos.SetItemBackgroundColour(item, use["background"])

    def walk_through(self, mainbranch):
        """ Walks through all items in one branch recursively"""
        yield mainbranch
        child, cookie = self.trcObjetos.GetFirstChild(mainbranch)
        while child.IsOk():
            for subbranch in self.walk_through(child):
                yield subbranch
            child = self.trcObjetos.GetNextSibling(child)

    def lsEscritosOnListItemSelected(self, event):
        idEscrito = self.list.get_key()
        self.list.apply_style_all(reset=True)
        self.list.apply_style(None, "blue")
        objetos = models.objects_rel_escrito(self.idCausa, idEscrito)
        if self.trcObjetos.ItemHasChildren(self.root):
            child, cookie = self.trcObjetos.GetFirstChild(self.root)
            while child.IsOk():
                idObjeto = self.trcObjetos.GetItemData(child)
                style = "enhanced" if idObjeto in objetos else "faded"
                for item in self.walk_through(child):
                    self.apply_style_on_tree(item, style)

                child = self.trcObjetos.GetNextSibling(child)
        event.Skip()

    def trcObjetosOnLeftDown(self, event):
        pt = event.GetPosition()
        self.trcObjetos.ExpandAll()
        item, flags = self.trcObjetos.HitTest(pt)
        if not item:
            return
        idObjeto = self.trcObjetos.GetItemData(item)
        for child in self.walk_through(self.root):
            self.apply_style_on_tree(child, "normal")
        self.apply_style_on_tree(item, "blue")
        escritos = models.escritos_rel_objeto(self.idCausa, idObjeto)
        for idx in range(self.lsEscritos.GetItemCount()):
            idEscrito = self.list.get_key(idx)
            if idEscrito in escritos:
                self.list.apply_style(idx, "enhanced")
            else:
                self.list.apply_style(idx, "faded")

    def btVincularOnButtonClick(self, event):
        item = self.trcObjetos.GetFocusedItem()
        idEscrito = self.list.get_key()
        if item.IsOk() and idEscrito:
            idObjeto = self.trcObjetos.GetItemData(item)
            objeto = self.trcObjetos.GetItemText(item)
            escrito = self.list.get_text()
            result = wx.MessageBox("Desea vincular al objeto %s con el escrito %s" % (objeto, escrito),
                                   "Confirma que desea vincular", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
            if result == wx.OK:
                models.relac_escrito_objeto(self.idCausa, idEscrito, idObjeto)

