"""
Show main window
"""
__author__ = "María Andrea Vignau"

import wx
from wxSQAlch import ListViewObject
from wxSQAlch import Tools
from vistas import Main
import models
import EdicionCausa
import EdicionUsuario


class ctrlMain(Main):
    def __init__(self, parent):
        super().__init__(parent)
        Tools.changeFont(self, 2)
        self.init_lista_causas()

    def init_lista_causas(self):
        # for normal, simple columns, you can add them like this:
        self.list = ListViewObject.ListViewObject(
            self.lsPrincipal,
            [
                ListViewObject.Column("Exp Judicial", "expteJud"),
                ListViewObject.Column("Carátula", "caratula", size=3),
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
        self.list.change_item_list(dlg.model, add=True)

    def mnuEditarUsuarioOnMenuSelection(self, event):
        app = wx.GetApp()
        dlg = EdicionUsuario.ctrlEdicionUsuario(self, app.usuario)
        dlg.ShowModal()
