### create a program for a parking garage

class ParkingGarage():
    
    def __init__(self, tickets=10, spaces=10, cur_tic = {'paid':False}):
        self.tickets = tickets
        self.spaces = spaces
        self.cur_tic = cur_tic

# TAKE TICKET
#   reduce tickets and spaces by 1

    def setTicket(self, tickets):
        self.tickets = tickets

    def setSpace(self, spaces):
        self.spaces = spaces

    def decNum(self, dec_num = 1):
        self.tickets -= dec_num
        self.spaces -= dec_num
        
        print('\nTicket allocated.\n\tAs a reminder, you will be charged $10 for every hour that your car is parked.\n\t(this means that this parking lot is being paid more per hour than every minimum wage employee in the country)\n\nThank you for choosing our garage!')
        
        print(garage.tickets)   # proof of concept
        print(garage.spaces)    # proof of concept

# PAY FOR PARKING
#   display input and wait for amount
#   if ticket paid - print 'paid message'
#   update cur_tic dict 'paid' to TRUE

    def payParking(self):
        hours = input('\nThe cost of your ticket is $10 for every hour in the garage.\nPlease input the amount of hours you are paying for.\n\ninput:  ')        
        
        if type(hours) == int:
            pass
        else:
            print('\nPlease input a valid option.')
        
        amount_owed = int(hours) * 10    
        
        payment = input('\nYou owe $' + str(amount_owed) + ' to the parking garage for ' + hours + ' hour(s) of parking.\nPlease input "paid" when you have paid for your ticket.\n(if this is incorrect, please input "return" to go back.)\n\ninput:  ')

        if payment.lower() == 'return':
            if garage.cur_tic['paid'] == False:
                print('\nPlease pay for your ticket before leaving.')
            else:
                print('\nWe hope to serve you again soon.')
                run()
        elif payment.lower() == 'paid':
            garage.cur_tic['paid'] = True
            print('\nThank you for your payment! Have a safe trip!\n(in order to get the gate to open, don\'t forget to "Leave" the parking garage through our terminal)')
        else:
            print('\nPlease select a valid option.')



# LEAVE GARAGE
#   if paid - thank you
#   if not - prompt for payment
#   increase tickets and spaces by 1

    def setTicket(self, tickets):
        self.tickets = tickets

    def setSpace(self, spaces):
        self.spaces = spaces

    def incNum(self, inc_num = 1):
        self.tickets += inc_num
        self.spaces += inc_num

    def leaveGarage(self):
        if garage.cur_tic['paid'] == True:
            print('\nPlease allow the armbar to raise fully before exiting the garage.\nUpon exiting the garage, traffic moves one way to the right.\n\n\tHave a safe trip!')
            garage.incNum()
            
            print(garage.tickets)   # proof of concept
            print(garage.spaces)    # proof of concept
        else:
            print('\nPlease pay for your ticket before leaving the garage.')
            ParkingGarage()

# RUN PROGRAM

garage = ParkingGarage()

def run():
    while True:
        option = input('\nWhat do you want to do?\nOptions:\n\tN: Number of available tickets and spaces\n\tT: Take ticket and space\n\tP: Pay for parking\n\tL: Leave garage\n\tQ: Quit terminal\n\ninput:  ')

        if option.lower() == 'q':
            print('\nThank you for stopping by')
            break
        elif option.lower() == 'n':
            print('\nThere are ' + str(garage.spaces) + ' tickets/spaces available.')
        elif option.lower() == 't':
            garage.decNum() 
        elif option.lower() == 'p':
            garage.payParking()
        elif option.lower() == 'l':
            if garage.cur_tic['paid'] == True:
                garage.leaveGarage()
                break
            else:
                print('\nYou have either not taken or not paid for your ticket yet.\nPlease make the appropriate selection as needed.')
        else:
            print('\nPlease select a valid option.')

run()