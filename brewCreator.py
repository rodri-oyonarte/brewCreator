from flask import Flask,jsonify,json, request,send_file
from sqlalchemy.orm import sessionmaker
from Db_def import Equipo,RecetaCerveza,EtapaReceta, EtapaRecetaRealizada,EtapasCerveza,Ingredientes,IngredienteReceta, CervezaVta, RecetaRealizada
import conect
import find, datetime

app = Flask(__name__)
conexionBD=conect.Conexion()
engine=conexionBD.engine()

Session = sessionmaker(bind=engine)
session = Session()
"""
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
"""

#-------------------------------------equipo---------------------------------------------------
# POST crear equipo nuevo
""""
recibe
{
    fermentador:INT,
    airlock: Boolean(0 o 1),
    densimetro: Boolean(0 o 1),
    termometro: Boolean(0 o 1),
    tuboDeTrasiego: Boolean(0 o 1),
    pipetaEmbotellar: Boolean(0 o 1),
    molino: Boolean(0 o 1),
    macerador: INT,
    bolsaGrano: Boolean(0 o 1),
    rejillaDobleFondo: Boolean(0 o 1),
    ollaCoccion: INT,
    enfriador: Boolean(0 o 1),
    probeta: Boolean(0 o 1),
    pala: Boolean(0 o 1)
    idUsuario: INT
}
"""

@app.route('/Equipo',methods=['POST'])
def equipo():
        equipoJson = request.get_json()
        ##equipo = Equipo(fermentador,airlock,densimetro,termometro,tuboDeTrasiego,pipetaEmbotellar,molino,macerador,bolsaGrano,rejillaDobleFondo,ollaCoccion,enfriador,probeta,pala)
        equipo = Equipo()

        equipo.fermentador = equipoJson["fermentador"]
        equipo.airlock = equipoJson["airlock"]
        equipo.densimetro = equipoJson["densimetro"]
        equipo.termometro = equipoJson["termometro"]
        equipo.tuboDeTrasiego = equipoJson["tuboDeTrasiego"]
        equipo.pipetaEmbotellar = equipoJson["pipetaEmbotellar"]
        equipo.molino = equipoJson["molino"]
        equipo.macerador = equipoJson["macerador"]
        equipo.bolsaGrano = equipoJson["bolsaGrano"]
        equipo.rejillaDobleFondo = equipoJson["rejillaDobleFondo"]
        equipo.ollaCoccion = equipoJson["ollaCoccion"]
        equipo.enfriador = equipoJson["enfriador"]
        equipo.probeta = equipoJson["probeta"]
        equipo.pala = equipoJson["pala"]
        equipo.Usuario = find.findUsuario(session,equipo["idUsuario"])

        session.add(equipo)
        session.commit()
        return jsonify(equipoJson)


# GET enviar equipo cargado
@app.route('/Equipo/<idUsuario>',methods=['GET'])
def getEquipo(idUsuario):

    equipoEncontrado = find.findEquipo(session,idUsuario)

    if(equipoEncontrado != None):
        equipoJson = json.dumps({
            'equipoID': equipoEncontrado.idEquipo,
            'fermentador': equipoEncontrado.fermentador,
            'airlock': equipoEncontrado.airlock,
            'densimetro': equipoEncontrado.densimetro,
            'termometro': equipoEncontrado.termometro,
            'tuboDeTrasiego': equipoEncontrado.tuboDeTrasiego,
            'pipetaEmbotellar': equipoEncontrado.pipetaEmbotellar,
            'molino': equipoEncontrado.molino,
            'macerador':equipoEncontrado.macerador,
            'bolsaGrano':equipoEncontrado.bolsaGrano,
            'rejillaDobleFondo':equipoEncontrado.rejillaDobleFondo,
            'ollaCoccion':equipoEncontrado.ollaCoccion,
            'enfriador':equipoEncontrado.enfriador,
            'probeta':equipoEncontrado.probeta,
            'pala':equipoEncontrado.pala
        })
    else:
        equipoJson = "el usuario no contiene Equipo"

    return equipoJson

