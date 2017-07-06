data1={
    'Name':'Moshabbar',
    'Id':103,
    'Adress':'1st street hyderabad',
    'Phone':78906556576
    }
data2={
    'Name':'Irshad',
    'Id':104,
    'Adress':'1st SR Nagar',
    'Phone':7890888888
    }
data3={
    'Name':'Rahul',
    'Id':105,
    'Adress':'6st street Masabtank',
    'Phone':989878878878
    }
data4={
    'Name':'Raqibul',
    'Id':106,
    'Adress':'1st Eragadda',
    'Phone':6778876898878
    }
import json
myJson=[]
json_output1=json.dumps(data1)
json_output2=json.dumps(data2)
json_output3=json.dumps(data3)
json_output4=json.dumps(data4)

data1=myJson.append(json_output1)
data2=myJson.append(json_output2)
data3=myJson.append(json_output3)
data4=myJson.append(json_output4)
# merged_dict={key: value for (key, value) in (data1.items()+data2.items()+data3.items()+data4.items())}

# data1=myJson.append(json_output1)
# data2=myJson.append(data1)
# data3=myJson.append(data2)
# data4=myJson.append(data3)

json_output=json.dumps(data4)
print(myJson)

