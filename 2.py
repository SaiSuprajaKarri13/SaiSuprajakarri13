s1=input()
s2=input()
c=s2[-1]
def count(s1,c):
    res=0
    for i in range(len(s1)):
        if(s1[i]==c):
            res=res+1
    return res
print(count(s1,c))
