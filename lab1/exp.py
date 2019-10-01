import math

numOfTest =int(input("Enter the number of Test: "))
testData=[]

for i in range(numOfTest):
    hi,we,cl = input("Enter height weight class ").split()
    person=[hi,we,cl]
    testData.append(person)

hei,wei =input("Enter height weight for test").split()

small=10000
name=""

for i in range(len(testData)):
    dh=int(testData[i][0])-int(hei)
    dh=math.pow(dh,2)
    dw=int(testData[i][1])-int(wei)
    dw=math.pow(dw,2)
    df=math.sqrt(dh+dw)
    if df<small:
        small=df
        name=testData[i][2]

print(name)
    


