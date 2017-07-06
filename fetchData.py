#..................................................................................................................
import cx_Oracle
import json
# import collections
 
    
SQL="select json_msg from INSERT_JSON where id='rx6461' "
# #For Server Database..................................
#       
dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
conn=cx_Oracle.connect(user="practice", password="Externet", dsn=dsnStr)
cursor=conn.cursor()
cursor.execute(SQL)
data=cursor.fetchone()
# l IS USE FOR EMPTY LIST WHERE WE APPEND ALL DATA.
l=[]
for rows in data:
    json_output=rows.read()
#     print (json_output)
    json_output2=json.loads(json_output)
    print(json_output2)
    for MetricsColumns in json_output2['MetricsColumns']:
        print (MetricsColumns)
        print "parentId:",MetricsColumns['parentId']
        print "ID:",MetricsColumns['id']
        print "Name:",MetricsColumns['name']
        print "Level:",MetricsColumns['level']
        print ("{0},{1},{2},{3}".format(MetricsColumns['parentId'],MetricsColumns['id'],MetricsColumns['name'],MetricsColumns['level']))
        
# FOR APPENDING PURPOSE UNDER LIST ......        
        
#         x=("{0},{1},{2},{3}".format(MetricsColumns['parentId'],MetricsColumns['id'],MetricsColumns['name'],MetricsColumns['level']))
#            
#         l.append(x)
#         print l
#          
# json_out=json.dumps(l)
# json_output5=json.loads(json_out)
# print(json_output5)       
        
        
        
       
        
        
       
        
    
            
    
    


    
    
    
    
    
    
    
#     selected_row=data[rows]
#   
#     for item in selected_row:
#         selected_row1=selected_row[item]
#         data1=[]
#         index=1
#         data1.append(selected_row1[len(selected_row1)-index])
#     list1.append(data1)
#         
# json_output=json.dumps(list1) 
# print(json_output)       
        
        
        
        
        
        
        
    

   

        
  
   
   
 
    
    
#     elemant=data[rows]
#     for elemant1 in elemant:
#         done=elemant[elemant1]
#         index=1
#         while (index<=1):
#             array.append(done[len(done)-index])
#             index=index+1
#     json_output=json.dumps(array)
#     print (json_output)        
    
       
        
        
    
    


# done=json.loads(data[0][0].read())
# json_output=json.dumps(done)
# playerstuff = json_output['MetricsColumns']
# for i in playerstuff:
#     print i['MetricsColumns']
# cursor.close()
# conn.close()
#    
# print data

#...............................................................................................................

      
  

       
#  
# import collections
# import cx_Oracle      
# import json
# dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
# conn=cx_Oracle.connect(user="practice", password="Externet", dsn=dsnStr)
# cursor=conn.cursor()
# cursor.execute("select * from insert_json")
# rows = cursor.fetchall()
# done=json.loads(rows[0][0].read())
#    
# array1=[]
#    
# for elemant in rows:
#     data=rows(elemant)
#     for elemant1 in data:
#         data_1=data[elemant1]
#         data1=[]
#         index=1
#         while(index<=3):
#             data1.append(data_1[len(data_1)-index])
#             index=index+1
# #             array2.update({elemant1 : data1})
# #     array3.update({elemant:array2})
# json_data = json.dumps(array1)
# print json_data

#........................................................................................................................................ 
# import json
# import cx_Oracle
# def fetch_data(self):
#     dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
#     conn=cx_Oracle.connect(user="practice", password="Externet", dsn=dsnStr)
#     cur=conn.cursor()
#     cur.execute("Select json from insert_json ")
#     rows=cur.fetchall()
# for row in rows:
#      
#     print row
 
#.......................................................................................................................................
# import cx_Oracle
# import json
# import collections
#  
#  
#      
# SQL="Select json  from INSERT_JSON "
# #For Server Database..................................
#        
# dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
# conn=cx_Oracle.connect(user="practice", password="Externet", dsn=dsnStr)
# cursor=conn.cursor()
# cursor.execute(SQL)
# data=cursor.fetchall()
# rowArray_list=[]
# while True:
#     row = cursor.fetchone()
#     if not row: break
#     t=row[0]
#  
# print  t
# rowArray_list.append
      
#..............................................................
# import json
# import cx_Oracle
# import collections
# dsnStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
# conn=cx_Oracle.connect(user="practice", password="Externet", dsn=dsnStr)
# json_msg=" Select id, json_msg from  insert_json "
# cursor=conn.cursor()
# cursor.execute(json_msg)
# for id, json_msg in cursor:
#     json_output=json_msg.read()
#     my_json=json.dumps(json_output)
#     for MetricsColumns in  my_json ["MetricsColumns"]:
#         print MetricsColumns

    
   
    
         
    

   
    
        
            
            
    
    






  





