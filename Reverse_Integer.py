n = int(input())
t = n
n = abs(n)
s = 0
while(n):
    s = s*10+(n%10)
    n//=10
if(t<0):
    print(s-(2*s))
else:
    print(s)