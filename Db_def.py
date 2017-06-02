from sqlalchemy import create_engine, ForeignKey, Table
from sqlalchemy import Column, Date, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

import conect

conexionBD=conect.Conexion()
print("voya crear conexion en modelo")
engine=conexionBD.engine()

Base = declarative_base()
#Relaciones
Equipo_Usuario = Table('Equipo_Usuario', Base.metadata,
    Column('idUsuario', Integer, ForeignKey('Usuario.idUsuario')),
    Column('idEquipo', Integer, ForeignKey('Equipo.idEquipo')))

Receta_Usuario = Table('Receta_Usuario', Base.metadata,
    Column('idUsuario', Integer, ForeignKey('Usuario.idUsuario')),
    Column('idRecetaRealizada', Integer, ForeignKey('RecetaRealizada.idRecetaRealizada')))

Receta_RecetaRealizada = Table('Receta_RecetaRealizada', Base.metadata,
    Column('idReceta', Integer, ForeignKey('RecetaCerveza.idReceta')),
    Column('idRecetaRealizada', Integer, ForeignKey('RecetaRealizada.idRecetaRealizada')))

Receta_Etapa = Table('Receta_Etapa', Base.metadata,
    Column('idReceta', Integer, ForeignKey('RecetaCerveza.idReceta')),
    Column('idEtapaReceta', Integer, ForeignKey('EtapaReceta.idEtapaReceta')))

EtapaCerveza_EtapaReceta = Table('EtapaCerveza_EtapaReceta', Base.metadata,
    Column('idEtapa', Integer, ForeignKey('EtapasCerveza.idEtapa')),
    Column('idEtapaReceta', Integer, ForeignKey('EtapaReceta.idEtapaReceta')))

IngredienteReceta_Receta = Table('IngredienteReceta_Receta', Base.metadata,
    Column('idReceta', Integer, ForeignKey('RecetaCerveza.idReceta')),
    Column('id', Integer, ForeignKey('IngredienteReceta.id')))

IngredienteReceta_Ingrediente = Table('IngredienteReceta_Ingrediente', Base.metadata,
    Column('idIngrediente', Integer, ForeignKey('Ingrediente.idIngrediente')),
    Column('id', Integer, ForeignKey('IngredienteReceta.id')))

RecetaRealizada_Etapa = Table('RecetaRealizada_Etapa', Base.metadata,
    Column('idEtapaRecetaRealizada', Integer, ForeignKey('EtapaRecetaRealizada.idEtapaRecetaRealizada')),
    Column('idRecetaRealizada', Integer, ForeignKey('RecetaRealizada.idRecetaRealizada')))

########################################################################
class Equipo(Base):

    __tablename__ = "Equipo"

    idEquipo = Column(Integer, primary_key=True, autoincrement=True)
    fermentador = Column(Integer)
    airlock = Column(Integer)
    densimetro = Column(Integer)
    termometro = Column(Integer)
    tuboDeTrasiego = Column(Integer)
    pipetaEmbotellar = Column(Integer)
    molino = Column(Integer)
    macerador = Column(Integer)
    bolsaGrano = Column(Integer)
    rejillaDobleFondo = Column(Integer)
    ollaCoccion = Column(Integer)
    enfriador = Column(Integer)
    probeta = Column(Integer)
    pala = Column(Integer)

    #idUsuario = Column(Integer)




    #----------------------------------------------------------------------
    def __init__(self,fermentador=0,airlock=0,densimetro=0,termometro=0,
                 tuboDeTrasiego=0,pipetaEmbotellar=0,molino=0,macerador=0,bolsaGrano=0,
                 rejillaDobleFondo=0,ollaCoccion=0,enfriador=0,probeta=0,pala=0):

        self.fermentador = fermentador
        self.airlock = airlock
        self.densimetro = densimetro
        self.termometro = termometro
        self.tuboDeTrasiego = tuboDeTrasiego
        self.pipetaEmbotellar = pipetaEmbotellar
        self.molino = molino
        self.macerador = macerador
        self.bolsaGrano = bolsaGrano
        self.rejillaDobleFondo = rejillaDobleFondo
        self.ollaCoccion = ollaCoccion
        self.enfriador = enfriador
        self.probeta = probeta
        self.pala = pala

