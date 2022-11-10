q = int(input())
m = []
javob=[]
for i in range(q):
    n = int(input())
    a = []
    for j in range(n):
        s = (input())
        s = s.split()
        a.append([int(s[0]), int(s[1])])

    all1 = True

    for j in a:
        soni=0
        for k in a:
            if j[0] == k[0] or j[1] == k[1]:
                soni+=1
        if soni == 1:
            all1 = False
            break

    if all1:
        javob.append("YES")
    else:
        javob.append("NO")

for i in javob:
    print(i)


