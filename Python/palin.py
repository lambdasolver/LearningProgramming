
t=list(map(int,input().split()))
boxarr=list(map(int,input().split()))
commands=list(map(int,input().split()))

stacks=t[0]-1
maxbox=t[1]

holds=0
boxes=boxarr[0]
pos=0


# 1
def moveLeft():
    global pos,boxes,boxarr
    if (pos > 0):
        pos = pos-1
        boxes=boxarr[pos]

    else:
        pos = pos

# 2
def moveRight():
    global pos,boxes,boxarr
    if (pos >= stacks):
        pos = pos
    else:
        pos=pos+1
        boxes=boxarr[pos]

# 3
def pickUp():
    global boxes, holds,pos
    if (boxes == 0):
        boxes = boxes
    else:
        if (holds == 1):
            boxes = boxes
        else:
            boxarr[pos]=boxes-1
            holds=1

# 4
def drop():
    global boxes, holds,pos
    if (boxes >= maxbox):
        boxes = boxes
    else:
        if (holds == 0):
            holds = 0
        else:
            boxarr[pos]=boxes+1
            holds=0

# 5
def quit():
    global boxarr
    print(" ".join(list(map(str,boxarr))))

def commandexecute(num):
    if(num ==1): moveLeft()
    elif(num==2): moveRight()
    elif(num==3): pickUp()
    elif(num==4): drop()
    else: quit()

for i in commands:
    commandexecute(i)
