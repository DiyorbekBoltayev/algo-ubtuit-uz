t=int(input())
a=[]
b=[]
javob=[]
for i in range(t):
    a.append(input())
    b.append(input())


for i in b:

    n=len(i)
    m=[]
    for j in range(2**n):
        m.append(bin(j)[2:].zfill(n))
    satrlar=[]
    for j in m:
        satr=""
        for k in range(n):
            if j[k]=='1':
                if satr.find(i[k])==-1:
                    satr+=i[k]
        satrlar.append(satr)

    javob.append(max(satrlar))

for i in javob:
    print(i)



