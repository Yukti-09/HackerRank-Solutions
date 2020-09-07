n=int(input())
l=[]
for _ in range(n):
    l.append(input())
ans=[]
for st in l:
    upper=0
    digits=0
    check="Invalid"
    l1=len(st)
    if l1==10:
        if st.isalnum()==True:
            if len(set(st))==l1:
                for i in st:
                    if i.isdigit()==True:
                        digits+=1
                    if i.isupper()==True:
                        upper+=1
                if digits>=3 and upper>=2:
                    check="Valid"
    ans.append(check)
for i in ans:
    print(i)                            
