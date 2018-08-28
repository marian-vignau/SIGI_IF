from vistas import PanelEscrito
from wxSQAlch.Mapper import Mapper, MapObj, MapDate

class ctrlPanelEscrito(PanelEscrito):
    def __init__(self,  parent, idCausa):
        self.idCausa = idCausa
        super().__init__(parent)
        self.mapper = Mapper(
            MapObj(self.tcDescripcion, "descripcion"),
            MapObj(self.tcFotos, "directorioFotos"),
            MapObj(self.tcUbicacionFisica, "ubicacionFisica"),
            MapObj(self.dpIngreso, "fechaEntrada"),
            MapObj(self.dpSalida, "fechaSalida")
        )

    def to_model(self, model):
        self.mapper.to_model(model)
        return model

    def from_model(self, model):
        self.mapper.from_model(model)
        return model

    def clear(self):
        self.mapper.clear()
