n = int(input())
lst = list(map(int,input().split()))
ex = int(input())
for i in lst:
    k = i+ex
    if max(lst)<=k:
        print(True,end=" ")
    else:
        print(False,end=" ")