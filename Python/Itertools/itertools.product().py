# Enter your code here. Read input from STDIN. Print output to STDOUT
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
res=[]
for i in l:
    for j in l1:
        res.append((i,j))

for i in range(0,len(res)):
    print(res[i],end=" ")
