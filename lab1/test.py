import math

numOfTest =int(input("Enter the number of Test: "))
testData=[]

for i in range(numOfTest):
    hi,we,cl = input("Enter height weight class: ").split()
    person=[hi,we,cl]
    testData.append(person)

hei,wei =input("Enter height weight for test: ").split()

result={}

for i in range(len(testData)):
    dh=int(testData[i][0])-int(hei)
    dh=math.pow(dh,2)
    dw=int(testData[i][1])-int(wei)
    dw=math.pow(dw,2)
    df=math.sqrt(dh+dw)
    result[df]=testData[i][2]

sorted(result)
print(result)
print(next(iter(result.values())))



