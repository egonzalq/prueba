import sqlite3
from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template,request,flash
from wtforms.compat import with_metaclass
from formularios import formVuelos
import os
import _sqlite3


DATABASE_NAME = "olaya.db"
from sqlite3 import Error

def get_db():
    conn=sqlite3.connect(DATABASE_NAME)
    return conn


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/Vuelos/save", methods=["POST"] )
def vuelos_save():
    form=formVuelos()
    if request == 'POST':
        vuelos =form.vuelo.data
        aerolinea = form.aerolinea.data
        ciudad = form.ciudad.data
        hora = form.hora.data
        estado=form.estado.data
        try:
            with sqlite3.connect("Data/olaya.db") as con:
                cur = con.cursor()#realiza la conexion a la base de datos
                cur.execute("INSERT INTO vuelos(ID_VUELOS,AEROLINEA,CIUDAD,HORA,ESTADO) VALUES(?,?,?,?,?)",
                (vuelos,aerolinea,ciudad,hora,estado))
                con.commit()#confirme la transaccion
                return "Guardado Satisfactoriamente"
        except(Error):
            print(Error)
    return "No se pudo guardar"


if __name__=="__main__":
    app.run(port=5000, debug=True)    