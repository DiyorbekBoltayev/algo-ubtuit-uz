n = int(input())
s = input()
a = s.split()
for i in range(len(a)):
    a[i] = int(a[i])
yigindi=0
soni=0
for i in a:
    if i%2==1:
        yigindi+=i
        soni+=1
print( "%.2f" %(yigindi/soni))
