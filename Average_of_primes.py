def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n = int(input())
l = list(map(int,input().split()))
l1 = []
for i in l:
    if(isprime(i)):
        l1.append(i)
r = sum(l1)/len(l1)
print("%.2f"%r)