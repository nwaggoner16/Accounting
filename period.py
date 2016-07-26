import datetime

def date_check(x):
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
	
	if period1 <= date1 < period2:
		print "Period 1"
	elif period2 <= date1 < period3:
		print "Period 2"
	elif period3 <= date1 < period4:
		print "Period 3"
	elif period4 <= date1 < period5:
		print "Period 4"
	elif period5 <= date1 < period6:
		print "Period 5"
	elif period6 <= date1 < period7:
		print "Period 6"
	elif period7 <= date1 < period8:
		print "Period 7"
	elif period8 <= date1 < period9:
		print "Period 8"
	elif period9 <= date1 < period10:
		print "Period 9"
	elif period10 <= date1 < period11:
		print "Period 10"
	elif period11 <= date1 < period12:
		print "Period 11"
	elif period12 <= date1 < year_end:
		print "Period 12"										
	else:
		print "Not a proper date"
