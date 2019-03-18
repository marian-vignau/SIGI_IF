"""
To edit Objetos

"""
__author__ = "María Andrea Vignau"


import wx
from sqlalchemy.exc import IntegrityError

from vistas import EdicionObjeto
import models
import PanelObjeto

from wxSQAlch.Tools import replace_widget


BORRAR_LABEL = "Borrar"
class ctrlEdicionObjeto(EdicionObjeto):
    def __init__(
            self,
            parent,
            idCausa=None,
            idEscrito=None,
            ObjetoRelacionado="",
            idObjetoRelacionado=None,
            idObjeto=None,
            delete=False,
    ):
        super().__init__(parent)
        self.error = False
        self.paObjetoNvo = PanelObjeto.ctrlPanelObjeto(self, ObjetoRelacionado)
        replace_widget(self, self.paObjeto, self.paObjetoNvo)
        self.Layout()
        self.idCausa = idCausa
        self.idObjeto = idObjeto
        self.idEscrito = idEscrito
        self.idObjetoRelacionado = idObjetoRelacionado
        if idObjeto is None:
            # self.enable_edicion_Objetos(False)
            self.model = models.TableObjeto()
        else:
            s1 = models.sessions()
            self.model = (
                s1.query(models.TableObjeto)
                    .filter(models.TableObjeto.idObjeto == idObjeto)
                    .first()
            )
            self.paObjetoNvo.from_model(self.model)
            s1.expunge(self.model)
        if delete:
            self.paObjetoNvo.mapper.enable(False)
            self.btGuardar.SetLabel(BORRAR_LABEL)

    def btReestablecerOnButtonClick(self, event):
        self.paObjetoNvo.from_model(self.model)

    def btGuardarOnButtonClick(self, event):
        s1 = models.sessions()
        self.paObjetoNvo.to_model(self.model)
        self.error = False
        if self.btGuardar.GetLabel() == BORRAR_LABEL:
            try:
                s1.add(self.model)
                s1.delete(self.model)
                s1.commit()
            except IntegrityError as error:
                self.error = "El Objeto no puede ser borrado\n" + str(error)

        else:
            try:
                if not self.idObjeto:
                    newid = models.next_objeto_id()
                    self.model.idObjeto = newid
                relacion = models.TableRelEscObj(
                    idCausa=self.idCausa,
                    idEscrito=self.idEscrito,
                    TableObjeto=self.model)
                s1.add(self.model)
                s1.add(relacion)

                s1.commit()
                wx.MessageDialog(
                    self, "El Objeto fue agregado"   #  + repr(self.model)
                ).ShowModal()
                self.idObjeto = self.model.idObjeto
                self.Descripcion = self.model.descripcion
                s1.expunge(self.model)

            except IntegrityError as error:
                self.error = "El Objeto no puede ser grabado\n" + str(error)
        if self.error:
            wx.MessageDialog(self, self.error).ShowModal()
            s1.rollback()
        self.Close()
