allEmployee = []
class Employee:
	def __init__(self,empName,empId):
		self.name = empName
		self.empId = empId

	def getEmployeeName(self):
		return self.name

	def getEmployeeId(self):
		return self.empId

def checkInput(empId):
	if len(empId) == empId.isdigit():
		return True
	else:
		return False

def isListEmpty():
	if len(allEmployee) == 0:
		return True
	else:
		return False	

def checkEmpList():
	if isListEmpty() == True:
		print "\nEnter Employee Details First\n"
		return 0
	else:
		return 1
def getEarningSalary(basicPay):
	hra = basicPay * 0.50
	travelAllowance = 0.223 * basicPay
	medicalAllowance = 0.18 * basicPay
	specialAllowance = 0.50 * basicPay
	print "\n<----- Earnings Details ----->\n1. Basic Pay = {}\n2. HRA = {}\n3. Travel Allowance = {}\n4. Medical Allowance = {}\n5. Special Allowance = {}\n".format(basicPay,hra,travelAllowance,medicalAllowance,specialAllowance)
	return (basicPay + hra + travelAllowance + medicalAllowance + specialAllowance + 1000)

def getDeductionAmount(totalEarning):
	annualIncome = totalEarning * 12
	epfo = 0.12 * totalEarning
	esi = 125
	if annualIncome > 350000 :
		incomeTax = ((annualIncome - 300000) * 0.33 )/12
		print "\n<----- Deduction Details ----->\nEPFO = {}\nESI = {}\nIncome Tax = {}\n".format(epfo,esi,incomeTax)
		return (epfo + esi + incomeTax )
	else:
		print "\n<----- Deduction Details ----->\nEPFO = {}\nESI = {}\n".format(epfo,esi)
		return (epfo + esi )

def generatePayDetails():
	basicPay = int (input("Enter Basic Pay of Employee: "))
	totalEarning = getEarningSalary(basicPay)
	totalDeduction = getDeductionAmount(totalEarning)
	finalSalary = totalEarning - totalDeduction
	#print allEmployee
	print "\n<----- Total Earining ---->\n",totalEarning
	print "\n<----- Total Deduction ---->\n",totalDeduction 
	print "\n<-----  Net Pay -----> \n",finalSalary

def createEmployeeDetails():
	global allEmployee
	name = raw_input("Enter Employee Name:")
	empId = raw_input("Enter Empolyee Id No:")
	if checkInput(empId) == False:
		newEmployee = Employee(name,empId)
		allEmployee.append(newEmployee)
		print "\n<----- Employee Details ----->\n"
		print "\n{} and {} Added Sucessfully".format(newEmployee.getEmployeeName(),newEmployee.getEmployeeId())
	else:
		print "Enter Employee Details"
		createEmployeeDetails()

def getOption():
	try:
		option = int (input("\nEnter Your Option\n1. Create Employee Details\n2. Generate Pay Slip\n3. Exit \n"))
		return option
	except NameError as err:
		print "Enter Correct Option\n",err


def main():
	print "\n<----- PAY ROLL ----->\n"
	while True:
		option = getOption()	
		if option == 1:
			createEmployeeDetails()
		elif option == 2:
			paySlip = checkEmpList()
			if paySlip == 0:
				createEmployeeDetails()
			else:
				generatePayDetails()
		elif option == 3:
			print "BYE\nGOOD LUCK"
			exit()

if __name__ == '__main__':
	main()