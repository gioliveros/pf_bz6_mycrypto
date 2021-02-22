from movements import app
from movements.forms import MomvementForm
from flask import render_template, request, url_for, redirect
import csv
import sqlite3
from datetime import date

DBFILE = 'movements/data/bbddmycrypto.db'

def consulta(query, params=()):
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    c.execute(query, params)
    conn.commit()

    filas = c.fetchall()
    print(filas)
    conn.close()

    if len(filas) == 0:
        return filas

    columnNames = []
    for columnName in c.description:
        columnNames.append(columnName[0])

    listaDeDiccionarios = []

    for fila in filas:
        d = {}
        for ix, columnName in enumerate(columnNames):
            d[columnName] = fila[ix]
        listaDeDiccionarios.append(d)

    return listaDeDiccionarios

@app.route('/')

def cryptoMovements():
    movimientos = consulta('SELECT fecha, hora, moneda_from, cantidad_from, moneda_to, cantidad_to')
    total = 0
    for movimiento in movimientos:
        total += movimientos    
    return render_template("movementList.html", datos=movimientos, title="Todos los movimientos")

@app.route('/')

def cryptoMovements():
    movimientos = consulta('SELECT fecha, hora, moneda_from, cantidad_from, moneda_to, cantidad_to')
    total = 0
    for movimiento in movimientos:
        total += movimientos    
    return render_template("movementList.html", datos=movimientos, title="Todos los movimientos")