########################################################################
class RecetaCerveza(Base):

    __tablename__ = "RecetaCerveza"

    idReceta = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(60))
    tipo = Column(String(60))

    # Etapas q contiene la receta
    Etapas = relationship("EtapaReceta", secondary=Receta_Etapa)

    # ingredientes que contiene la receta
    Ingredientes = relationship("IngredienteReceta", secondary=IngredienteReceta_Receta)

    def __init__(self,nombre="",tipo=""):
        self.nombre = nombre
        self.tipo = tipo

########################################################################
class CervezaVta(Base):

    __tablename__ = "CervezaVta"

    idCerveza = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(60))
    tipoCerveza = Column(String(60))
    descripcion = Column(String(240))
    tamaño = Column(Integer)
    envase = Column(String(60))
    rutaImagen = Column(String(60))

    def __init__(self,nombreCerveza="",tipo="",descripcion="",tamaño=0,envase="",rutaImagen=""):
        self.nombre = nombreCerveza
        self.tipoCerveza = tipo
        self.descripcion = descripcion
        self.tamaño = tamaño
        self.envase = envase
        self.rutaImagen = rutaImagen

########################################################################
class EtapasCerveza(Base):

    __tablename__ = "EtapasCerveza"

    idEtapa = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String(60))
    orden = Column(Integer)


    def __init__(self,nombre=""):
        self.nombre = nombre

######################################################################
class Usuario(Base):
    __tablename__ = "Usuario"

    idUsuario = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(60))
    contraseña = Column(String(60))

    Equipo = relationship("Equipo", secondary=Equipo_Usuario)

    RecetasRealizadas = relationship("RecetaRealizada", secondary=Receta_Usuario)

    def __init__(self, nombre="", contraseña=""):
        self.nombre = nombre
        self.contraseña = contraseña



######################################################################
class Ingredientes(Base):
    __tablename__ = "Ingrediente"

    idIngrediente = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(60))
    descripcion = Column(String(120))

    def __init__(self,nombre="", descripcion="" ):
        self.nombre = nombre
        self.descripcion = descripcion

######################################################################
class IngredienteReceta(Base):
    __tablename__ = "IngredienteReceta"

    id = Column(Integer, primary_key=True,autoincrement=True)
    cantidad = Column(Integer)

    # idEtapa = Column(Integer)
    Ingrediente = relationship("Ingredientes", secondary=IngredienteReceta_Ingrediente)

    def __init__(self, cantidad=0 ):
        self.cantidad = cantidad

#####################################################################
class EtapaReceta(Base):
    __tablename__ = "EtapaReceta"

    idEtapaReceta = Column(Integer, primary_key=True,autoincrement=True)
    tiempo = Column(Integer)
    descripcion = Column(String(120))

    # idEtapa = Column(Integer)
    Etapa = relationship("EtapasCerveza", secondary=EtapaCerveza_EtapaReceta)

    def __init__(self, tiempo="",descripcion="" ):
        self.tiempo = tiempo
        self.descripcion = descripcion

#####################################################################
class RecetaRealizada(Base):
    __tablename__ = "RecetaRealizada"

    idRecetaRealizada = Column(Integer, primary_key=True,autoincrement=True)
    VarianteAlaReceta = Column(String(120))


    #idReceta = Column(Integer)
    Receta = relationship("RecetaCerveza",secondary = Receta_RecetaRealizada)

    EtapasRealizadas = relationship("EtapaRecetaRealizada",secondary = RecetaRealizada_Etapa)

    def __init__(self, VarianteAlaReceta=0):
        self.VarianteAlaReceta = VarianteAlaReceta

#####################################################################
class EtapaRecetaRealizada(Base):
    __tablename__ = "EtapaRecetaRealizada"

    idEtapaRecetaRealizada = Column(Integer, primary_key=True,autoincrement=True)
    idEtapaReceta = Column(Integer)
    numeroEtapa = Column(Integer)
    NombreEtapa = Column(String(60))
    tiempoIdeal = Column(Integer)
    tiempoInicio = Column(DateTime)
    tiempoFinal = Column(DateTime)
    Variantes = Column(String(240))

    def __init__(self, tiempo=0, idEtapaReceta = 0 ):
        self.tiempoIdeal = tiempo
        self.idEtapaReceta = idEtapaReceta

# create tables
Base.metadata.create_all(engine)