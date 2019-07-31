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
    event,
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .audit_meta import import audit_session, Versioned
FILEPATH = "auditoria.db"
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




class TableUsuario(Base, GenericTable):
    __tablename__ = "TableUsuario"

    id = Column(Text, primary_key=True)
    nombre = Column(Text)
    presentacion = Column(Text)
    sello = Column(Text)
    directorio = Column(Text)
    grupousuario = Column(Text)


class TableEstadoCausa(Base, GenericTable):
    __tablename__ = "TableEstadoCausa"
    __audit__ = "AUDTableEstadoCausa"

    id = Column(Integer, primary_key=True)
    descripcion = Column(Text, unique=True)


def initSesion(user):


def versioned_objects(iter_):
    for obj in iter_:
        if hasattr(obj, "__audit__"):
            yield obj



def versioned_session(session):
    @event.listens_for(session, "before_flush")
    def before_flush(session, flush_context, instances):
        for obj in versioned_objects(session.dirty):
            create_version(obj, session)
        for obj in versioned_objects(session.deleted):
            create_version(obj, session, deleted=True)

def init_engine():
    global engine
    global sessions
    global Base
    engine = create_engine("sqlite:///" + str(datapath), echo=SQLALCHEMY_ECHO)
    sessions = sessionmaker()
    sessions.configure(bind=engine)
    Base.metadata.create_all(engine)


basedir = Path.cwd()
while not basedir.joinpath("data").is_dir():
    try:
        basedir = basedir.joinpath("..")
    except Exception as e:
        print("Ensure data directory exists")
        raise e


datadir = basedir.joinpath("data")
datapath = datadir.joinpath(FILEPATH)
init_engine()
