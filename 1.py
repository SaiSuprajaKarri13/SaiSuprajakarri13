n=int(input())
sign='-' if n <0 else ''
n=abs(n)
if n<3:
    print(str(n))
s=''
while n!=0:
    s=str(n%3)+s
    n=n//3
print(sign+s)
