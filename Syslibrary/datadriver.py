import json

class jsonread():
 def jsonread(self,filename):
    with open(filename) as jsonfile:
     value = json.load(jsonfile)
     return value