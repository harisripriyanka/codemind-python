n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m = []
for i in range(n):
    if l[i]<a or l[i]>b: 
        m.append(l[i])
r = []
for i in l:
    if i  not in m:
        r.append(i)
print(sum(r))