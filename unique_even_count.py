n = int(input())
l = list(map(int,input().split()))
b = set(l)
s = 0
for i in b:
    if i%2==0 and i!=0:
        s += 1
print(s)