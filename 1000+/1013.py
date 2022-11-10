s = input()
s = s.split()
n = int(s[0])
k = int(s[1])
s = input()
s = s.split()
soni = 0
for i in range(k):
    s.append(s[i])
i = 0
while i < n:
    t = False
    if s[i] == '1':
        t = True
        for j in range(1, k):
            if s[i + j] == '0':
                t = False
                break
    if t:
        print(s[i:i+k])
        soni += 1;
        i += k
    else:
        i += 1

print(soni)
