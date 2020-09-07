def solve(s):
    st=""
    st+=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==" ":
            x=s[i].upper()
            st+=x
        else:
            st+=s[i]
    return st
    


