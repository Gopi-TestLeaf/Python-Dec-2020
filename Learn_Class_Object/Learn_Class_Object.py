# Class is like a Blue print

class Mobile:
    # data (Properties) ----> variable --> OS, Model, Name
    # logic(Actions)    ----> Method ----> dialCall, sendSMS
    # build (object)    ----> Constructor

    def dail_number(self, ph):      # Instance method
        print('dailing.....')
        print("self: ", self)

    def send_SMS(self):
        print('sending.....')

# Create the Object - Syntax -> Object = ClassName()
m1 = Mobile()
m1.dail_number(959770458)
print("Object: ",m1)
print("************************************")
m2 = Mobile()
m2.dail_number(909090123)
print("Object: ",m2)


