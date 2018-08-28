import wx
from sqlalchemy.exc import IntegrityError

from wxSQAlch import ListViewObject
from vistas import EdicionCausa
import models
import PanelCausa, EdicionEscrito

class ctrlEdicionCausa (EdicionCausa):
    def __init__(self,  parent, idCausa=None):
        super().__init__(parent)
        itemsizer = self.GetSizer().GetItem(self.paCausa, recursive=True)
        self.paCausaNvo = PanelCausa.ctrlPanelCausa(self)
        itemsizer.AssignWindow(self.paCausaNvo)
        self.paCausa.Destroy()
        self.Layout()
        self.idCausa = idCausa
        self.list = ListViewObject.ListViewObject(
            self.lsEscritos,
            [ListViewObject.Column("Escrito", "idEscrito"),
            ListViewObject.Column("Descripción", "descripcion"),
            ListViewObject.Column("Ubicación", "ubicacionFisica")],
            itemkey="idEscrito"
        )

        if idCausa is None:
            self.enable_edicion_lista(False)
            self.model = models.TableCausa()
        else:
            s1 = models.sessions()
            self.model = s1.query(models.TableCausa)\
                .filter(models.TableCausa.idCausa == idCausa).first()
            self.paCausaNvo.from_model(self.model)
            s1.expunge(self.model)
            s1 = models.sessions()
            for row in s1.query(models.TableEscrito).\
                    filter(models.TableEscrito.idCausa==idCausa):
                self.list.change_item_list(row)

    def enable_edicion_lista(self, enabled):
        self.btAdd.Enable(enabled)
        self.btDelete.Enable(enabled)

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
            wx.MessageDialog(
                self, "La causa no puede ser grabada\n" +\
                      str(e)
            ).ShowModal()

            s1.rollback()

    def btAddOnButtonClick(self, event):
        dlg = EdicionEscrito.ctrlEdicionEscrito(self, self.model.idCausa)
        dlg.ShowModal()
        self.list.change_item_list(dlg.model)


    def btDeleteOnButtonClick(self, event):
        idEscrito = self.list.get_key()
        dlg = EdicionEscrito.ctrlEdicionEscrito(self, self.idCausa, idEscrito, delete=True)
        dlg.ShowModal()
        self.list.change_item_list(dlg.model)

    def lsEscritosOnLeftDClick(self, event):
        idEscrito = self.list.get_key()
        dlg = EdicionEscrito.ctrlEdicionEscrito(self, self.idCausa, idEscrito)
        dlg.ShowModal()
        self.list.change_item_list(dlg.model)


