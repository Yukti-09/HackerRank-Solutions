# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for i in range(0,n):
    l.append(input())
l=set(l)
print(len(l))    
