import xlrd
#Location path for excel sheet

file_location='C:\\Users\\mayank\\desktop\\data.xlrd.xlsx'
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
# workbook.cell_value(0,0)

#number of rows in excel sheet
# p=sheet.nrows
# print p

# Number of culumns in excel sheet
# s=sheet.ncols
# print s

# printing colums from excel sheet what columns you want
# for col in range(sheet.ncols):
#     print sheet.cell_value(3,col)

#Number of Rows from excel sheet.
# 
# cells =sheet.row_slice(rowx=0,start_colx=0)
# for cell in cells:
#     print cell.value
#  #Printing what columns you want will print in list format    
# print sheet.row_values(6)

# # This is for how many sheet in our excel
# print workbook.nsheets

# For getting Total excel Sheet purpose
total_rows=sheet.nrows
tota_cols=sheet.ncols
table=list()
record=list()
x=0
y=0

for x in range(total_rows):
    for y in range(tota_cols):
        record.append(sheet.cell_value(x,y))
    table.append(record) 
    record=[]
    x+=1
print table    
for mytable in table:
    print mytable


# For Json Format Purpose......... 
  
import json
json_output=json.dumps(table)
print json_output  




                            
    
                       
    

      
#Getting Full data from excel......
# n=0
# i=0
# x={}
# file=open("data.xlrd.xlsx","r")
# for n in range(sheet.nrows):
#     for i in range(sheet.ncols):
#         data =sheet.cell_value(n,i)
#         print  data,
#         x.append(data)
#         print x
#    
             
    





 



