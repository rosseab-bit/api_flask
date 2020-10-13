from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql
import sqlite3
import jinja2

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def apiInfo():
	info = '''<h1>Server bot informations</h1>
	<p>This API need a number key for get info.</p>
	<p>route: /api_server/id/option</p>
	<p>Options: [status, stop, start]</p>'''
	return info

@app.route('/api_server/<string:id>/<string:option>', methods=['GET'])
def infoServer(id, option):
	if str(id) == 'batman':
		return 'sucess'
	else:
		info = '''<h1>Server bot informations</h1>
		<p>This API need a number key for get info.</p>
		<p>Acces denegated, number key invalid</p>
		<p>Options: [status, stop, start]</p>'''
		return info


if __name__ == '__main__':
	app.jinja_env.filters['zip'] = zip
	app.run(port = 3000, debug = True)
