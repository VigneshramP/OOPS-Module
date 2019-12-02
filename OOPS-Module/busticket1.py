passengerDetails = []
ticketDetails = []
class Ticket:
    counter=0 
    def __init__(self,source,destination,passengerList,busDetails):
        self.source = source
        self.destination = destination
        self.passengerDetails = passengerList
        self.busDetails = busDetails
        self.Counter=Ticket.counter
        Ticket.counter+=1

    def generateTicket(self ):
        ticketId=self.source[0]+self.destination[0]+"0"+str(self.Counter)
        print "<======== Ticket ID =======>\n"
        ticketDetails.append([
            					ticketId,
            					{
            						'Passenger Details' : self.passengerDetails,
            						'Starting Point' : self.source,
            						'Destination' : self.destination,
            						'Bus Operator' : self.busDetails

            					}
            					])
    	print ticketDetails
    	
def printTicket():
	tickets = dict(ticketDetails)
	ticketId = raw_input("Enter Ticket Id\n")
	print tickets.get(ticketId)
        
def getOption():
	choice = int (input("Which you are Selacted\n1. SRM Transport\n2. SRS Travels\n3. PARVEEN Travels\n"))
	return choice

def getBusDetails(source,destination,seats):
	option = getOption()
	if option == 1:
		return "SRM Transport"

	elif option == 2:
		return "SRS Travels"

	elif option == 3:
		return"PARVEEN Travels"	

def getPassengerDetails(seats):
	for i in range(0,seats):
		passengerName = raw_input("Enter Passenger Name\n")
		passengerDetails.append([
								passengerName,
											{		
												'age' : int (input ("Enter Passenger Age\n")),
												'sex' : raw_input("Male / Female\n")
											}]
	)	
	return dict(passengerDetails)

def bookTicket():
	startingPoint = raw_input("Enter Your Starting Location\n")	
	destination = raw_input("Enter Your Destination\n")
	requriedSeat = int(input("Howmany Seats Your are Required?\n"))
	busDetails = getBusDetails(startingPoint,destination,requriedSeat)
	passengerList = getPassengerDetails(requriedSeat)
	newTicket = Ticket(startingPoint,destination,passengerList,busDetails)
	newTicket.generateTicket()

def isTicketListEmpty():
	if len(ticketDetails) == 0:
		return True
	else:
		return False			

def getChoice():
	option = int (input("Enter your Option\n1. Ticket Booking\n2. Print Ticket\n3. Exit\n"))
	return option

        
def main():
	while True:
		print "<======= Ticket Reservation System =======>\n"
		choice = getChoice()
		if choice == 1:
			print "<====== WELCOME =====>\n"
			bookTicket()			
			
		elif choice == 2:
			check = isTicketListEmpty()
			if check == True:
				print "Please Book a Ticket First\n"
				bookTicket()
			else:
				printTicket()

		elif choice == 3:
			print"Happy Journey"
			exit()		

					


if __name__ == '__main__':
	main()
