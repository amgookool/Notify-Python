#importing the date-time module to work with date and time objects
import datetime

#importing the elder person class from the data folder/Elder.py
#the '*' tells python that we want to include everything from the Elder.py file into this current file
from data.Elder import *

person = Patient('Pete',['Mon','Tue'],2)

#setting the current date into a variable
curr_date = datetime.datetime.now()

print(curr_date)