# Creating a class First

class Employee:
    # Methods for class:
    def __init__(self,name,age,sex,salary,dept,duration):
        
        
        self.name=name
        self.age=age
        self.salary=salary
        self.sex=sex
        self.dept=dept
        self.duration=duration

    # Calling For class ...        
    def displayEmp(self):
        
        print "Emp Name:",self.name
        print "Emp Age:",self.age
        print "Emp Sex:",self.sex
        print "Emp Salary:",self.salary
        print "Emp Dept:",self.dept
        print "Emp Duration:",self.duration
        print "Emp Name:",self.name,"Emp Age:",self.age, "Emp Sex:",self.sex, "Emp Salary:",self.salary, "Emp Dept:",self.dept, "Emp Duration:",self.duration
# creating second Class         
class Hospital:
    # Method for Class
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone
    # Calling for that Method     
    def displayHospital(self):
        print "Hospital Name",self.name 
        print "Hospital Address:",self.address
        print "Hospital Phone:",self.phone
        print self.name,self.address,self.phone
        
# creating My third Class        
        
class College:
    
    # Method For Third Class
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone
    # Calling Method Purpose   
    def displayCollege(self):
        print "College Name",self.name 
        print "College Address:",self.address
        print "College  Phone:",self.phone
        print self.name,self.address,self.phone

class Restrorent:
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone
        
    def displayRestrorent(self):
        print " Name",self.name 
        print "Address:",self.address
        print "Phone:",self.phone
        print self.name,self.address,self.phone
            
                
        

print ".........................................Employee Records........................................................."                              
c1=Employee("Zara",24,"F",12000,"IT","4 years")
c2=Employee("Moshabbar",24,"M",12000,"IT","2 years")
c3=Employee("Irshad",30,"M",22000,"IT","3 years")
c4=Employee("Rahul",25,"M",12000,"IT","1 years")
c5=Employee("Raju",30,"M",12000,"IT","3 years")
c6=Employee("Rakesh",24,"M",12000,"IT","1 years")
c7=Employee("lohit",24,"F",12000,"IT","5years") 
c1.displayEmp()
c2.displayEmp()
c3.displayEmp()
c4.displayEmp()
c5.displayEmp()
c6.displayEmp()
c7.displayEmp()
 
print "............................................Hospital Records........................................................"
c1=Hospital("Applow Hospital","Banjara Hills Road No -5 ,Hyderabad",400786543)
c2=Hospital("Sorojini Eye Hospital","Mehdipatnam ,Hyderabad",400765544)
c3=Hospital("Cricent Hospital","S R Nagar ,Hyderabad",40769087)
c4=Hospital("Durga Hospital","Banjara Hills Road No -12 ,Hyderabad",405643389)
c1.displayHospital()
c2.displayHospital()
c3.displayHospital()
 
print "...........................................College Records........................................................."
c1=College("Mahaveer College of Engineering","Banjara Hills Road No -5 ,Hyderabad",400786590)
c2=College("Sorojini Eye College","Mehdipatnam ,Hyderabad",4005544788)
c3=College("Lara College Of Science & Tech.","S R Nagar ,Hyderabad",407690871)
c4=College("Durga College of Degree","Banjara Hills Road No -12 ,Hyderabad",405643354)
c1.displayCollege()
c2.displayCollege()
c3.displayCollege()
c4.displayCollege()

print ".............................................Restourent Records..................................................."
c1=Restrorent("Hussain Resturent" ,"Mumbai Road no 5",89078900)
c2=Restrorent("Irshad  Resturent" ,"Delhi Road no 9",890787876)
c3=Restrorent("Brother Resturent" ,"Hyderabad Road no 5",890564321)
c4=Restrorent("Star Resturent" ,"Ahmedabad Road no 5",89076755675)
c1.displayRestrorent()
c2.displayRestrorent()
c3.displayRestrorent()
c4.displayRestrorent()






         
        
        
    