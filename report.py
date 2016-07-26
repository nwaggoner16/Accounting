import csv
import datetime

def view_period_total(x,y):
	acn = y
	per_entry = x
	
	period1 = datetime.date(2016,1,01)
	period2 = datetime.date(2016,2,01)
	period3 = datetime.date(2016,3,01)
	period4 = datetime.date(2016,4,01)
	period5 = datetime.date(2016,5,01)
	period6 = datetime.date(2016,6,01)
	period7 = datetime.date(2016,7,01)
	period8 = datetime.date(2016,8,01)
	period9 = datetime.date(2016,9,01)
	period10 = datetime.date(2016,10,01)
	period11 = datetime.date(2016,11,01)
	period12 = datetime.date(2016,12,01)
	year_end = datetime.date(2016,12,31)
	
	with open('%s.csv' % acn , 'r') as a:
		debit_file = csv.reader(a)
		debit = ()
		deb = 0
		credit = ()
		cred = 0
		for d in debit_file:
			date = d[4]
			month, day, year  = map(int, date.split('/'))
			d2 = datetime.date(year, month, day)
			if period1 <= d2 < period2:
				debit = d[1]
				deb += int(debit)
	with open('%s.csv' % acn , 'r') as a:
		credit_file = csv.reader(a)
				
		for c in credit_file:
			date = c[4]
			month, day, year  = map(int, date.split('/'))
			d2 = datetime.date(year, month, day)
			if period1 <= d2 < period2:
				credit = c[2]
				cred += int(credit)		
			
	print "Period: %s\nDebit total: %s\nCredit total: %s" % (x, deb, cred)
	see_details = raw_input("Would you like to see period details? Y/N: ")
	if see_details.upper() == "Y":
		with open('%s.csv' % acn , 'r') as a:
			debit_file = csv.reader(a)
			for d in debit_file:
				date = d[4]
				month, day, year  = map(int, date.split('/'))
				d2 = datetime.date(year, month, day)
				if period1 <= d2 < period2:
					print d
	

def period_total(x):
	date_entry = x
	month, day, year = map(int, date_entry.split('/'))
	date1 = datetime.date(year, month, day)
	period1 = datetime.date(2016,1,01)
	period2 = datetime.date(2016,2,01)
	period3 = datetime.date(2016,3,01)
	period4 = datetime.date(2016,4,01)
	period5 = datetime.date(2016,5,01)
	period6 = datetime.date(2016,6,01)
	period7 = datetime.date(2016,7,01)
	period8 = datetime.date(2016,8,01)
	period9 = datetime.date(2016,9,01)
	period10 = datetime.date(2016,10,01)
	period11 = datetime.date(2016,11,01)
	period12 = datetime.date(2016,12,01)
	year_end = datetime.date(2016,12,31)
	
