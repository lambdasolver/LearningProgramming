import math

i = 2
flag = 0
a=int(input("Enter a number: "))
if (a < 0):
    print("Wrong Number")
elif (a == 0 and a == 1):
    print("Not Prime")
elif (a==2 and a == 3):
    print("Prime")
for i in range(2,int(math.sqrt(a))+1):
    if (a%i == 0):
        print("Not Prime")
        flag = 1
        break
if (flag == 0):
    print("Prime")
