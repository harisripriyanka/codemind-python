n = int(input())
l = list(map(int,input().split()))
a = 0
b = 0
for i in range(0,n//2):
    a = a+l[i]
print(a)
for i in range(n//2,n):
    b = b+l[i]
print(b)

    