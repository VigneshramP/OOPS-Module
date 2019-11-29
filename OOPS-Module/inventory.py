priceList = []
delivaryBill = []

class Product:
	def __init__(self,name,code,cost,date):
		self.productName = name
		self.productCode = code
		self.productCost = cost
		self.mfgDate = date

	def appendProductDetails(self):
		priceList.append(
						[
							self.productCode,
							{
								'Product Name' : self.productName,
								'Product Cost' : self.productCost,
								'MFG Date' : self.mfgDate
							}
						]
						)

class Invoice:
	def __init__(self,billNo,billName,address):
		self.billNo = billNo
		self.buyerName = billName
		self.buyerAddress = address

	def totalCost(self,totalCost):
		self.totalCost = totalCost
		totalAmount = 0 
		for cost in range (0,1):
		 	totalAmount = totalAmount + self.totalCost
		delivaryBill.append(
							[
								str(self.billNo),
								{
									'Customer Name' : self.buyerName,
									'Customer Contact Details' : self.buyerAddress,
									'Total Buying Amount -"Rs"' :  totalAmount
								} 
							]
							)

def dictConversion():
	productList = dict(priceList)
	return productList

def generateDelivaryBill():
	delivaryInvoice = dict(delivaryBill)
	print delivaryInvoice
	invoiceNo = str(input("Enter Invoice Number\n"))
	print delivaryInvoice.get(invoiceNo)	

def createDelivaryBill():
	billNo = int(input("Enter Bill Number\n"))
	billName = raw_input("Enter Buyer Name\n")
	buyerAddress = raw_input("Enter Buyer Address\n")
	totalQuantity = int(input("How Many Products Buy by Customer\n"))
	totalAmount = 0
	newInvoice = Invoice(billNo,billName,buyerAddress)
	for item in range(0,totalQuantity):
		productList = dictConversion()
		itemCode = str (input("Enter Product Code"))
		productDetails = productList.get(itemCode)
	 	cost = int(productDetails.get("Product Cost"))
	 	quantity = int (input("Howmany Quantity buy this Product?\n"))
	 	totalAmount = totalAmount + ( cost * quantity ) 
	newInvoice.totalCost(totalAmount)
		
def getProductDetails():
		products = dictConversion()
		return products

def createProductDetails():
	productName = raw_input("Enter Product Name\n")
	productCode = raw_input("Enter Product Idem Code\n")
	productCost = raw_input("Enter Product Cost\n")
	mfgDate = raw_input("Enter Manufacturing Date (01/01/2019)\n")
	newProduct = Product(productName,productCode,productCost,mfgDate)
	newProduct.appendProductDetails() 

def isPriceListEmpty():
	if len(priceList) == 0:
		return 1
	else:
		return 0	

def getOption():
	option = int(input("1. Create Product Details\n2. Get Product Details\n3. Create Delivary Bill Details\n4. Generate Delivary Bill\n5. Exit\n"))
	return option

def main():
	while True:
		print "<========== INVENTORY MANAGEMENT =========>\n\nEnter Your Option\n"
		option = getOption()
		if option == 1:
			createProductDetails()

		elif option == 2:
			check = isPriceListEmpty()
			if check == 1:
				print "Enter Product Details First\n"
				createProductDetails()
			else:
				products = getProductDetails()
				print products
		
		elif option == 3:
			check = isPriceListEmpty()
			if check == 1:
				print "Enter Product Details First\n"
				createProductDetails()
			else:
				createDelivaryBill()
		
		elif option == 4:
			generateDelivaryBill()
		
		elif option ==5:
			print "Thanks for Shopping"
			exit()			
	
if __name__ == '__main__':
	main()