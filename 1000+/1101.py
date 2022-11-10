n = int(input())
s = input()
a = s.split()
for i in range(len(a)):
    a[i] = int(a[i])
soni=0
for i in a:
    if i%2==1:
        soni+=1
print(soni**2)