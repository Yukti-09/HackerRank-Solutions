# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l1=[]
l2=[]
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
count=0
for i in l1:
    if i in l2:
        count+=1
print(count)
