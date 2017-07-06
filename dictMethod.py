my_dict={"ID":123,"Name":"Moshabbar","Dept":"IT","Salary":12000}
# print my_dict.keys()
# print my_dict.values()
# 
# # Only Keys output purpose...
# for i in my_dict.keys():
#     print i
#   
# # Only Values output showing Purpose....
# for j in my_dict.values():
#     print j 
     
# For Key value output Purpose.....      
# var1=my_dict.iteritems()
# for key,v in var1:
#     print key ,v    

# print Out The Result as per Dictionary format
# for key,v in sorted(my_dict.iteritems()):
#     print key,v    
# 
# for key, value in sorted(my_dict.iteritems(), key=lambda (k,v): (v,k)):
#     print "%s: %s" % (key, value) 
import collections 
print collections.OrderedDict(my_dict)
