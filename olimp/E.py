n=int(input())
a=input()
a=a.split()
for i in range(n):
    a[i]=int(a[i])
soni=0
for i in range(n):
    c=a[i+1:n]
    soni+=c.count(a[i])

print(soni)