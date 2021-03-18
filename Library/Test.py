s  =[]

for i in range(10):
    s.append(i**2)
print(s)

add = lambda x,y:x+y
print(add(1,2))

#download a file from web

##import requests
##file_url = 'https://www.facebook.com/favicon.ico'
##
##image  = requests.get(file_url)
##print(image)
##
##with open('D:/eTender/facebook.ico','wb') as f:
##    f.write(image.content)

dict  = {'a':1,'b':2}

print(dict.keys())
print(dict.values())

for i in dict.items():
    print(i)

string = 'SURESH'
print(string.lower())
print(string.upper())
print(string.swapcase())

lower  =[]
upper = []

with open('D:/test.txt','r') as fh:
    count = 0
    text = fh.read()
    for character in text:
        #if character.islower():
            #a= lower.append(character)
            #print(character)
        if character.isupper():
            print(len(character))
            print(character)


test = [1,5,3,9,8,34]
test.sort()
print(test)

##import xlrd
##import openpyxl

#Reading data from Excel
##book=xlrd.open_workbook('D:/Test/details2.xlsx')
##sheet=book.sheet_by_name('Old')
##
##i=0
##while i < 2:
##    rows = sheet.row_values(i)
##    print(rows)
##    i=i+1

x = [1,5,6,9,10,14,34]

x.sort()
print(x)
print(x[-1])
print(x[-2])

newlist  =0
for i in x:
    newlist = i+newlist
print(newlist)
##import random
##
##with open('D:/test.txt','r') as fh:
##    value = fh.read().splitlines()
##    print(value)
##    print(random.choice(value))

print (sum(1 for line in open('D:/test.txt','r') ))
#duplicate
list1 = [1,1,2,2,3,3,4,5,6,6]

newlist = []

for i in list1:
    if i not in newlist:
        newlist.append(i)
print(newlist)
#reverse a string
string = 'suresh'
emptystr  =""
for i in string:
    emptystr=  i+emptystr
print(emptystr)

#sorting without using sort menthod
list2  = [1,3,4,56,1,2]
newlist1  =[]

for i in range(len(list2)):
    minvalue = min(list2)
    newlist1.append(minvalue)
    list2.remove(minvalue)
print(newlist1)

with open('D:\Test\employees - Copy.csv', 'r') as t1, open('D:\Test\employees.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('D:/Test/update.csv', 'w') as outFile:
    for line in filetwo:
        #print(line)
        if line not in fileone:
            #print(line)
            outFile.write(line)

with open('D:/test.txt','r') as f:
    value=f.read()

upper=[]
lower=[]
for i in value:
    if i.isupper():
        upper.append(i)
    else:
        lower.append(i)

print(len(upper))
print(len(lower))
print(upper)
print(lower)

test1  = [1,2,2,3,1]
newlist  = []

for i in test1:
    if i not in newlist:
        newlist.append(i)
print(newlist)

#PyTest Fixures
import pytest
@pytest.fixture()
def setup():
    print("once efore every method")

def testmethod1(setup):
    print("test method1")

def testmethod2(setup):
    print("test method2")


