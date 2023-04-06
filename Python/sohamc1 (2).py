class node:    # each binomial trees
    def __init__(self,val=None):
        self.val=val
        self.deg=0
        self.parent=self.left=self.bro=None     #bro is just fancy way to say sibling lol

class beap:   #bheap= array of root nodes
    def link(self,b1,b2):  #link 2 trees
        if b1.val<=b2.val:   # minheap property
            temp=b1.left
            b1.left=b2
            b2.bro=temp
            b1.deg+=1
            b2.parent=b1
            return b1
        else: return self.link(b2,b1)   
    def adjust(self,bheap,unindex):                                         # adjust by merging trees of same degrees
        x=0
        next=1
        nexx=2
        bp=[]
        n=len(bheap)
        if n==0:return bp
        while x<n:
            if x==n-1:                                                      # reched the end of the array
                bp.append(bheap[x])
                x+=1
                next+=1
                nexx+=1
            elif bheap[x].deg!=bheap[next].deg :                            # current and next have different degree
                bp.append(bheap[x])
                x+=1
                next+=1
                nexx+=1
            else:                                                           # current and next have same degree
                if nexx<n and bheap[x].deg==bheap[nexx].deg:                # next.next also has same degree
                    bp.append(bheap[x])
                    x+=1
                    nexx+=1
                    next+=1
                else:                                                       # next.next is different degree
                    if unindex[next]>=unindex[x]:
                        bheap[next]=self.link(bheap[x],bheap[next])
                        unindex[next]=1
                    if unindex[next]<unindex[x]:
                        bheap[next]=self.link(bheap[next],bheap[x])
                        unindex[next]=1  
                    x=next
                    next=x+1
                    nexx=next+1
        
        for j in range(len(bp)-1):
                bp[j].bro=bp[j+1]
        bp[len(bp)-1].bro=None
        return bp
    def union(self,bheap1,bheap2):   #union of 2 bheaps
        n1=len(bheap1)
        n2=len(bheap2)
        i,j=0,0
        bheap=[]
        l=[]
        while i<n1 and j<n2:
            if bheap1[i].deg<=bheap2[j].deg:
                bheap.append(bheap1[i])
                l.append(0)
                i+=1
            else:
                bheap.append(bheap2[j])
                l.append(2)
                j+=1
        while i<n1:
            bheap.append(bheap1[i])
            l.append(0)
            i+=1
        while j<n2:
            bheap.append(bheap2[j])
            l.append(2)
            j+=1
        return self.adjust(bheap,l)

    def insert(self,bheap,val):
        temp=[node(val)]
        if bheap==None: return temp
        if bheap==[]:return temp
        return self.union(bheap,temp)

    def findmin(self,bheap):
        return min([x.val for x in bheap])   #find minimum of values of the roots in array

    def extractmin(self,bheap):
        bp1=[]
        bp2=[]
        m=self.findmin(bheap)
        c=0    #flag for first occurance of minimum
        for i in range (len(bheap)):
            if m==bheap[i].val and c==0:    
                c+=1
                x=bheap[i].left
                while x:     #pull up all siblings of leftchild of min
                    x.parent=None
                    bp1.append(x)
                    #print(x.deg)
                    x=x.bro
            elif c==1 or m!=bheap[i].val:
                bp2.append(bheap[i])
        bp1.sort(key=lambda x:x.deg)
        return (m,self.union(bp2,bp1))    #returns minimum and final bheap after deletion of min.
    def display(self,head):           #display the heap
        while head:
            print(head.val,end=' ')
            self.display(head.left)
            head=head.bro

n=int(input())      #number of input
bhp=beap()
bh=[]
a=[]
for i in range(n):
    x = input()

    if x[0]=="I": #next line should contain a single integer to be added to heap
        x1,y=x.split()
        bh= bhp.insert(bh,int(y))
    if x[0]=="D":          #extracts minimum
        if len(bh)==0:
            continue
        m,bh= bhp.extractmin(bh)
    if x[0]=="M":      #prints minimum
        if len(bh)==0:
            a.append("None")
            continue
        a.append(bhp.findmin(bh))
    if x[0]=="H":           #next line should contain 2 integers , first integer decreased to 2nd
        s = 0
        for x in range(len(bh)):
            s += bh[i].val*bh[i].deg
        a.append(s)
for i in a:
    print(i)
