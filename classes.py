class User:
    #constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'
    def has_birthday(self):
        self.age+=1


#extend class 
class Customer(User):
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance=0

    def set_balance(self,balance):
        self.balance=balance
    
    def greeting(self):
        return f'My name is {self.name} and i am {self.age} and balance {self.balance}'
           
    

janet=Customer('janet jhnson','akjhksa@jkfe',25)
print(janet.greeting())
#init object
sachin= User('sachin kumar','cashin@gmail.com',22)

sachin.has_birthday()
print(sachin.greeting())
