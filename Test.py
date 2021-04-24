import datetime
#For Testing statements to not effect the database


#test datetime
x = datetime.datetime.now()
x = x.replace(microsecond=0)
print(x)