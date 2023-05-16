n = int(input())
m = 0
while n > 0:
    dig = n%10
    if m < dig:
        m = dig
    n = n//10
print(m)