class MobileTransaction:
    def __init__(self):
        print("this is parent class")
    def parent_method(self):
        print("This is parent method")
    
class Bkash(MobileTransaction):
    def __init__(self):
        print("This is Bkash constructor")
    def parent_method(self):
        print("This is Bkash method,")
    def send_money(self,phone,amount,fee,pin,finger):
        print(phone,amount,fee,pin,finger)

class nexuspay(MobileTransaction):
    def __init__(self):
        print("This is nexuspay constructor")
    def parent_method(self):
        print("This is nexus method,")
    def send_money(self,phone,amount,fee,pin,otp):
        print(phone,amount,fee,pin,otp)


b=Bkash()

b.parent_method()
b.send_money(0,100,5,12345,1)
c=nexuspay()
c.send_money(0,100,2,123456,3452)