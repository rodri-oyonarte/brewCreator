import conect
from flask import Flask,jsonify,json, request,send_file
from sqlalchemy.orm import sessionmaker
from Db_def import Equipo,RecetaCerveza,EtapaReceta, EtapaRecetaRealizada,EtapasCerveza,Ingredientes,IngredienteReceta, CervezaVta, RecetaRealizada

conexionBD=conect.Conexion()
engine=conexionBD.engine()

Session = sessionmaker(bind=engine)
session = Session()

etapa = EtapasCerveza("etapa")
etapa2 = EtapasCerveza("etapa2")
etapa3 = EtapasCerveza("etapa3")

ingrediente1 = Ingredientes("malta","descripcion Malta")
ingrediente2 = Ingredientes("cebada","descripcion Cebada")
ingrediente3 = Ingredientes("lupulo","descripcion Lupulo")

ingreReceta = IngredienteReceta(5)
ingreReceta.Ingrediente = [ingrediente1]
ingreReceta2 = IngredienteReceta(15)
ingreReceta2.Ingrediente = [ingrediente2]
ingreReceta3 = IngredienteReceta(25)
ingreReceta3.Ingrediente = [ingrediente3]

etapaReceta1 = EtapaReceta(30,"descripcion etapa")
etapaReceta1.Etapa = [etapa]
etapaReceta2 = EtapaReceta(50,"descripcion etapa2")
etapaReceta2.Etapa = [etapa2]
etapaReceta3 = EtapaReceta(60,"descripcion etapa3")
etapaReceta3.Etapa = [etapa3]

receta1 = RecetaCerveza("test","tipo1")
etapas =[etapaReceta1,etapaReceta2,etapaReceta3]
ingredientes = [ingreReceta,ingreReceta2,ingreReceta3]
receta1.Etapas.extend(etapas)
receta1.Ingredientes.extend(ingredientes)
session.add(receta1)

cerveza1 = CervezaVta("IPA 1", "IPA", "muy buena", 700, "botella chica", "/img/tst.jpg")
cerveza2 = CervezaVta("HEINEKEN", "PILSNER", "ALEMANA", 5, "KEGGEL", "/img/HEINEKEN.jpg")
cerveza3 = CervezaVta("QUILMES", "BOCK", "CREMOSA", 1, "botella VIDRIO", "/img/QUILMES.jpg")
session.add(cerveza1)
session.add(cerveza2)
session.add(cerveza3)
session.commit()