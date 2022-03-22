from datetime import datetime
from dateutil.parser import parse
b = input("Input date in the date-month-year format:\t")
a = parse(b, dayfirst = True)#reading the date format with day first
c = datetime.date(a)
d = c.strftime("%-m/%-d/%Y")
print("Date in western format 'mm/dd/yyyy' is: ",d)
