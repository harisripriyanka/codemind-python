n = int(input())
lst = list(map(int,input().split()))
a = []
for i in lst:
    if lst.count(i)==1:
        a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(max(a))