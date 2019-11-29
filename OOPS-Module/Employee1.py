allEmployee =[]
empPersonal = []
projectList = []

class Employee:
	def __init__(self,name,employeeId,salary,jobRole):
		self.name = name
		self.empId = employeeId
		self.empSalary = salary       # emp refers Employee
		self.jobRole = jobRole
	
	def appendEmpDetails(self):
		allEmployee.append(
							[
								self.empId,
							{
								'Emplyee Name' : self.name,
								'Employee Salary' : self.empSalary,
								'Job Description' : self.jobRole
							}
							]
							)
		print "=====================================\n"
		print "Employee Details Created Successfully\n"


class EmpPersonalDetails:
	def __init__(self,eId,qualification,bloodGroup,address):
		self.eId = eId                        #eId refers Employee Id
		self.qualification = qualification
		self.bloodGroup = bloodGroup
		self.address = address

	def appendEmpPersonalDetails(self):
		print "You are Enter {} Personal Details\n".format(self.eId)
		empPersonal.append(
							[
								self.eId,
								{
									'Qualification' : self.qualification,
									'Blood Group' : self.bloodGroup,
									'Contact Address' : self.address
								}
							]
						 )		
		print "==================================================\n"
		print "\n{} Employee Personal Details Added Successfully\n".format(self.eId)
	
	
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
		print "<========== EMPLOYEE DETAILS ==========>\n",dict(allEmployee)
	elif choice == 2:
		print "<========== EMPLOYEE PERSONAL DETAILS ==========>\n",dict(empPersonal)
	elif choice == 3:
		print "<========== EMPLOYEE PROJECT DETAILS ==========>\n",dict(projectList)		 

def createEmployeeProjects():
	empId = getDictionaryConversion()
	for eId in empId:
		print "You are Enter {} Project Details\n".format(eId)
		projectList.append(
							[
								eId,
								raw_input("Enter Employee Project Details\n")
							]
							) 			

def createEmpPersonalDetails():
	empId = getDictionaryConversion()
	for eId in empId:
		print "You are Enter {} Personal Details\n".format(eId)
		qualification = raw_input("Enter Employee Qualification\n")
		bloodGroup = raw_input("Enter Employee Blood Group\n")
		contactAddress = raw_input("Enter Employee Contact Details\n")
		newEmpPersonal = EmpPersonalDetails(eId,qualification,bloodGroup,contactAddress)
		newEmpPersonal.appendEmpPersonalDetails()					

def createEmployeeDetails():
		name = raw_input("Enter Employee Name\n")
		empId = raw_input("Enter Employee Id No\n")
		salary = raw_input("Enter Employee Salary\n")
		jobRole = raw_input("Enter Employee Job Description\n")
		newEmployee = Employee(name,empId,salary,jobRole)
		newEmployee.appendEmpDetails()
		
def getOption():
	option = int (input("\nEnter Your Option\n1. Create Employee Details\n2. Create Employee Personal Details\n3. Get Project Details\n4. Print Employee Details\n5. Exit\n"))	
	return option
def main():
	print "<========== Employee Module ==========>\n"
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