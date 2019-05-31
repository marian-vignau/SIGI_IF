"""
Model database

"""
__author__ = "María Andrea Vignau"

# coding: utf-8
from pathlib import Path
from sqlalchemy import (
    Column,
    ForeignKey,
    Table,
    Text,
    Integer,
    DateTime,
    Date,
    create_engine,
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

FILEPATH = "database.db"
SQLALCHEMY_ECHO = False
Base = declarative_base()
metadata = Base.metadata


class GenericTable:
    def __repr__(self):
        """Prints every attrib in the object."""
        campos = [str(x).split(".")[1] for x in self.__table__._columns]
        list = []
        for c in campos:
            list.append('%s="%s"' % (c, repr(getattr(self, c))))
        return "%s <%s>\n" % (self.__tablename__, ";".join(list))

    def __init__(self, **kargs):
        """Generic init, every arg is (name, value) of some attrib on table."""
        for key, value in kargs:
            if key in self.__table__._columns:
                self.__setattr__(key, value)
            else:
                raise (
                    ValueError,
                    "{} column not exists on table {}".format(key, self.__tablename__),
                )


class TableEstadoCausa(Base, GenericTable):
    __tablename__ = "TableEstadoCausa"

    id = Column(Integer, primary_key=True)
    descripcion = Column(Text, unique=True)


class TableEstadoInforme(Base, GenericTable):
    __tablename__ = "TableEstadoInforme"

    id = Column(Integer, primary_key=True)
    descripcion = Column(Text)


class TableObjeto(Base, GenericTable):
    __tablename__ = "TableObjeto"

    idObjeto = Column(Integer, primary_key=True)
    objetoRelacionado = Column(ForeignKey("TableObjeto.idObjeto"), nullable=True)
    descripcion = Column(Text)
    ubicacionFisica = Column(Text)
    directorioFotos = Column(Text)
    fechaEntrada = Column(DateTime)
    fechaSalida = Column(DateTime)

    parent = relationship("TableObjeto", remote_side=[idObjeto])


class TableTipoDestinatario(Base, GenericTable):
    __tablename__ = "TableTipoDestinatario"

    id = Column(Integer, primary_key=True)
    descripcion = Column(Text)


class TableUsuario(Base, GenericTable):
    __tablename__ = "TableUsuario"

    id = Column(Text, primary_key=True)
    nombre = Column(Text)
    presentacion = Column(Text)
    sello = Column(Text)
    directorio = Column(Text)
    grupousuario = Column(Text)


class AUDFecha(Base, GenericTable):
    __tablename__ = "AUDFecha"

    idFecha = Column(DateTime, primary_key=True)
    timestamp = Column(Text)
    idUsuario = Column(ForeignKey("TableUsuario.id"))

    TableUsuario = relationship("TableUsuario")


class AUDTableCausa(AUDFecha):
    __tablename__ = "AUDTableCausa"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idCausa = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableDestinatario(AUDFecha):
    __tablename__ = "AUDTableDestinatario"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idSolicitante = Column(Text)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableEscrito(AUDFecha):
    __tablename__ = "AUDTableEscrito"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idCausa = Column(Integer)
    idEscrito = Column(Text)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableEstadoCausa(AUDFecha):
    __tablename__ = "AUDTableEstadoCausa"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idEstado = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableEstadoInforme(AUDFecha):
    __tablename__ = "AUDTableEstadoInforme"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idEstado = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableInforme(AUDFecha):
    __tablename__ = "AUDTableInforme"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idInforme = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableObjeto(AUDFecha):
    __tablename__ = "AUDTableObjeto"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idObjeto = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableRelEscObj(AUDFecha):
    __tablename__ = "AUDTableRelEscObj"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idCausa = Column(Integer)
    idEscrito = Column(Text)
    idObjeto = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableRelInfCau(AUDFecha):
    __tablename__ = "AUDTableRelInfCau"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idInforme = Column(Integer)
    idCausa = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableTipoDestinatario(AUDFecha):
    __tablename__ = "AUDTableTipoDestinatario"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    idTipo = Column(Integer)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class AUDTableUsuario(AUDFecha):
    __tablename__ = "AUDTableUsuario"

    idFecha = Column(ForeignKey("AUDFecha.idFecha"), primary_key=True)
    # idUsuario = Column(ForeignKey('AUDFecha.idUsuario'), primary_key=True)
    idUsuario = Column(Text)
    datosAntiguos = Column(Text)
    datosActualizados = Column(Text)


class TableCausa(Base, GenericTable):
    __tablename__ = "TableCausa"

    idCausa = Column(Integer, primary_key=True)
    expteJud = Column(Text)
    exptePol = Column(Text)
    expteOtro = Column(Text)
    idEstado = Column(ForeignKey("TableEstadoCausa.id"))
    observaciones = Column(Text)
    caratula = Column(Text)
    idDestinatario = Column(ForeignKey("TableDestinatario.id"))

    TableDestinatario = relationship("TableDestinatario")
    TableEstadoCausa = relationship("TableEstadoCausa")
    TableInforme = relationship("TableInforme", secondary="TableRelInfCau")


class TableDestinatario(Base, GenericTable):
    __tablename__ = "TableDestinatario"

    id = Column(Text, primary_key=True)
    nombre = Column(Text)
    circunscripcion = Column(Integer)
    aCargo = Column(Text)
    idTipo = Column(ForeignKey("TableTipoDestinatario.id"))
    correoElectronico = Column(Text)
    telefono = Column(Text)

    TableTipoDestinatario = relationship("TableTipoDestinatario")


class TableInforme(Base, GenericTable):
    __tablename__ = "TableInforme"

    id = Column(Integer, primary_key=True)
    nroInforme = Column(Text)
    idEstado = Column(ForeignKey("TableEstadoInforme.id"))
    observaciones = Column(Text)
    informeRelacionado = Column(Text)
    idProfesional = Column(ForeignKey("TableUsuario.id"))

    TableEstadoInforme = relationship("TableEstadoInforme")
    TableUsuario = relationship("TableUsuario")


class TableRegistroUsuario(Base, GenericTable):
    __tablename__ = "TableRegistroUsuario"

    timestamp = Column(DateTime, primary_key=True)
    idUsuario = Column(ForeignKey("TableUsuario.id"))
    terminalUtilizado = Column(Text)

    TableUsuario = relationship("TableUsuario")


class TableEscrito(Base, GenericTable):
    __tablename__ = "TableEscrito"

    idCausa = Column(ForeignKey("TableCausa.idCausa"), primary_key=True, nullable=False)
    idEscrito = Column(Text, primary_key=True, nullable=False)
    descripcion = Column(Text)
    observaciones = Column(Text)
    ubicacionFisica = Column(Text)
    directorioFotos = Column(Text)
    fechaEntrada = Column(DateTime)
    fechaSalida = Column(DateTime)


    TableCausa = relationship("TableCausa")


class TableInformeDireccione(Base, GenericTable):
    __tablename__ = "TableInformeDirecciones"

    idInforme = Column(ForeignKey("TableInforme.id"), primary_key=True, nullable=False)
    idUsuario = Column(ForeignKey("TableUsuario.id"), primary_key=True, nullable=False)
    directorio = Column(Text)

    TableInforme = relationship("TableInforme")
    TableUsuario = relationship("TableUsuario")


t_TableRelInfCau = Table(
    "TableRelInfCau",
    metadata,
    Column(
        "idInforme", ForeignKey("TableInforme.id"), primary_key=True, nullable=False
    ),
    Column(
        "idCausa", ForeignKey("TableCausa.idCausa"), primary_key=True, nullable=False
    ),
)


class TableRelEscObj(Base, GenericTable):
    __tablename__ = "TableRelEscObj"

    idCausa = Column(
        ForeignKey("TableEscrito.idCausa"), primary_key=True, nullable=False
    )
    idEscrito = Column(
        ForeignKey("TableEscrito.idEscrito"), primary_key=True, nullable=False
    )
    idObjeto = Column(
        ForeignKey("TableObjeto.idObjeto"), primary_key=True, nullable=False
    )

    TableEscrito = relationship(
        "TableEscrito", primaryjoin="TableRelEscObj.idCausa == TableEscrito.idCausa"
    )
    TableEscrito1 = relationship(
        "TableEscrito", primaryjoin="TableRelEscObj.idEscrito == TableEscrito.idEscrito"
    )
    TableObjeto = relationship("TableObjeto")


def objects_rel_causa(idCausa):
    s1 = sessions()
    q1 = (
        s1.query(TableObjeto)
        .join(TableRelEscObj, TableObjeto.idObjeto == TableRelEscObj.idObjeto)
        .filter(TableRelEscObj.idCausa == idCausa)
    )
    return q1


def objects_rel_causa(idCausa):
    s1 = sessions()
    q1 = (
        s1.query(TableObjeto)
            .join(TableRelEscObj, TableObjeto.idObjeto == TableRelEscObj.idObjeto)
            .filter(TableRelEscObj.idCausa == idCausa)
    )
    return q1


def objects_rel_escrito(idCausa, idEscrito):
    s1 = sessions()
    q1 = (
        s1.query(TableRelEscObj)
        .filter(TableRelEscObj.idCausa == idCausa)
        .filter(TableRelEscObj.idEscrito == idEscrito)
    )
    list = [row.idObjeto for row in q1]
    return list


def escritos_rel_objeto(idCausa, idObjeto):
    s1 = sessions()
    q1 = (
        s1.query(TableRelEscObj)
        .filter(TableRelEscObj.idCausa == idCausa)
        .filter(TableRelEscObj.idObjeto == idObjeto)
    )
    list = [row.idEscrito for row in q1]
    return list


def get_escrito(idCausa, idEscrito):
    s1 = sessions()
    q1 = (
        s1.query(TableEscrito)
            .filter(TableEscrito.idCausa == idCausa)
            .filter(TableEscrito.idEscrito == idEscrito)
    )
    if q1:
        return q1[0]
    else:
        return None


def relac_escrito_objeto(idCausa, idEscrito, idObjeto):
    s1 = sessions()
    o1 = TableRelEscObj(idCausa=idCausa, idEscrito=idEscrito, idObjeto=idObjeto)
    s1.append(o1)
    s1.commit()


def next_objeto_id():
    last_id = sessions().query(func.max(TableObjeto.idObjeto)).first()
    if last_id[0] is None:
        return 0
    else:
        return last_id[0] + 1


def init_engine():
    global engine
    global sessions
    global Base
    engine = create_engine("sqlite:///" + str(datapath), echo=SQLALCHEMY_ECHO)
    sessions = sessionmaker()
    sessions.configure(bind=engine)
    Base.metadata.create_all(engine)


def make_backup(basedir, filename):
    import getpass
    import datetime
    import shutil
    current_user = getpass.getuser()
    backupdate = datetime.datetime.now()
    backupname = current_user + "-" + backupdate.isoformat(timespec="seconds") + ".db"
    backupname = backupname.replace(":", "_")
    if Path.is_file(Path(filename)):
        backupdir = basedir.joinpath("backup")
        if not Path.is_dir(backupdir):
            backupdir.mkdir()
        shutil.copy(str(datapath), str(backupdir.joinpath(backupname)))
        # Path.replace(datapath, )
        if not Path.is_file(backupdir.joinpath(backupname)):
            raise (FileNotFoundError, "Backup failed " + str(backupdir.joinpath(backupname)))


basedir = Path.cwd()
while not basedir.joinpath("data").is_dir():
    basedir = basedir.joinpath("..")
datadir = basedir.joinpath("data")
datapath = datadir.joinpath(FILEPATH)
if datapath.is_file():
    make_backup(basedir, datapath)
init_engine()
