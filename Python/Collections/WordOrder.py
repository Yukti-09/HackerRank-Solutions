# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for _ in range(n):
    l.append(input())
print(len(set(l)))    
d={}
for i in l:
    if i not in d:
        d[i]=0
    d[i]+=1    


for i in d:
    print(d[i],end=" ")    

