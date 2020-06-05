#open file

myFile=open('myfile.txt','w')

#get somme info

print('Name:',myFile.name)
print('is closed:',myFile.closed)
print('openeing mode: ',myFile.mode)

#write to file
myFile.write('I love python')
myFile.write('I lovjabdjsdnn')
myFile.close()

myFile=open('myfile.txt','a')
myFile.write('I also like PHP')
myFile.close()

myFile=open('myfile.txt','r+')
text=myFile.read(100)
print(text)
