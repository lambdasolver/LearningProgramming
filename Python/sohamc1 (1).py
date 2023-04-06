num=int(input())
vals=list(map(int,input().split()))
maxbreak=[vals[0]]
for i in range(1,num):
    max=vals[i]
    for j in range(i):
        if max < maxbreak[j] + vals[i-1-j]:
            max = maxbreak[j] + vals[i-1-j]
    maxbreak.append(max)
print(maxbreak[num-1])