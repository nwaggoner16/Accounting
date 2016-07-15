# Create a dictionary to hold expense information and functions to recall specific info.

from datetime import date
import csv


# Create a  class to define accounts
class account(object):
    def __init__(self, account_num, debit_am, credit_am, details, date):
        self.account_num = account_num
        self.debit_am = debit_am
        self.credit_am = credit_am
        self.details = details
        self.date = date


# Define a function to make a journal entry
def make_entry():
    account_num = raw_input("What is your account number? ")
    amount = raw_input("How much did it cost? ")
    details = raw_input("Why did you spend my money? ")
    date = raw_input("What is the date? ")
    entry = account(account_num, amount, details, date)

    print "So you spent %s for %s on %s and you want to put it into account %s?" % (
    entry.amount, entry.details, entry.date, entry.account_num)
    mk_lst = (entry.account_num, entry.amount, entry.details, entry.date)

    # Append entry to acc.csv file
    with open(r'%s.csv' % entry.account_num, 'a') as t:
        transfer = csv.writer(t)
        transfer.writerow(mk_lst)

#Define double entry function
def double_entry():
    print "Remember debits and credits must be equal!"
    account_num = raw_input("Account: ")
    debit_am = raw_input("Debit amount: ")
    credit_am = raw_input("Credit amount: ")
    details = raw_input("Why did you spend my money? ")
    date = raw_input("What is the date? ")
    entry = account(account_num, debit_am, credit_am, details, date)

    mk_lst = (entry.account_num, entry.debit_am, entry.credit_am, entry.details, entry.date)

    # Append entry to acc.csv file
    with open(r'%s.csv' % (entry.account_num), 'a+') as t:
        transfer = csv.writer(t)
        transfer.writerow(mk_lst)

    if debit_am == credit_am:
        intro()

# Define a function to view a sum of accounts
def view_account_total():
	acn = raw_input("What account would you like to view?")
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
