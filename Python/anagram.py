inpstring=input("Enter a string: ")

def charfreq(string):               # this finds the frequency of the first character in 

    s=''                            # the string and returns a tuple  of a string without 
    i=0                             # all appearance of first character and the frequency 
    for l in string:                # of occurance of the first character
        if (l == string[0]):
            i=i+1
        else:
            s=s+l
    return((s,i))
fqls=[]                             # this list stores the frquencies of all distinct characters
while (inpstring != ''):
    temp=charfreq(inpstring)
    fqls.append(temp[1])            # apply the define function -> add the frequency
    inpstring=temp[0]               #  -> now apply the function again on the returned string
flag = 0                            #  untill the string is empty
for i in fqls:
    if (i != fqls[0]):
        flag = 1
        print("Not Anagram")        # just check if the first element is not equal any where in the list
        break

if (flag==0):
    print("Anagram")
