allEmployee =[]
empPersonal = []
projectList = []

class Employee:
	def __init__(self,name,employeeId,salary,jobRole):
		self.name = name
		self.empId = employeeId
		self.empSalary = salary
		self.jobRole = jobRole
	
	def getEmpId(self):
		return self.empId
	
	def getEmpName(self):
		return self.name

	def getSalary(self):
		return self.empSalary	

	def getJobRole(self):
		return self.jobRole			

class EmpPersonalDetails:
	def __init__(self,qualification,bloodGroup,address):
		self.qualification = qualification
		self.bloodGroup = bloodGroup
		self.address = address
			
	def getEmpQualifiaction(self):
		return self.qualification

	def getEmpBloodGroup(self):
		return self.bloodGroup

	def getEmpAddress(self):
		return self.address
	
def getDictionaryConversion():
	empDictConvertion = dict(allEmployee)
	return empDictConvertion.keys()

def checkEmpList():
	if len(allEmployee) == 0:
		return True
	else:
		return False

def printEmployeeDetails():
	print "1. Employee Details\n2. Employee Personal Details\n3. Employee Project Details\n"
	choice = int (input("Enter Your Required Print Details\n"))
	if choice == 1:
		print "<----- EMPLOYEE DETAILS ----->\n",dict(allEmployee)
	elif choice == 2:
		print "<----- EMPLOYEE PERSONAL DETAILS ----->\n",dict(empPersonal)
	elif choice == 3:
		print "<----- EMPLOYEE PROJECT DETAILS ----->\n",dict(projectList)		 
def createEmployeeProjects():
	empId = getDictionaryConversion()
	for eId in empId:
		print "You are Enter {} Project Details\n".format(eId),eId
		projectList.append(
							[
								eId,
								raw_input("Enter Employee Project Details\n")
							]
							) 			

def createEmpPersonalDetails():
	empId = getDictionaryConversion()
	for eId in empId:
		print "You are Enter {} Personal Details\n".format(eId),eId
		qualification = raw_input("Enter Employee Qualification\n")
		bloodGroup = raw_input("Enter Employee Blood Group\n")
		contactAddress = raw_input("Enter Employee Contact Details\n")
		newEmpPersonal = EmpPersonalDetails(qualification,bloodGroup,contactAddress)
		empPersonal.append(
							[
								eId,
								{
									'Qualification' : newEmpPersonal.getEmpQualifiaction(),
									'Blood Group' : newEmpPersonal.getEmpBloodGroup(),
									'Contact Address' : newEmpPersonal.getEmpAddress()
								}
							]
							)				

def createEmployeeDetails():
	try:
		name = raw_input("Enter Employee Name\n")
		empId = raw_input("Enter Employee Id No\n")
		salary = raw_input("Enter Employee Salary\n")
		jobRole = raw_input("Enter Employee Job Description\n")
		newEmployee = Employee(name,empId,salary,jobRole)
		allEmployee.append(
							[
								newEmployee.getEmpId(),
							{
								'Emplyee Name' : newEmployee.getEmpName(),
								'Employee Salary' : newEmployee.getSalary(),
								'Job Description' : newEmployee.getJobRole()
							}
							]
							)
	except ValueError as err:
		print "Enter Correct Employee Details",err	

def getOption():
	option = int (input("Enter Your Option\n1. Create Employee Details\n2. Create Employee Personal Details\n3. Get Project Details\n4. Print Employee Details\n5. Exit\n"))	
	return option
def main():
	print "<----- Employee Module ----->\n"
	while True :
		option = getOption()
		if option == 1:
			createEmployeeDetails()
		
		elif option == 2:
			empList = checkEmpList()
			if empList == True:
				print "Enter Employee Details First\n"
				createEmployeeDetails()
			else:
				createEmpPersonalDetails()
		
		elif option == 3:
			empList = checkEmpList()
			if empList == True:
				print "Enter Employee Details First\n"
				createEmployeeDetails()
			else:
				createEmployeeProjects()
		
		elif option == 4:
			empList = checkEmpList()
			if empList == True:
				print "Enter Employee""(Pesonal,Project)"" Details First\n"
				createEmployeeDetails()
			else:
				printEmployeeDetails()	
					
		elif option == 5:
			print "BYE\nGOOD LUCK FOR YOUR FUTURE "
			exit()		
						
if __name__ == '__main__':
	main()