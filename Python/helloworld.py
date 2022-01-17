#a=int(input())
def fact(num):
    if (num==1):
        return 1
    else:
        return(num*fact(num-1))
def f(num):
    facsum=0
    if (num<10):
        facsum = fact(num)
    else:
        while (num != 0):
            facsum=facsum+fact(num%10)
            num = num // 10
    return facsum

def g(num):
    i=1
    if(num < 10):
        while (num!=fact(i)):
            i=i+1
        return i
    else:
        result=0
        while (i>=1):
            print((f(i)))
            if(s(f(i))==num):
                break
            else: 
                i=i+1
        return i

def s(num):
    sd=0
    while(num !=0):
        sd+=num % 10
        num=num // 10
    return sd

print(f(9))

