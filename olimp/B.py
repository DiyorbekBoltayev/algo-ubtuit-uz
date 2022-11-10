a=input()
b=input()
c=""
for i in range(len(a)):
    if a[i]!=b[i]:
        c+="1"
    else:
        c+="0"
print(c)