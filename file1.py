import json
import cx_Oracle
# import collections
# from _sqlite3 import Row
from fetchData import json_output2
# from symbol import except_clause
def fetch_data_from_database():
    try:
        
        SQL="select json_msg from INSERT_JSON where id='rx6461' "
        snStr=cx_Oracle.makedsn("172.16.113.103", "1521", "orcl")
        conn=cx_Oracle.connect(user="practice", password="Externet", dsn=snStr)
        cursor=conn.cursor()
        cursor.execute(SQL)
        data=cursor.fetchone()
        for row in data:
            json_output=row.read()
            json_output2=json.loads(json_output)
            for rows1 in json_output2["MetricsColumns"]:
                print rows1
                print "parentId:",rows1['parentId']
                print "ID:",rows1['id']
                print "Name:",rows1['name']
                print "Level:",rows1['level']
                print ("{0},{1},{2},{3}".format(rows1['parentId'],rows1['id'],rows1['name'],rows1['level']))
    except cx_Oracle.Error:
        if conn:
            conn.rollback()
            print "Therw was a problem in your Connections please check it again"
    finally:
        if conn:
            conn.close() 
            print "Sucessfull You get your data  Thank you"     
                    
                


    
       
          
        
        
        
    

