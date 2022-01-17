t=int(input())
def sumls(listed):
    sum=0
    for i in listed:
        sum+=i
    return sum
for _ in range(t):
    dmarks=list(map(int,input().split()))
    smarks=list(map(int,input().split()))
    if (sumls(dmarks)> sumls(smarks)):
        print("DRAGON")
    elif (sumls(dmarks)< sumls(smarks)):
        print("SLOTH")
    else:
        if(dmarks[0]>smarks[0]):
            print("DRAGON")
        elif(dmarks[0] < smarks[0]):
            print("SLOTH")
        else:
            if (dmarks[1] > smarks[1]):
                print("DRAGON")
            elif (dmarks[1] < smarks[1]):
                print("SLOTH")
            else:
                print("TIE")
