# Enter your code here. Read input from STDIN. Print output to STDOUT
st=input()
s=""
l=[]
l1=[]
l2=[]
l3=[]
for i in st:
    if i.islower()==True:
        l.append(i)
for i in st:
    if i.isupper()==True:
        l1.append(i)
for i in st:
    if i.isdigit()==True:
        if int(i)%2!=0:
            l2.append(i)
        else:
            l3.append(i)
l.sort()
l2.sort()
l1.sort()
l3.sort()
for i in l:
    s+=i
for i in l1:
    s+=i
for i in l2:
    s+=i
for i in l3:
    s+=i    
print(s)                    
