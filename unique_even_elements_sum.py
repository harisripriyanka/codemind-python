n = int(input())
l = list(map(int,input().split()))
a = set(l)
s = 0
for i in a:
    if i%2==0 and i!=0:
        s += i
print(s)