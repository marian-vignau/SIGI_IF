import wx
from sqlalchemy.exc import IntegrityError

from vistas import EdicionObjeto
import models
import PanelObjeto

BORRAR_LABEL = "Borrar"

class ctrlEdicionObjeto (EdicionObjeto):
    def __init__(self,  parent, idObjeto=None, delete=False):
        super().__init__(parent)
        itemsizer = self.GetSizer().GetItem(self.paObjeto, recursive=True)
        self.paObjetoNvo = PanelObjeto.ctrlPanelObjeto(self, idCausa)
        itemsizer.AssignWindow(self.paObjetoNvo)
        self.paObjeto.Destroy()
        self.Layout()
        if idObjeto is None:
            #self.enable_edicion_Objetos(False)
            self.model = models.TableObjeto()
        else:
            s1 = models.sessions()
            self.model = s1.query(models.TableObjeto)\
                .filter(models.TableObjeto.idObjeto == idObjeto).first()
            self.paObjetoNvo.from_model(self.model)
            s1.expunge(self.model)
        if delete:
            self.paObjetoNvo.mapper.enable(False)
            self.btGuardar.SetLabel(BORRAR_LABEL )


    def btReestablecerOnButtonClick(self, event):
        self.paObjetoNvo.from_model(self.model)

    def btGuardarOnButtonClick(self, event):
        s1 = models.sessions()
        self.paObjetoNvo.to_model(self.model)
        if self.btGuardar.GetLabel() == BORRAR_LABEL:
            try:
                s1.add(self.model)
                s1.delete(self.model)
                s1.commit()
                s1.expunge(self.model)
            except IntegrityError as e:
                wx.MessageDialog(
                    self, "El Objeto no puede ser borrado\n" + \
                          str(e)
                ).ShowModal()

                s1.rollback()

        else:
            try:
                s1.add(self.model)
                s1.commit()
                s1.expunge(self.model)

            except IntegrityError as e:
                wx.MessageDialog(
                    self, "El Objeto no puede ser grabado\n" + \
                          str(e)
                ).ShowModal()

                s1.rollback()
