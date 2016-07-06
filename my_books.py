#Create a dictionary to hold expense information and functions to recall specific info.

from datetime import date

#Create a  class to define accounts
class account(object):
	def __init__(self):
		self.account = raw_input("What is your account number?")
		self.amount = raw_input("How much did it cost?")
		self.details = raw_input("Why did you spend my money?")
		self.date = raw_input("What is the date?")
	
	def print_entry(self):
		print self.account
		
entry = account()
print "So you spent %s for %s on %s and you want to put it into account %s?" % (entry.amount, entry.details, entry.date, entry.account)
