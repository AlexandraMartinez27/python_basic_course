year = input("birth year:   ")
print(type(year))

from datetime import date
currenty = date.today().year
print(currenty)

age = currenty - int(year)
print(type(age))

from datetime import date
currentd = date.today().day
print(currentd)

from datetime import date
currentm = date.today().month
print(currentm)

