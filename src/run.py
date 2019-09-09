"""
To start the software

"""
__author__ = "María Andrea Vignau"

import getpass

import wx
import auth

import vistas
import models
import EdicionUsuario
import Main


class ctrlLogin(vistas.Login):
    resultado = False

    def __init__(self, parent):
        super().__init__(parent)
        self.tcUsuario.SetValue(getpass.getuser())

    def btCancelarOnButtonClick(self, event):
        self.resultado = False
        self.Close()

    def btAceptarOnButtonClick(self, event):
        self.usuario = self.tcUsuario.GetValue()
        self.passw = self.tcPass.GetValue()
        self.resultado = True

        self.Close()


class Login:
    name = None

    def __init__(self):
        window = ctrlLogin(None)
        window.ShowModal()
        if window.resultado:
            self.validate(window)
        window.Destroy()

    def validate(self, window):
        self.name = None
        if auth.test_ldap(window.usuario, window.passw):
            if auth.test_db(window.usuario):
                self.name = window.usuario
            else:
                dlg = EdicionUsuario.ctrlEdicionUsuario(None)
                dlg.ShowModal()
                if dlg.confirm:
                    self.name = window.usuario
                dlg.Destroy()


class App(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def __del__(self):
        pass


if __name__ == "__main__":
    models.run_model()
    app = App()
    usuario = Login()
    if usuario.name:
        app.usuario = usuario
        window = Main.ctrlMain(None)

        window.Show()
        app.MainLoop()
