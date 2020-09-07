n=int(input())
l=set(map(int,input().split()))
m=int(input())
l1=set(map(int,input().split()))
l2=l^l1
print(len(l2))
