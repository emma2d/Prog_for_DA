import datetime



print("Check if it is Tuesday")

today = datetime.datetime.today()
day_of_week = today.weekday()

if day_of_week == 1:
    print("It's Tuesday")
elif day_of_week == 2:
    print("It is Wednesday")
elif day_of_week == 0:
    print("It is Monday")
else:
    print("It's not Tuesday")

