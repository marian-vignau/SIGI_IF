"""
Show main window
"""
__author__ = "María Andrea Vignau"


from wxSQAlch import ListViewObject
from vistas import Main
import models
import EdicionCausa


class ctrlMain(Main):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_lista_causas()

    def init_lista_causas(self):
        # for normal, simple columns, you can add them like this:
        self.list = ListViewObject.ListViewObject(
            self.lsPrincipal,
            [
                ListViewObject.Column("Exp Judicial", "expteJud"),
                ListViewObject.Column("Carátula", "caratula"),
                ListViewObject.Column("Exp Policial", "exptePol"),
                ListViewObject.Column("Id", "idCausa"),
            ],
            itemkey="idCausa",
        )
        s1 = models.sessions()
        for row in s1.query(models.TableCausa).all():
            self.list.change_item_list(row)

    def lsPrincipalOnLeftDClick(self, event):
        idCausa = self.list.get_key()
        dlg = EdicionCausa.ctrlEdicionCausa(self, idCausa)
        dlg.ShowModal()
        self.list.change_item_list(dlg.model)

    def scBuscarOnSearchButton(self, event):
        event.Skip()

    def mnuCausaAgregarOnMenuSelection(self, event):
        dlg = EdicionCausa.ctrlEdicionCausa(self)
        dlg.ShowModal()
        self.list.change_item_list(dlg.model)
