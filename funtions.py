
#create funcion
def sayhello(name='sachin'):
    print(f'hello {name}')

sayhello('sahc')

#return values

# def getsum(num1,num2):
#     total=num1+num2
#     return total


# num=getsum(3,4)
# print(num)

#lambda function
getsum=lambda num1,num2: num1+num2

print(getsum(3,10))