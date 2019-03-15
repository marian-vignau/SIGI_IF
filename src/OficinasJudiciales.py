"""
To edit Oficinas Judiciales, add, modify and delete

"""
__author__ = "María Andrea Vignau"


import wx
from sqlalchemy.exc import IntegrityError

from wxSQAlch import Mapper, ListViewObject
from vistas import OficinasJudiciales
import models


class ctrlOficinasJudiciales(OficinasJudiciales):
    def __init__(self, parent):
        super().__init__(parent)
        self.mapper = Mapper.Mapper(
            Mapper.MapObj(self.tcId, "id"),
            Mapper.MapObj(self.tcNombre, "nombre"),
            Mapper.MapObj(self.tcCircunscripcion, "circunscripcion"),
            Mapper.MapObj(self.tcACargo, "aCargo"),
            Mapper.MapList(self.chIdTipo, "idTipo", self.loadTipoDestinatarios()),
            Mapper.MapObj(self.tcCorreoElectronico, "correoElectronico"),
            Mapper.MapObj(self.tcTelefono, "telefono"),
        )
        self.init_lista_destinatarios()
        self.model = None
        self.selected = None

    def clear(self):
        self.mapper.clear()

    def to_model(self, model):
        self.mapper.to_model(model)
        return model

    def from_model(self, model):
        self.mapper.from_model(model)
        return model

    def init_lista_destinatarios(self):
        # for normal, simple columns, you can add them like this:
        self.item = None
        self.lsOficinas.ClearAll()
        self.list = ListViewObject.ListViewObject(
            self.lsOficinas,
            [
                ListViewObject.Column("Circunscripcion", "circunscripcion"),
                ListViewObject.Column("Nombre", "nombre"),
                ListViewObject.Column("A cargo", "aCargo"),
                ListViewObject.Column("Id", "id"),
            ],
            itemkey="id",
        )
        s1 = models.sessions()
        for row in s1.query(models.TableDestinatario).all():
            self.list.change_item_list(row)

    def loadTipoDestinatarios(self):
        s1 = models.sessions()
        valores = [
            (row.descripcion, row.id) for row in s1.query(models.TableTipoDestinatario)
        ]
        return valores

    def AddTipoOficinaOnLeftDClick(self, event):
        dlg = wx.TextEntryDialog(
            self,
            "Ingrese la descripción del nuevo tipo de destinatario",
            "Editar Tipo Destinatario",
            "",
        )

        dlg.SetValue("")

        if dlg.ShowModal() == wx.ID_OK:
            # self.log.WriteText('You entered: %s\n' % dlg.GetValue())
            s1 = models.sessions()
            model = models.TableTipoDestinatario()
            try:
                model.descripcion = dlg.GetValue()
                s1.add(model)
                s1.commit()
                self.mapper.idTipo.reload(self.loadTipoDestinatarios())
                self.mapper.idTipo.SetValue(model.id)

            except IntegrityError:
                wx.MessageDialog(
                    self, "El tipo de oficina ya se encuentra agregado"
                ).ShowModal()

                s1.rollback()

        dlg.Destroy()

    def lsOficinasOnListItemSelected(self, event):
        idOficina = self.list.get_key(event.Index)
        s1 = models.sessions()
        self.model = (
            s1.query(models.TableDestinatario)
            .filter(models.TableDestinatario.id == idOficina)
            .first()
        )
        self.from_model(self.model)
        self.selected = self.model.id
        s1.expunge(self.model)

    def btReestablecerOnButtonClick(self, event):
        self.model = None
        self.clear()
        self.init_lista_destinatarios()

    def btSalirOnButtonClick(self, event):
        self.Close()

    def OficinasJudicialesOnClose(self, event):
        event.Skip()

    def btAddOnButtonClick(self, event):
        s1 = models.sessions()
        if not self.model:
            self.model = models.TableDestinatario()
            self.list.clear_item()

        self.to_model(self.model)
        try:
            s1.add(self.model)
            s1.commit()
            idx = self.list.change_item_list(self.model)
            self.selected = self.model.id
            self.list.show_selection()
            self.model = None
            self.clear()

        except IntegrityError as e:
            wx.MessageDialog(
                self, "La oficina no puede ser agregada agregado\n" + str(e)
            ).ShowModal()

            s1.rollback()

    def btDeleteOnButtonClick(self, event):
        if not self.model:
            wx.MessageDialog(self, "No hay oficina seleccionada").ShowModal()
        else:
            s1 = models.sessions()
            try:
                s1.add(self.model)
                s1.delete(self.model)
                s1.commit()
                wx.MessageDialog(self, "Oficina eliminada").ShowModal()
                self.list.delete_item()
                self.model = None
                self.clear()
                self.selected = None

            except IntegrityError as e:
                wx.MessageDialog(
                    self, "La oficina no puede ser borrada\n" + str(e)
                ).ShowModal()

                s1.rollback()
