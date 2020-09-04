

n = int(input())
if n%2!=0:
    print("Weird")
else:
    for i in range(2,6):
        if n==i:
            print("Not Weird")
       
    for i in range(6,21):
        if n==i:
            print("Weird")
        
    if n>20:
        print("Not Weird")                         
