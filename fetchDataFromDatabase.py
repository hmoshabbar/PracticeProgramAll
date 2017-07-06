import cx_Oracle
import json
SQL="Select first_name,Last_name,email,id from USERS"
# For Local Database............

# dsnStr=cx_Oracle.makedsn("localhost","1521","orcl")
# conn=cx_Oracle.connect(user="att", password="admin", dsn=dsnStr)

#For Server Database..................................

dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
conn=cx_Oracle.connect(user="att", password="Externet", dsn=dsnStr)
cursor=conn.cursor()
cursor.execute(SQL)
data=cursor.fetchall()

# row_list={}
# myList=[]
# 
# for first_name,last_name,email,id in cursor:
#     row_list={
#         
#         "first_name":first_name,
#         "Last_name":last_name,
#         "email":email,
#         "id":id
#         
#     }
#     myList.append(row_list)
    

 
    

json_output=json.dumps(data)
print(json_output)
     
 
cursor.close()
conn.close()



