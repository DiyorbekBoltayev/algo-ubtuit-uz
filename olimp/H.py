s=input()
s=s.split()
k=int(s[0])
n=int(s[1])
def Ball(k,n):
    if k==0:
        return 0
    elif k==1:
        return 1
    else:
        return (Ball(k-1,n)+n-1)%k+1

print(Ball(k,n))