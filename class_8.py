"""
i=2
while i<10:
    print(i)
    i+=1

i=0
a="debajyoti"
while i < len(a):
    print(a[i])
    i+=1

#infinite loop
i=2
while True:
    print(i)

i=2
while i<10:
    print(i)
    i-+1    
"""
"""
i=2
while i<18:
    i+=2
    print(i)
else:
    #print("The loop is over")        
    sq_i=i**2
    print("The square of the number is :-",sq_i)"""

li=[2,3,4,5,6]
i=0
while i<len(li):
    if li[i]==5:
        print("We got 5")
        break
    i+=1
else:
    print("We can't find 5")    

