"""#Creating Variables
a=10
print(a)
b="Internjunction"
print(b)
c=False
print(c)
d=10.99
print(d)
#Casting
e=str(a) #str actually turns anything into string
print(e)
print(type(e))
f=str(c)
print(f)
#Get the Type
abc="10"

print(type(abc))

#Case-Sensitive
abc=10
ABC=20
print(abc)
print(ABC)
#Variable Name rules
abc=5
a_b_c=6
_abc=7
#9abc=90
a_9_b_c=10
A_99bc=10
if=78
print(if)    
#Camel Case 
#Pascal Case
#Snake Case
#Assigning single value to multiple variables
a=5
b=5
c=5
print(a,b,c)
a=b=c=6
print(a,b,c)
#Assigning multiple values to multiple variable
a,b,c=5,6,7
print(a,b,c)
print(c)
print("The value of c is ", c)"""
"""#Local Variable
def add():
    a=5
    b=6
    return a+b
print(add())

#Global Variable
a=10
def add():
    a=5
    b=6
    return a+b
print(add())
print(a)"""
#Delete a variable
a=10
del a
print(a)