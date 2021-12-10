import os
from flask import Flask, request,jsonify,redirect,render_template
from flask_cors import CORS
from flask_classful import FlaskView,route
from flask_mysqldb import MySQL
from Details import Products
import stripe 
from dotenv import load_dotenv
import webbrowser

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='flask'

mysql = MySQL(app)


CORS(app)
message ={"Content":""}
class GateWay(FlaskView):

	def connection(self):
		return mysql.connection

	def cursor(self):
		return self.connection().cursor()

	def db_Connection(self):
		return Products(self.connection(),self.cursor())

	@route("/getProducts",methods =["GET"])#passing products details to angular frontend
	def getProducts(self):
		return jsonify(self.db_Connection().getProducts())

	@route("/orderProduct",methods =["GET","POST"])
	def orderProduct(self): #extracting purchasing request fron angular and making purchase order with stripe
		if request.method=="POST":
			data = request.get_json()
			product = self.db_Connection().extractProduct(data)

			if data!= product["Name"]:
				abort(400)

			#creating stripe checkout session
			checkout_session = stripe.checkout.Session.create(
				line_items=[{
				'price_data':{
			    'product_data':{
			     'name':product["Name"],
			},
			'unit_amount':int(product["Price"]),
			'currency':'usd'
				},
				'quantity':1,},],
			    payment_method_types =["card"],
			    mode ="payment",
			    success_url = request.host_url + 'order/success',
			    cancel_url = request.host_url + 'order/cancel'
			)
			return webbrowser.open_new_tab(checkout_session.url)
	@route('/order/cancel')
	def cancel(self):#page rendered if payment is not successful
		return jsonify({"Message":"cancel"})


	@route('/order/success')
	def success(self):#page rendered if payment is successful
		return jsonify({"Message":"success"})

GateWay.register(app,route_base ="/")
if __name__=="__main__":
	app.run(debug=True)



