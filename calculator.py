#calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #print what options you have
    print "Welcome to calculator.py"

    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit calculator.py"
    print " "

    choice = input("Choose your option: ")
    if choice == 1:
        add1 = input("Enter your First Number: ")
        add2 = input("Enter Your Second Number: ")
        print add1, "+", add2, "=", add1 + add2
    elif choice == 2:
        sub2 = input("nter your First Number: ")
        sub1 = input("Enter Your Second Number: ")
        print sub1, "-", sub2, "=", sub1 - sub2
    elif choice == 3:
        mul1 = input("nter your First Number: ")
        mul2 = input("Enter Your Second Number: ")
        print mul1, "*", mul2, "=", mul1 * mul2
    elif choice == 4:
        div1 = input("nter your First Number: ")
        div2 = input("Enter Your Second Number: ")
        print div1, "/", div2, "=", div1 / div2
    elif choice == 5:
        loop = 0
    
print "Thankyou for using calculator.py!"  