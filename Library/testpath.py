import os
import sys

dir_path = os.getcwd()
print(dir_path)

folder_path = os.path.abspath(os.path.join(dir_path,os.pardir))
print(folder_path)

sys.path.insert(0,folder_path+'/Library')

string = 'suresh'
revstring = ''

for i in string:
    revstring = i + revstring
print(revstring)

list1 = [1,2,3,4,5,5]
newist = []

for i in list1:
    if i not in newist:
        newist.append(i)
print(newist)

print([x for x in range(8) if x%2==0])
dict1 = {'a':1,'b':2,'c':3}

for k,v in dict1.items():
    print(k,v)

print(dict1.keys())
print(dict1.values())



