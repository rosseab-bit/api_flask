from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import pymysql
import sqlite3
import jinja2
import json
import requests
import secrets
from . import routes
@routes.route('/', methods=['GET', 'POST'])
def dbGet():
    # primero analizo el metodo post
    if request.method == "POST":
        db=json.loads(open('database/db.json').read())
        # una vez que este en post tomo los datos del req
        req = request.json
        print(req)
        req['id']=secrets.token_hex(20)
        # cargo los datos del req
        db['data'].append(req)
        data = open('database/db.json', 'w')
        data.write(json.dumps(db, indent=4))
        data.close()
        return jsonify(db)
    if request.method == "GET":
        db=json.loads(open('database/db.json').read())
        # si el metodo es GET solo devuelvo los datos.
        return jsonify(db)

@routes.route('/delete/<string:id>', methods=['DELETE'])
def dbDelete(id):
    if request.method == "DELETE":
        db=json.loads(open('database/db.json').read())
        updateDB=[]
        for item in db['data']:
            if item['id']!=id:
                updateDB.append(item)
        db['data']=updateDB
        data = open('database/db.json', 'w')
        data.write(json.dumps(db, indent=4))
        data.close()
        return id

@routes.route('/update/<string:id>', methods=['PUT'])
def dbPut(id):
    if request.method == "PUT":
        db=json.loads(open('database/db.json').read())
        req=request.json
        print(req)
        update_db=[]
        for item in db['data']:
            if item['id']==id:
                item['correo']=req['correo']
                item['nombre']=req['nombre']
                item['telefono']=req['telefono']
                item['empresa']=req['empresa']
            update_db.append(item)
        db['data']=update_db
        data = open('database/db.json', 'w')
        data.write(json.dumps(db, indent=4))
        data.close()
        return "ok"
