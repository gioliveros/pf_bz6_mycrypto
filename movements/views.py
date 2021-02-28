from movements import app
from flask import render_template, request, url_for, redirect
import sqlite3
from datetime import date

DBFILE = 'movements/data/bdmycrypto.db'

@app.route('/') #Home es una página de bienvenida sin contenido#
def homemyCrypto():
    return render_template("Home.html", title="Bienvenido a myCrypto")

@app.route('/inicio') #Aquí devolvemos la relacion de movimientos existentes en la BBDD#
conn = sqlite3.connect('movements/data/bdmycrypto.db')
c = conn.cursor()
def listaMovimientos():
    listaMovimientos = c.execute("SELECT * FROM movimientos)
    c.fetchall()
conn.commit()
conn.close()
    return render_template("inicio.html", title="Todos los movimientos")

@app.route('/compra')
def compraCrypto():
    return render_template("compra.html", title="Compra de Cryptomonedas")

@app.route('/status')
def statusCrypto():
    return render_template("status.html", title="Status de Operaciones realizadas")

@app.route('/testing')
def testingCrypto():
    return render_template("testing.html", title="Página de test de códigos")