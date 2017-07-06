import calendar
y=int(input("Enter your Year:"))
s=calendar.calendar(y,2,1,5,6)
print ".......................CALENDAR................................::",y,"::.........................CALENDAR.....................................",s

if y%4==0:
    print "You Entered Year is:",y
    print "Yes its a leap year"
else:
    print "You Entered Year is:",y 
    print "No its  not a leap year" 