#Create a dictionary to hold expense information and functions to recall specific info.

from datetime import date

#Create a  class to define accounts
class account(object):
	def __init__(self):
		self.account_num = raw_input("What is your account number?")
		self.amount = raw_input("How much did it cost?")
		self.details = raw_input("Why did you spend my money?")
		self.date = raw_input("What is the date?")
	
#Define a function to make a journal entry
def make_entry():
	entry = account()
	print "So you spent %s for %s on %s and you want to put it into account %s?" % (entry.amount, entry.details, entry.date, entry.account_num)
	mk_str = ("%s, %s, %s, %s") % (entry.account_num, entry.amount, entry.details, entry.date) 
	with open("acc.csv", "w") as transfer:
		transfer.write(mk_str)
		

print "Welcome to Nathan's super awesome accounting program!"
choice = raw_input("What would you like to do? \nE - Make entry \nV - View account \nX - Exit\n: ") 
if choice.upper() == "E":
	make_entry()
	
else:
	print "goodbye"