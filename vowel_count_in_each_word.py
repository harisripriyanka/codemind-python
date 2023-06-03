n = input()
a = n.split()
b = "aeiouAEIOU"
for i in a:
    c = 0
    for j in range(len(i)):
        if i[j] in b:
            c += 1
    print(c,end=" ")
