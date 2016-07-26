# Create a dictionary to hold expense information and functions to recall specific info.

from datetime import date
import csv
import period
import report


# Create a  class to define accounts
class account(object):
    def __init__(self, account_num, debit_am, credit_am, details, en_date, datestamp):
        self.account_num = account_num
        self.debit_am = debit_am
        self.credit_am = credit_am
        self.details = details
        self.en_date = en_date
        self.datestamp = datestamp



#Define double entry function
def double_entry():
    print "Remember debits and credits must be equal!"
    accounts = []
    with open('acc.csv', 'r') as accsv:
    	acclist = csv.reader(accsv, delimiter = ',')
    	for row in acclist:
			for field in row:
				accounts.append(field)
    
    deb_acc = raw_input("Debit Account: ")
    #Making sure appropriate account number is used
    while deb_acc not in accounts:
    	#Pro tip: print accounts for super user friend experience.
    	print "Please use a real account."
    	deb_acc = raw_input("Debit Account: ") 
    
    debit_am = raw_input("Debit amount: ")
    
    #What is the difference between debit and credit account?
    
    cred_acc = raw_input("Credit Account: ")    
    #Making sure appropriate account number is used
    while cred_acc not in accounts:
    	print "Please use a real account."
    	cred_acc = raw_input("Crebit Account: ") 
    credit_am = raw_input("Credit amount: ")
    
    #Checking to make sure debits and credits are equal
    if debit_am != credit_am:
    	print "I told you Debits must equal credits!"
    	#How about, printing the accounts you just inputed and then trying again
    	#at the debit and credit amounts.
    	double_entry()
    else:
    	details = raw_input("Description: ")#Describes what the entry is for, what the user just bought, ect.
    	en_date = raw_input("Entry date: ")
    	datestamp = date.today()
    	
    	print "Debit Account: %s\nAmount: %s\nCredit Account: %s\nAmount: %s\nDetails: %s\nEntry Date: %s" % (deb_acc, debit_am, cred_acc, credit_am, details, en_date)
    	correct = raw_input("Finalize entry? y/n \n")
    	if correct.upper() == 'Y':	
    	
    		#Creating class objects for debit and credit accounts
    		debit_entry = account(deb_acc, debit_am, 0, details, en_date, datestamp)
    		credit_entry = account(cred_acc, 0, credit_am, details, en_date, datestamp)
    		#Create lists to hold the desired variables from account objects
    		#Silly python needs to write to the csv using a list and I don't know how to convert a class instance to a list of properties.
    		debit_list = (debit_entry.account_num, debit_entry.debit_am, debit_entry.credit_am, debit_entry.details, debit_entry.en_date, debit_entry.datestamp)
    		credit_list = (credit_entry.account_num, credit_entry.debit_am, credit_entry.credit_am, credit_entry.details, credit_entry.en_date, credit_entry.datestamp)
    
    		with open('acc.csv', 'r') as accsv:
    			acclist = csv.reader(accsv, delimiter = ',')
	
				# Append entry to acc.csv file
			with open(r'%s.csv' % (debit_entry.account_num), 'a+') as t:
				transfer = csv.writer(t)
				transfer.writerow(debit_list)
			with open(r'%s.csv' % (credit_entry.account_num), 'a+') as x:
				transfer = csv.writer(x)
				transfer.writerow(credit_list)


# Define a function to view a sum of accounts
def view_account_total():
	acn = raw_input("What account would you like to view: ")
	with open('%s.csv' % acn , 'r') as a:
		debit_file = csv.reader(a)
		debit = ()
		deb = 0
		for row in debit_file:
			#row is an array. Position 1 is the debit amount.
			debit = row[1]
			deb += int(debit)
	
	with open('%s.csv' % acn , 'r') as a:
		credit_file = csv.reader(a)	
		credit = ()
		cre = 0
		for row in credit_file: 
			#Position 2 is the credit amount.
			credit = row[2]
			cre += int(credit)
			
		print "Total Debit Amount: %s \nTotal Credit Amount: %s" % (deb, cre)



def check_period():
	x = raw_input("Period: ")
	period_check = period.date_check(x)
	print period_check
	intro()		
			
def period_total():
	x = raw_input("Period: ")
	y = raw_input("Account: ")
	report.view_period_total(x,y)
	
				
			
		
# Intro and initiate program
def intro():
    print "Welcome to Nathan's super awesome accounting program!"
    choice = raw_input("What would you like to do? \nE - Make entry \nV - View account totals \nX - Exit\n: ")
    if choice.upper() == "E":
        double_entry()

    elif choice.upper() == "V":
        view_account_total()
    elif choice.upper() == "C":
    	check_period()
    elif choice.upper() == "P":
    	period_total()
    else:
        print "goodbye"


intro()
