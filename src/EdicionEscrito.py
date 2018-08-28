import wx
from sqlalchemy.exc import IntegrityError

from vistas import EdicionEscrito
import models
import PanelEscrito

BORRAR_LABEL = "Borrar"

class ctrlEdicionEscrito (EdicionEscrito):
    def __init__(self,  parent, idCausa, idEscrito=None, delete=False):
        super().__init__(parent)
        itemsizer = self.GetSizer().GetItem(self.paEscrito, recursive=True)
        self.paEscritoNvo = PanelEscrito.ctrlPanelEscrito(self, idCausa)
        itemsizer.AssignWindow(self.paEscritoNvo)
        self.paEscrito.Destroy()
        self.Layout()
        if idEscrito is None:
            #self.enable_edicion_escritos(False)
            self.model = models.TableEscrito()
            self.enable_edicion_lista(False)
        else:
            s1 = models.sessions()
            self.model = s1.query(models.TableEscrito)\
                .filter(models.TableEscrito.idCausa == idCausa)\
                .filter(models.TableEscrito.idEscrito == idEscrito).first()
            self.paEscritoNvo.from_model(self.model)
            s1.expunge(self.model)
        if delete:
            self.paEscritoNvo.mapper.enable(False)
            self.btGuardar.SetLabel(BORRAR_LABEL )
            self.enable_edicion_lista(False)

    def enable_edicion_lista(self, enabled):
        self.btAdd.Enable(enabled)
        self.btDelete.Enable(enabled)

    def btReestablecerOnButtonClick(self, event):
        self.paEscritoNvo.from_model(self.model)

    def btGuardarOnButtonClick(self, event):
        s1 = models.sessions()
        self.paEscritoNvo.to_model(self.model)
        if self.btGuardar.GetLabel() == BORRAR_LABEL:
            try:
                s1.add(self.model)
                s1.delete(self.model)
                s1.commit()
                s1.expunge(self.model)
                # self.enable_edicion_escritos(True)
            except IntegrityError as e:
                wx.MessageDialog(
                    self, "El escrito no puede ser borrado\n" + \
                          str(e)
                ).ShowModal()

                s1.rollback()

        else:
            try:
                s1.add(self.model)
                s1.commit()
                s1.expunge(self.model)
                self.enable_edicion_lista(True)

            except IntegrityError as e:
                wx.MessageDialog(
                    self, "El escrito no puede ser grabado\n" + \
                          str(e)
                ).ShowModal()

                s1.rollback()

    def btDeleteOnButtonClick(self, event):
        event.Skip()

    def btAddOnButtonClick(self, event):
        event.Skip()