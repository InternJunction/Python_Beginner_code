"""#larger number
num1=int(input("Enter the first nummber:-"))
num2=int(input("Enter the second nummber:-"))
if num1 > num2:
    print(num1,"is larger number")
elif num1 == num2:
    print("Both numbers are equal")    
else:
    print(num2,"is larger number")    """
"""# even-odd
num1=int(input("Enter a number"))
if num1%2==0 and num1!=0:
    print(num1,"is even number")
elif num1==0:
    print(num1," is zero")
else:
    print(num1,"is odd number")    
"""

#leapyear
year=int(input("Enter a year:-"))

if year%100==0 and year%400==0:
    print("The year is leap year") 
elif year%100!=0 and year%4==0:
    print("The year is leap year")  
else:
    print("The year is not leap year")      

"""
#triangle
side1=int(input("Enter the first side:-"))
side2=int(input("Enter the second side:-"))
side3=int(input("Enter the third side:-"))

if (side1+side2 > side3) and (side1+side3 > side2) and (side2+side3 > side1): #triangle validity
    if (side1==side2==side3):
        print("This is a Equilateral triangle")
    elif (side1==side2) or (side2==side3) or (side1==side3):
        print("This is a isoscalen triangle")
    elif (side1 !=side2!=side3):
        print("This is a scalen triangle")
else:
    print("Give some valid input")                
"""







