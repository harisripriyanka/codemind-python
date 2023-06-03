n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())
c = []
for i in range(n):
    if l[i]<a or l[i]>b:
        c.append(l[i])
r =[]
for i in l:
    if i not in c:
        r.append(i)
if len(r)==0:
    print('-1')
else:
    print(max(r))