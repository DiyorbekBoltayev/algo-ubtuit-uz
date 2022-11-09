a=[-1,2]
while len(a)<10000000:
    a.append(a[-1]+(a[-1]-a[-2])+2)
n=int(input())
print(a[n])

