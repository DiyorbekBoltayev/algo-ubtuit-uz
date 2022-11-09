n = int(input())
s = input()
a = s.split()
for i in range(len(a)):
    a[i] = int(a[i])
min_indeks = a.index(min(a))
a[min_indeks], a[-1] = a[-1], a[min_indeks]
for i in a:
    print(i,end=" ")
