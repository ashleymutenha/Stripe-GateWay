class Products:
	def __init__(self,con,cur):
		self.con =con
		self.cur =cur
		self.products ={"Name":"","Description":"","Price":0}
		self.final =[]

	def getProducts(self):#fetching products from db
		elements =[]
		counter =0
		self.cur.execute("SELECT * FROM products")
		for i in self.cur:
			for e in i:
				elements.append(e)

		_products = [elements[n:n+len(self.products)] 
		for n in range(0, len(elements), len(self.products))]

		self.products.update(zip(self.products,_products[0]))# retrieving first product

		#if there are other products in db
		if len(_products)>1:
			remainingProducts = _products[1:]
			while counter!=len(remainingProducts):
				dict =self.products.copy()
				dict.update(zip(dict,["","",0]))#initialising new dict
				dict.update(zip(dict,remainingProducts[counter]))
				self.final.append(dict)
				counter+=1
		self.final.insert(0,self.products)
		return self.final

	def extractProduct(self,name):#extract a single product's details 
		for i in self.getProducts():
			if i["Name"]==name:
				return i
		
	def addProduct(self,name,price):#function to add products to db
		self.cur.execute("INSERT INTO products VALUES(%s,%d)",(name,[price],))
		self.con.commit()

	def deleteProduct(self,name):#deleting product from db
		self.cur.execute("DELETE FROM products where Name=%s",(name,))
		self.con.commit()
