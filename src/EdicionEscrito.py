"""
To edit escritos

"""
__author__ = "María Andrea Vignau"


import wx
from sqlalchemy.exc import IntegrityError

from vistas import EdicionEscrito
from wxSQAlch import Tools
import models
import PanelEscrito, EdicionObjeto
from wxSQAlch.Tools import replace_widget


BORRAR_LABEL = "Borrar"


class ctrlEdicionEscrito(EdicionEscrito):
    def __init__(self, parent, idCausa, idEscrito=None, delete=False):
        super().__init__(parent)
        self.paEscritoNvo = PanelEscrito.ctrlPanelEscrito(self, idCausa)
        replace_widget(self, self.paEscrito, self.paEscritoNvo)
        self.Layout()
        self.resultado = False
        if idEscrito is None:
            # self.enable_edicion_escritos(False)
            self.model = models.TableEscrito()
        else:
            s1 = models.sessions()
            self.model = (
                s1.query(models.TableEscrito)
                .filter(models.TableEscrito.idCausa == idCausa)
                .filter(models.TableEscrito.idEscrito == idEscrito)
                .first()
            )
            self.paEscritoNvo.from_model(self.model)
            s1.expunge(self.model)
        if delete:
            self.paEscritoNvo.mapper.enable(False)
            self.btGuardar.SetLabel(BORRAR_LABEL)
        Tools.changeFont(self, 2)
        Tools.changeFont(self.paEscritoNvo, 2)

    def btReestablecerOnButtonClick(self, event):
        self.paEscritoNvo.from_model(self.model)

    def btGuardarOnButtonClick(self, event):
        s1 = models.sessions()
        self.paEscritoNvo.to_model(self.model)
        self.error = False
        if self.btGuardar.GetLabel() == BORRAR_LABEL:
            try:
                s1.add(self.model)
                s1.delete(self.model)
                s1.commit()
                self.resultado = True
                # self.enable_edicion_escritos(True)
            except IntegrityError as e:
                self.error = "El escrito no puede ser borrado\n" + str(e)

        else:
            try:
                s1.add(self.model)
                s1.commit()
                self.resultado = True

            except IntegrityError as e:
                self.error = "El escrito no puede ser grabado\n" + str(e)

        if self.error:
            wx.MessageDialog(self, self.error).ShowModal()
            s1.rollback()
        else:
            self.Close()
