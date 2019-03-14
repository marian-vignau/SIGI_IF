from vistas import PanelObjeto
from wxSQAlch.Mapper import Mapper, MapObj, MapList
import models


class ctrlPanelObjeto(PanelObjeto):
    def __init__(self,  parent, ObjetoRelacionado = ""):
        super().__init__(parent)
        self.mapper = Mapper(
            MapObj(self.tcDescripcion, "descripcion"),
            MapObj(self.tcUbicacionFisica, "ubicacionFisica"),
            MapObj(self.tcFotos, "directorioFotos"),
            MapObj(self.dpIngreso, "fechaEntrada"),
            MapObj(self.dpSalida, "fechaSalida")
        )
        self.lblObjetoRelacionado.SetLabel(ObjetoRelacionado)

    def to_model(self, model):
        self.mapper.to_model(model)
        return model

    def from_model(self, model):
        self.mapper.from_model(model)
        return model

    def clear(self):
        self.mapper.clear()
