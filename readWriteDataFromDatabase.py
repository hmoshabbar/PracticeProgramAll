import cx_Oracle
# import json
# import collections


SQL="Select id, first_name,Last_name,email from USERS"


#For Server Database..................................

dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
conn=cx_Oracle.connect(user="att", password="Externet", dsn=dsnStr)
cursor=conn.cursor()
cursor.execute(SQL)
rows=cursor.fetchall()
rowArray_List=[]
for row in rows:
    print "Id:",row[0]
    print "First Name:",row[1]    
    print "Last Name:",row[2]   
    print  "Email:",row[3]
    
#     json_output=json.dumps(row)
#     rowArray_List.append(json_output)
#     print(rowArray_List)
   
    
    
#     d=collections.OrderedDict()
#     d["id"]=row.id
#     d["first_name"]=row.first_name
#     d["Last_name"]=row.last_name
#     d["email"]=row.email
#     rowArray_List.append(d)
#     j=json.dumps(rowArray_List) 
# print j 

    
    