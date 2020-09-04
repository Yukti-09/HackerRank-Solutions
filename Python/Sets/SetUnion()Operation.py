# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=set(map(int,input().split()))
m=int(input())
l1=set(map(int,input().split()))
print(len(l.union(l1)))
