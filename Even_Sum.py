n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if i%2 == 0:
        a.append(i)
b = sum(a)
print(b)