import json

class School :
	def getStudentDetails(self):
		students = []
		print "Enter Student Details "
		try :
			numberofStudent=int(input("Enter the Total Number of Student :"))
		except NameError as err:
			print "Enter Integers Value of Student Count \n",err
			exit()
		for i in range (0,numberofStudent):
			regNumber = raw_input("Enter the Student RollNumber :")
			students.append(
				[
					 regNumber,
					{
				 		'Student Name': raw_input ("Enter the Student Name :"),
						'Class - Section' : raw_input("Enter Student Studying Class and Section :")
					}
				]
							)
		print "<----- STUDENT DETAILS ----->"
		return json.dumps(dict(students))
		
	def getStaffDetails (self):
		print " Enter Teaching Staff Details "
		staffCount = int (input("Total Number of Teaching Staff Count :"))
		teachingStaff = []
		for i in range(0,staffCount):
			idNo = raw_input("Enter Staff Identify Number :")
			teachingStaff.append(
				[
					idNo,
					{
						'Staff Name' : raw_input ("Enter the Staff Name :"),
						'Handling Subject': raw_input("Enter the Staff Handling Subject : ")
					}
				]
								)
		print "<----- STAFF DETAILS ----->"
		return dict(teachingStaff)

	def getAdminStaffDetails(self):
		print " Enter Non Teaching Staff Details "
		adminStaffCount = int(input("Total Number of Non - Teaching Staff Count :"))
		adminStaff = []
		for i in range(0,adminStaffCount):
			idNo = raw_input("Enter Staff Identify Number :")
			adminStaff.append(
				[ 
					idNo, 
					{
						'Admin Staff Name' : raw_input ("Enter the Staff Name :"),
						'Job Description' : raw_input("Enter the Staff Job Description: ")
					}
				]
							)
		print "<----- ADMIN STAFF DETAILS ----->"	
		return dict(adminStaff)	

def main():
	school=School()
	print "Enter your Choice : \n1.Student Details\n2.Teaching Staff Details\n3.Non Teaching Staff Details"
	try:
		choice = int(input("Enter Your Choice(1/2/3) : "))
	except NameError as err:
		print "Enter Correct Choice\n",err
		exit()
	if choice == 1:
		student = school.getStudentDetails()
		print type(student),"\n",student
		
	elif choice == 2:
		print school.getStaffDetails()
	elif choice == 3:
		 print school.getAdminStaffDetails()
	else:
		print "Select Correct Choice"
		exit()	

if __name__ == '__main__':
	main()	