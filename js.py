#First we are importing Json
import json

#Taking One data in a Dictionary fromat like as a key pair value

data={
    'Name':'Moshabbar',
    'Id':103,
    'Adress':'1st street hyderabad',
    'Phone':78906556576
    }
#Creating a New data as a list Format i want all data have to come under this format

data1=[]
json_output=json.dumps(data)
#Appending data into data1 
  
data=data1.append(json_output)
#Now printing Data1
print(data1)


# #Another program  for writing json data:
# json_output=json.dumps(data)
# data=json.loads(json_output)
# # Writing JSON data
# with open('data.json', 'w') as f:
#      json.dump(data, f)
# print(data)     
# # Reading data back
# with open('data.json', 'r') as f:
#      data = json.load(f)
# print(data)   
for i in data.keys():
    print i
        
