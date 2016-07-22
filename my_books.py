# Create a dictionary to hold expense information and functions to recall specific info.

from datetime import date
import csv



# Create a  class to define accounts
class account(object):
    def __init__(self, account_num, debit_am, credit_am, details, en_date, datestamp):
        self.account_num = account_num
        self.debit_am = debit_am
        self.credit_am = credit_am
        self.details = details
        self.en_date = en_date
        self.datestamp = datestamp


# Define a function to make a journal entry
def make_entry():
    account_num = raw_input("What is your account number? ")
    amount = raw_input("How much did it cost? ")
    details = raw_input("Why did you spend my money? ")
    en_date = raw_input("What is the date? ")
    entry = account(account_num, amount, details, en_date)

    print "So you spent %s for %s on %s and you want to put it into account %s?" % (entry.amount, entry.details, entry.en_date, entry.account_num)
    mk_lst = (entry.account_num, entry.amount, entry.details, entry.en_date)

    # Append entry to acc.csv file
    with open(r'%s.csv' % entry.account_num, 'a') as t:
        transfer = csv.writer(t)
        transfer.writerow(mk_lst)

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
    	print "Please use a real account."
    	deb_acc = raw_input("Debit Account: ") 
    
    debit_am = raw_input("Debit amount: ")
    cred_acc = raw_input("Credit Account: ")
    #Making sure appropriate account number is used
    while cred_acc not in accounts:
    	print "Please use a real account."
    	cred_acc = raw_input("Debit Account: ") 
    credit_am = raw_input("Credit amount: ")
    #Checking to make sure debits and credits are equal
    if debit_am != credit_am:
    	print "I told you Debits must equal credits!"
    	double_entry()
    else:
    	details = raw_input("Description: ")
    	en_date = raw_input("Entry date: ")
    	datestamp = date.today()
    	
    	print "Debit Account: %s\nAmount: %s\nCredit Account: %s\nAmount: %s\nDetails: %s\nEntry Date: %s" % (deb_acc, debit_am, cred_acc, credit_am, details, en_date)
    	correct = raw_input("Finalize entry? y/n")
    	if correct.upper() == 'Y':
    	
    	
    		#Creating class objects for debit and credit accounts
    		entry = account(deb_acc, debit_am, 0, details, en_date, datestamp)
    		ent_2 = account(cred_acc, 0, credit_am, details, en_date, datestamp)
    		#Create lists to hold the desired variables from account objects
    		mk_lst = (entry.account_num, entry.debit_am, entry.credit_am, entry.details, entry.en_date, entry.datestamp)
    		mk_lst2 = (ent_2.account_num, ent_2.debit_am, ent_2.credit_am, ent_2.details, ent_2.en_date, ent_2.datestamp)
    
    		with open('acc.csv', 'r') as accsv:
    			acclist = csv.reader(accsv, delimiter = ',')
	
			
				# Append entry to acc.csv file
			with open(r'%s.csv' % (entry.account_num), 'a+') as t:
				transfer = csv.writer(t)
				transfer.writerow(mk_lst)
			with open(r'%s.csv' % (ent_2.account_num), 'a+') as x:
				transfer = csv.writer(x)
				transfer.writerow(mk_lst2)


# Define a function to view a sum of accounts
def view_account_total():
	acn = raw_input("What account would you like to view: ")
	with open('%s.csv' % acn , 'r') as a:
		col = csv.reader(a)
		debit= ()
		deb = 0
		for row in col:
			debit = row[1]
			deb += int(debit)
	
	with open('%s.csv' % acn , 'r') as a:
		col = csv.reader(a)	
		credit = ()
		cre = 0
		for row in col:
			credit = row[2]
			cre += int(credit)
			
		print "Total Debits: %s \nTotal Credits: %s" % (deb, cre)
				
			
				
			
		
# Intro and initiate program
def intro():
    print "Welcome to Nathan's super awesome accounting program!"
    choice = raw_input("What would you like to do? \nE - Make entry \nV - View account totals \nX - Exit\n: ")
    if choice.upper() == "E":
        double_entry()

    elif choice.upper() == "V":
        view_account_total()
    else:
        print "goodbye"


intro()
