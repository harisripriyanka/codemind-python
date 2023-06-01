n = int(input())
l = list(map(int,input().split()))
c = 0
for i in range(n):
    for j in range(n):
        if i!=j and l[i]==l[j] and l[i]!=-1:
            l[j]=-1
for i in range(n):
    if l[i]%2!=0:
        if l[i]!=-1:
            c = c+1
print(c)
    