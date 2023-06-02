a,b = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
c = set(l1)
d = set(l2)
m = 0
for i in c:
    for j in d:
        if i==j:
            m += 1
print(m)