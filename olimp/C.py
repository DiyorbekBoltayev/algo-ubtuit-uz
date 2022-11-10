n = int(input())
if n == 1:
    print(1)
else:
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    b = a.copy()


    def raqam_yigindi(n):
        a = 0
        while n > 0:
            a += n % 10
            n //= 10
        return a

    for i in range(len(a)):
         b[i] = raqam_yigindi(a[i])
    mx = b.index(max(b))

    print(a[mx])
