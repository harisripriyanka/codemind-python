n = int(input())
lst = list(map(int,input().split()))
u = []
for i in lst:
    if lst.count(i) == 1:
        u.append(i)
if len(u)!=0:
    print(*u)
else:
    print(-1)