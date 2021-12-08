from flask import Flask, request,jsonify,redirect,render_template
from flask_cors import CORS
from flask_classful import FlaskView,route
from flask_mysqldb import MySQL
from Details import Products
import stripe

app = Flask(__name__)

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='flask'

mysql = MySQL(App)


CORS(app)

class GateWay(FlaskView):

	def connection(self):
		return mysql.connection

	def cursor(self):
		return self.connection().cursor()

	def db_Connection(self):
		return Products(self.connection(),self.cursor())

	@route("/",methods =["GET"])
	def index(self):
		try:
			return jsonify(self.db_Connection().)


	@route("/config")
	def get_publishable_key(self):
		stripe_config =