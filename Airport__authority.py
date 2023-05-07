n = int(input())
lst = []
c = 0
for i in range(n):
    lst.append(int(input()))
t = int(input())
for i in lst:
    if i>t:
        c += 2
    elif i <= t:
        c += 1
print(c)