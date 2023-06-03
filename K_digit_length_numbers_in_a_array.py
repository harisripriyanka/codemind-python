n,k = map(int,input().split())
l = list(map(int,input().split()))
c = 0
for i in l:
    x = str(i)
    p = len(x)
    if(i < 0):
        p -= 1
    if (p==k):
        c += 1
print(c)
        