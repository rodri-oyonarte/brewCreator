from Db_def import Equipo,Usuario,RecetaCerveza, EtapaReceta, CervezaVta, EtapaRecetaRealizada
from sqlalchemy import text
from flask import jsonify


def findEquipo(session,idEquipo):
    busqueda = session.query(Equipo).filter(Equipo.idEquipo == idEquipo).first()
    return busqueda

def findUsuario(session,idUsuario):

    busqueda = session.query(Usuario).filter(Usuario.idUsuario == idUsuario).first()
    return busqueda

def findEtapaRealizada(session,idEtapa):

    busqueda = session.query(EtapaRecetaRealizada).filter(EtapaRecetaRealizada.idEtapaRecetaRealizada == idEtapa).first()
    return busqueda

def findReceta(session):
    busqueda = session.execute(text("SELECT * FROM RecetaCerveza"))
    res = []
    for row in busqueda:
        data={"idReceta":row[0],"nombre":row[1],"tipo":row[2]}
        res.append(data)
    return res

def findRecetaId(session,idReceta):
    etapas = []
    ingredientes = []
    busqueda = session.query(RecetaCerveza).filter(RecetaCerveza.idReceta == idReceta).first()
    print("-------------------")
    print(busqueda.nombre, busqueda.tipo, len(busqueda.Etapas))
    for row in busqueda.Etapas:
        tst = row.tiempo
        dataEtapa={"idEtapaReceta":row.idEtapaReceta,"etapaNombre":row.Etapa[0].nombre, "tiempo":row.tiempo,"descripcion":row.descripcion}
        etapas.append(dataEtapa)

    for row in busqueda.Ingredientes:
        dataIng ={"nombreIngrediente":row.Ingrediente[0].nombre,"cantidad":row.cantidad}
        ingredientes.append(dataIng)

    data = {
        "idReceta": idReceta,
        "nombreReceta": busqueda.nombre,
        "tipoReceta": busqueda.tipo,
        "Etapas": etapas,
        "Ingredientes": ingredientes
    }
    print(data)
    return data

def findObjReceta(session,idReceta):
    busqueda = session.query(RecetaCerveza).filter(RecetaCerveza.idReceta == idReceta).first()
    return  busqueda

def findCervezas(session):
    res = []
    busqueda = session.query(CervezaVta).all()
    for row in busqueda:
        data = {"id": row.idCerveza,
                "nombreCerveza": row.nombre,
                "tipo": row.tipoCerveza,
                "descripcion":row.descripcion,
                "tamaño":row.tamaño,
                "envase":row.envase,
                "rutaImagen":row.rutaImagen}
        res.append(data)
    print(res)
    return res
