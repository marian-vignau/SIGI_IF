CREATE TABLE TableCausa (
  idCausa TEXT PRIMARY KEY,
  expteJud TEXT,
  exptePol TEXT,
  expteOtro TEXT,
  idEstado TEXT,
  observaciones TEXT,
  caratula TEXT,
  idDestinatario TEXT,
  FOREIGN KEY(idEstado) REFERENCES TableEstadoCausa(id),
  FOREIGN KEY(idDestinatario) REFERENCES TableTipoDestinatario(id)
);

CREATE TABLE TableEscrito (
  idCausa TEXT,
  idEscrito TEXT,
  descipcion TEXT,
  ubicacionFisica TEXT,
  directorioFotos TEXT,
  fechaEntrada TEXT,
  fechaSalida TEXT,
  PRIMARY KEY(idCausa, idEscrito),
  FOREIGN KEY(idCausa) REFERENCES TableCausa(idCausa)
);

CREATE TABLE TableTipoDestinatario (
  id TEXT PRIMARY KEY,
  descripcion TEXT
);

CREATE TABLE TableEstadoInforme (
  id TEXT PRIMARY KEY,
  descripcion TEXT
);

CREATE TABLE TableObjeto (
  idObjeto TEXT PRIMARY KEY,
  objetoRelacionado TEXT,
  descipcion TEXT,
  ubicacionFisica TEXT,
  directorioFotos TEXT,
  fechaEntrada TEXT,
  fechaSalida TEXT,
  FOREIGN KEY(objetoRelacionado) REFERENCES TableObjeto(idObjeto)
);

CREATE TABLE TableRegistroUsuario (
  timestamp TEXT PRIMARY KEY,
  idUsuario TEXT,
  terminalUtilizado TEXT,
  FOREIGN KEY(idUsuario) REFERENCES TableUsuario(id)
);

CREATE TABLE TableRelEscObj (
  idCausa TEXT,
  idEscrito TEXT,
  idObjeto TEXT,
  PRIMARY KEY (idCausa, idEscrito, idObjeto),
  FOREIGN KEY(idCausa) REFERENCES TableEscrito(idCausa),
  FOREIGN KEY(idEscrito) REFERENCES TableEscrito(idEscrito),
  FOREIGN KEY(idObjeto) REFERENCES TableObjeto(idObjeto)
);

CREATE TABLE TableInformeDirecciones (
  idInforme TEXT,
  idUsuario TEXT,
  directorio TEXT,
  PRIMARY KEY (idInforme, idUsuario),
  FOREIGN KEY(idInforme) REFERENCES TableInforme(id),
  FOREIGN KEY(idUsuario) REFERENCES TableUsuario(id)
);

CREATE TABLE TableUsuario (
  id TEXT PRIMARY KEY,
  nombre TEXT,
  presentacion TEXT,
  sello TEXT,
  directorio TEXT
);

CREATE TABLE TableInforme (
  id TEXT PRIMARY KEY,
  nroInforme TEXT,
  idEstado TEXT,
  observaciones TEXT,
  informeRelacionado TEXT,
  idProfesional TEXT,
  FOREIGN KEY(idEstado) REFERENCES TableEstadoInforme(id),
  FOREIGN KEY(idProfesional) REFERENCES TableUsuario(id)
);

CREATE TABLE TableDestinatario (
  id TEXT PRIMARY KEY,
  nombre TEXT,
  circunscripcion TEXT,
  aCargo TEXT,
  idTipo TEXT,
  correoElectronico TEXT,
  telefono TEXT,
  FOREIGN KEY(idTipo) REFERENCES TableTipoDestinatario(id)
);

CREATE TABLE TableRelInfCau (
  idInforme TEXT,
  idCausa TEXT,
  PRIMARY KEY (idInforme, idCausa),
  FOREIGN KEY(idInforme) REFERENCES TableInforme(id),
  FOREIGN KEY(idCausa) REFERENCES TableCausa(idCausa)
);

CREATE TABLE TableEstadoCausa (
  id TEXT PRIMARY KEY,
  descripcion TEXT
);

CREATE TABLE AUDTableEstadoCausa (
  idFecha TEXT PRIMARY KEY,
  idEstado TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableRelInfCau (
  idFecha TEXT PRIMARY KEY,
  idInforme TEXT,
  idCausa TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableInforme (
  idFecha TEXT PRIMARY KEY,
  idInforme TEXT,
  nroInforme TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableRelEscObj (
  idFecha TEXT PRIMARY KEY,
  idEscrito TEXT,
  idObjeto TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableEstadoInforme (
  idFecha TEXT PRIMARY KEY,
  idEstado TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDFecha (
  idFecha TEXT PRIMARY KEY,
  timestamp TEXT,
  idUsuario TEXT,
  FOREIGN KEY(idUsuario) REFERENCES TableUsuario(id)
);

CREATE TABLE AUDTableTipoDestinatario (
  idFecha TEXT PRIMARY KEY,
  idTipo TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableDestinatario (
  idFecha TEXT PRIMARY KEY,
  idSolicitante TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableObjeto (
  idFecha TEXT PRIMARY KEY,
  idObjeto TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableCausa (
  idFecha TEXT PRIMARY KEY,
  idCausa TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableEscrito (
  idFecha TEXT PRIMARY KEY,
  idCausa TEXT,
  idEscrito TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);

CREATE TABLE AUDTableUsuario (
  idFecha TEXT PRIMARY KEY,
  idUsuario TEXT,
  datosAntiguos TEXT,
  datosActualizados TEXT,
  FOREIGN KEY(idFecha) REFERENCES AUDFecha(idFecha)
);
