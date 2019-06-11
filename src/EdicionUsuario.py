__author__ = "María Andrea Vignau"

import getpass
import wx

from vistas import EdicionUsuario
import models
import auth

from wxSQAlch import Tools
from wxSQAlch.Mapper import Mapper, MapObj


class ctrlEdicionUsuario(EdicionUsuario):

    def __init__(
            self,
            parent,
            usuario=None
    ):
        super().__init__(parent)
        self.confirm = False
        self.mapper = Mapper(
            MapObj(self.tcUsuario, "id"),
            MapObj(self.tcNombre, "nombre"),
            MapObj(self.tcPresentacion, "presentacion"),
            MapObj(self.tcSello, "sello"),
            MapObj(self.tcDirectorio, "directorio"),
            MapObj(self.chGrupo, "grupousuario"),
        )
        if usuario is None:
            self.mapper.id = getpass.getuser()
            self.model = models.TableUsuario()
        else:
            s1 = models.sessions()
            self.model = (
                s1.query(models.TableUsuario)
                .filter(models.TableUsuario.id == usuario.name)
                .first()
            )
            self.mapper.from_model(self.model)
            s1.expunge(self.model)

        Tools.changeFont(self, 2)

    def btGuardarOnButtonClick(self, event):

        if auth.test_ldap(self.tcUsuario.GetValue(), self.tcClave.GetValue()):
            wx.MessageBox("El usuario es correcto! Guardando", "")
            s1 = models.sessions()

            self.mapper.to_model(self.model)
            s1.add(self.model)
            s1.commit()
            self.confirm = True
            self.Close()
        else:
            print(self.mapper.id, self.tcClave.GetValue())
            wx.MessageBox("Ingrese un usuario de windows correcto", "")

    def btCancelarOnButtonClick( self, event ):
        self.Close()