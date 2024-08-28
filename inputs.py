# Halloween Day

# Published by BijogFc24 in JavaScript▾

# dates

# language_fundamentals

# validation

# Create a function that takes date in the format yyyy/mm/dd as an input and returns "Bonfire toffee" if the date is October 31, else return "toffee"

# Examples

# halloween (new Date("2013/10/31")) "Bonfire toffee"

# halloween (new Date("2012/07/31")) "toffee"

# halloween (new Date("2011/10/12")) "toffee"




# from datetime import datetime 

# def halloween(date):

#     month =date.month
#     day= date.day

#     if month==10 and day==31:
#         return "Bonfire toffee"
#     else:
#         return "toffee"
# print("Appeared result ---> ", halloween(datetime.strptime("2013/10/31", "%Y/%m/%d")))
# print("Appeared result ---> ", halloween(datetime.strptime("2012/07/31", "%Y/%m/%d")))
# print("Appeared result ---> ", halloween(datetime.strptime("2011/10/12", "%Y/%m/%d"))) 


# ____________________________________________________________________________________________________________________________________________________________________________

# Convert Year to Century

# Posted by Matt in JavaScript

# algorithms

# dates

# math

# Write a function that takes a year and returns its corresponding century.

# Examples

# centuryFromYear (2005) + 21

# centuryFromYear (1950) → 20

# centuryFromYear (1900) 19

# Notes

# For guidance on the year boundaries for each century:

# The 19th century are the years from 1801 to 1900.

# The 20th century are the years from 1901 to 2000.



# from datetime import datetime

# def century(year):
#     return (year - 1) // 100 + 1


# print("Centuries ---> ", century(2005))
# print("Centuries ---> ", century(1950))
# print("Centuries ---> ", century(1900))

# ____________________________________________________________________________________________________________________________________________________________________________

# After N Mobths....

# Create a function that takes in year and months as input, then return what year it would be after n-months have elapsed.

# Examples

# afterNMonths (2020, 24) → 2022

# afterNMonths (1832, 2)→ 1832

# afterNMonths (1444, 60) → 1449

# Notes

# • Assume that adding 12 months will always increment the year by 1.

# If no value is given for year or months, return "year missing" or "month missing"

# At least one value will be present.

# from datetime import datetime

# def after_n_months(year, months):
#     if year == 1:
#         return "year missing"
#     if months == 1:
#         return "month missing"
#     return year + (months // 12)

# print("Result from given input ---> ", after_n_months(2020, 24))
# print("Result from given input ---> ", after_n_months(1832, 2))
# print("Result from given input ---> ", after_n_months(1444, 60))

# ____________________________________________________________________________________________________________________________________________________________________________


# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

# Examples

# formatDate("11/12/2019") + "20191211"

# formatDate("12/31/2019") + "20193112"

# formatDate("01/15/2019") "20191501"

# Notes

# Return value should be a string.



# from datetime import datetime

# def formatDate(date: str):
#     return datetime.strptime(date, "%m/%d/%Y").strftime("%Y%d%m")

# print("Output---> ", formatDate("11/12/2019"))
# print("Output---> ", formatDate("12/31/2019"))
# print("Output---> ", formatDate("01/15/2019"))

# ____________________________________________________________________________________________________________________________________________________________________________

# Is it Time for Milk and Cookies?
# Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns true if it's Christmas Eve (December 24th) and false otherwise. Keep in mind JavaScript's Date month is O based, meaning December is the 11th month while January is 0.

# Examples

# timeForMilkAndCookies (new Date (2013, 11, 24)) true

# timeForMilkAndCookies (new Date (2013, 0, 23)) false

# timeForMilkAndCookies (new Date (3000, 11, 24)) true

# Notes

# Dates are zero based (see resources).

# All test cases contain valid dates.



# from datetime import datetime

# def gift_time(date: datetime):
#     return date.month == 12 and date.day == 24
# print("Gift Time ---> ", gift_time(datetime(2013, 12, 24)))
# print("Gift Time ---> ", gift_time(datetime(2013, 1, 23)))
# print("Gift Time ---> ", gift_time(datetime(3000, 12, 24)))


# |______________________________________________________________________________________________________________________________________________________________________________

# Get the date

# Write a function that, given a date (in the format MM/DD/YYYY), returns the day of the week as a string. Each day name must be one of the following strings: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", or "Saturday".

# To illustrate, the day of the week for "12/07/2016" is "Wednesday".

# Examples

# getDay("12/07/2016") "Wednesday"

# getDay ("09/04/2016") "Sunday"

# getDay("12/08/2011") "Thursday"

# Notes

# This challenge assumes the week starts on Sunday.


# from datetime import datetime

# def Day(date: str):
#     date_date = datetime.strptime(date, "%m/%d/%Y")
#     return date_date.strftime("%A")

# print("Week day output ---> ", Day("12/07/2016"))
# print("Week day output ---> ", Day("09/04/2016"))
# print("Week day output ---> ", Day("12/08/2011"))


