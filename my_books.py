#Create a dictionary to hold expense information and functions to recall specific info.

from datetime import date
import csv

#Create a  class to define accounts
class account(object):
	def __init__(self, account_num, amount, details, date):
		self.account_num = account_num
		self.amount = amount
		self.details = details
		self.date = date
	
#Define a function to make a journal entry
def make_entry():
	account_num = raw_input("What is your account number? ")
	amount = raw_input("How much did it cost? ")
	details = raw_input("Why did you spend my money? ")
	date = raw_input("What is the date? ")
	entry = account(account_num, amount, details, date)
	
	print "So you spent %s for %s on %s and you want to put it into account %s?" % (entry.amount, entry.details, entry.date, entry.account_num)
	mk_lst = (entry.account_num, entry.amount, entry.details, entry.date)
	
	#Append entry to acc.csv file
	with open(r'%s.csv' % (entry.account_num), 'a') as t:
		transfer = csv.writer(t)
		transfer.writerow(mk_lst)
		
#Define a function to view accounts
def view_account():
	with open('acc.csv', 'r') as a:
		for item in a:
			if "100" in item:
				print item
		
#Intro and initiate program
print "Welcome to Nathan's super awesome accounting program!"
choice = raw_input("What would you like to do? \nE - Make entry \nV - View account \nX - Exit\n: ") 
if choice.upper() == "E":
	make_entry()
	
elif choice.upper() == "V":
	view_account()
else:
	print "goodbye"
