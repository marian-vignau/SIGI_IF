"""
To show fields of causas

"""
__author__ = "María Andrea Vignau"

import wx
from sqlalchemy.exc import IntegrityError

from wxSQAlch import Mapper
import models

from vistas import PanelCausa
import OficinasJudiciales


class ctrlPanelCausa(PanelCausa):
    def __init__(self, parent):
        super().__init__(parent)
        self.mapper = Mapper.Mapper(
            Mapper.MapObj(self.tcExpteJud, "expteJud"),
            Mapper.MapObj(self.tcExptePol, "exptePol"),
            Mapper.MapList(self.chEstado, "idEstado", self.loadEstados()),
            Mapper.MapObj(self.tcExpteOtro, "expteOtro"),
            Mapper.MapObj(self.tcObservaciones, "observaciones"),
            Mapper.MapObj(self.tcCaratula, "caratula"),
            Mapper.MapList(
                self.chDestinatario, "idDestinatario", self.loadDestinatarios()
            ),
        )

    def loadEstados(self):
        s1 = models.sessions()
        valores = [
            (row.descripcion, row.id) for row in s1.query(models.TableEstadoCausa)
        ]
        return valores

    def loadDestinatarios(self):
        s1 = models.sessions()
        valores = [(row.id, row.id) for row in s1.query(models.TableDestinatario)]
        return valores

    def to_model(self, model):
        self.mapper.to_model(model)
        return model

    def from_model(self, model):
        self.mapper.from_model(model)
        return model

    def clear(self):
        self.mapper.clear()

    # Virtual event handlers, overide them in your derived class
    def lblEstadoOnLeftDClick(self, event):
        dlg = wx.TextEntryDialog(
            self, "Ingrese la descripción del nuevo estado", "Editar Estado", ""
        )

        dlg.SetValue("")

        if dlg.ShowModal() == wx.ID_OK:
            s1 = models.sessions()
            modelEstado = models.TableEstadoCausa()
            try:
                modelEstado.descripcion = dlg.GetValue()
                s1.add(modelEstado)
                s1.commit()
                self.mapper.idEstado.reload(self.loadEstados())
                self.mapper.idEstado.SetValue(modelEstado.id)

            except IntegrityError:
                wx.MessageDialog(self, "El estado ya se encuentra agregado").ShowModal()

                s1.rollback()

        dlg.Destroy()

    def lblDestinatarioOnLeftDClick(self, event):
        dlg = OficinasJudiciales.ctrlOficinasJudiciales(self)
        dlg.ShowModal()
        self.mapper.idDestinatario.reload(self.loadDestinatarios())
        if dlg.selected:
            self.mapper.idDestinatario.SetValue(dlg.selected)
        dlg.Destroy()
