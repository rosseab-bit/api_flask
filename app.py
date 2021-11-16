from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import pymysql
import sqlite3
import jinja2
import requests
import secrets
from routes import *
from flask import Blueprint

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.register_blueprint(routes)


server=json.loads(open('conf.d/server.json').read())
if __name__ == '__main__':
        app.jinja_env.filters['zip'] = zip
        app.run(host=server['server']['host'], port=server['server']['port'], debug = True)
