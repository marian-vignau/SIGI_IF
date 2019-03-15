"""
To show fields of escritos

"""
__author__ = "María Andrea Vignau"

from vistas import PanelEscrito
from wxSQAlch.Mapper import Mapper, MapObj


class ctrlPanelEscrito(PanelEscrito):
    def __init__(self, parent, idCausa):
        self.idCausa = idCausa
        super().__init__(parent)
        self.mapper = Mapper(
            MapObj(self.tcIdEscrito, "idEscrito"),
            MapObj(self.tcDescripcion, "descripcion"),
            MapObj(self.tcFotos, "directorioFotos"),
            MapObj(self.tcUbicacionFisica, "ubicacionFisica"),
            MapObj(self.dpIngreso, "fechaEntrada"),
            MapObj(self.dpSalida, "fechaSalida"),
        )
        # print(repr(self.mapper))

    def to_model(self, model):
        self.mapper.to_model(model)
        model.idCausa = self.idCausa
        return model

    def from_model(self, model):
        self.mapper.from_model(model)
        self.idCausa = model.idCausa
        return model

    def clear(self):
        self.mapper.clear()
