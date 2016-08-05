import csv
import datetime

def view_period_total(x,y):
	#Create variables containing the opening and clos
	per_open = datetime.date(2016, int(x), 1)
	per_close = datetime.date(2016, int(x)+1, 1)
	
	with open('%s.csv' % y , 'r') as a:
		debit_file = csv.reader(a)
		debit = ()
		deb = 0
		credit = ()
		cred = 0
		for d in debit_file:
			date = d[4]
			month, day, year  = map(int, date.split('/'))
			d2 = datetime.date(year, month, day)
			if per_open <= d2 < per_close:
				debit = d[1]
				deb += int(debit)
	with open('%s.csv' % y , 'r') as a:
		credit_file = csv.reader(a)
				
		for c in credit_file:
			date = c[4]
			month, day, year  = map(int, date.split('/'))
			d2 = datetime.date(year, month, day)
			if per_open <= d2 < per_close:
				credit = c[2]
				cred += int(credit)	
		
	print "Period: %s\nDebit total: %s\nCredit total: %s" % (x, deb, cred)
	see_details = raw_input("Would you like to see period details? Y/N: ")
	if see_details.upper() == "Y":
		with open('%s.csv' % y , 'r') as a:
			debit_file = csv.reader(a)
			for d in debit_file:
				date = d[4]
				month, day, year  = map(int, date.split('/'))
				d2 = datetime.date(year, month, day)
				if per_open <= d2 < per_close:
					print d
					
					

