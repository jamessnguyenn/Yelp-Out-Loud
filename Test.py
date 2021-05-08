import datetime
import uuid
#For Testing statements to not effect the database


#test datetime
x = uuid.uuid4().hex
print(str(x)[0:3]+'-'+str(x)[3:21])