# DELETE eliminar equipo
@app.route('/Equipo/<idUsuario>',methods=['DELETE'])
def borrarEquipo(idUsuario):
    equipoEncontrado = find.findEquipo(session, idUsuario)
    if(equipoEncontrado != None):
        session.delete(equipoEncontrado)
        session.commit()
        rta = "equipo eliminado"
    else:
        rta = "No se encontro equipo"
    return rta

#--------------------------------------------recetas------------------------------------------
# GET recetas (nombres y ids de las recetas que existen)
""""
{
    {
        idReceta:INT,
        nombreReceta: String,
        tipo: String
    },
    {
        idReceta:INT,
        nombreReceta: String,
        tipo: String
    },
    ...
}
"""
@app.route('/Receta',methods=['GET'])
def getRecetas():

    Recetas = find.findReceta(session)
    return jsonify(Recetas)

# GET receta %id (envia la receta requerida por id)
"""
{
    nombreReceta:"",
    ingredientes: {},
    etapas:{
        {
            nombreEtapa:"",
            descripcion:"",
            tiempoInicio:"",
            duracion:""
        },
        {
            nombreEtapa:"",
            descripcion:"",
            tiempoInicio:"",
            duracion:""},
        ...
        }
}
"""
@app.route('/Receta/<idReceta>',methods=['GET'])
def getRecetasId(idReceta):
    Receta = find.findRecetaId(session,idReceta)
    return jsonify(Receta)


# POST asociar una receta a un usuario (recibir Id de receta y datos de usuario)
@app.route('/Receta/<idUsuario>/<idReceta>',methods=['POST'])
def empezarReceta(idUsuario,idReceta):
    recetaNueva = RecetaRealizada()
    Receta = find.findObjReceta(session,idReceta)
    Usuario = find.findUsuario(session,idUsuario)
    recetaNueva.Receta.append(Receta)
    for row in (Receta.Etapas):
        etapaRealizada = EtapaRecetaRealizada()
        etapaRealizada.idEtapaReceta = row.idEtapaReceta
        etapaRealizada.tiempoIdeal = row.tiempo
        etapaRealizada.NombreEtapa = row.Etapa[0].nombre
        #etapaRealizada.tiempoInicio = datetime.datetime.now()
        etapaRealizada.numeroEtapa = row.Etapa[0].orden
        recetaNueva.EtapasRealizadas.append(etapaRealizada)


    Usuario.RecetasRealizadas.append(recetaNueva)
    session.add(recetaNueva)
    session.commit()
    return "Receta iniciada"

# UPDATE iniciar etapa
@app.route('/etapaRealizada/<idEtapa>',methods=['POST'])
def iniciarEtapa(idEtapa):
    etapaRealizada = find.findEtapaRealizada(session,idEtapa)
    etapaRealizada.tiempoInicio = datetime.datetime.now()
    session.commit()

    return ""

#UPDATE finalizar etapa
@app.route('/etapaRealizada/fin/<idEtapa>',methods=['POST'])
def finalizarEtapa(idEtapa):
    etapaRealizada = find.findEtapaRealizada(session,idEtapa)
    etapaRealizada.tiempoFinal = datetime.datetime.now()
    session.commit()

    return ""
#--------------------------------------Cerveceros-------------------------------------------
# GET Cerveceros listado de cerveza ofrecidas
"""
{
}
"""
@app.route('/Cerveceros',methods=['GET'])
def getCervezas():
    Cervezas = find.findCervezas(session)
    return jsonify(Cervezas)

# POST Cerveceros Cargar cervezas para ofrecer
""""
{}
"""
@app.route('/Cerveceros',methods=['POST'])
def postCerveza():
    cervezaJson = request.get_json()
    cerveza = CervezaVta()

    cerveza.nombre = cervezaJson["nombre"]
    cerveza.tipoCerveza = cervezaJson["tipoCerveza"]
    cerveza.descripcion = cervezaJson["descripcion"]
    cerveza.envase = cervezaJson["envase"]
    cerveza.tamaño = cervezaJson["tamaño"]
    cerveza.rutaImagen = "/img/"+cervezaJson["nombreImagen"]

    session.add(cerveza)
    session.commit()

    return cervezaJson

#--------------------------------------IMAGENES-------------------------------------------
@app.route('/Img/<imgRoute>',methods=['GET'])
def getImg(imgRoute):
    return send_file(imgRoute, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
