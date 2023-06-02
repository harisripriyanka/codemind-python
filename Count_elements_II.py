a,b = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
c = set(l1)
d = set(l2)
m = 0
n = 0
for i in c:
    if i not in d:
        m+=1
for j in d:
    if j not in c:
        n+=1
print(m+n)