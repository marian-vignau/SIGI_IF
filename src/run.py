"""
To start the software

"""
__author__ = "María Andrea Vignau"

import wx
import vistas
import models
import Main
import getpass


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
            s1 = models.sessions()
            userlogin = (
                s1.query(models.TableUsuario)
                .filter(models.TableUsuario.id == window.usuario)
                .first()
            )
            if userlogin:
                self.name = window.usuario
            else:
                self.name = None
        self.name = getpass.getuser()  # disables control of login
        window.Destroy()


class App(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def __del__(self):
        pass


if __name__ == "__main__":
    app = App()
    usuario = Login()
    if usuario.name:
        window = Main.ctrlMain(None)

        window.Show()
        app.MainLoop()
