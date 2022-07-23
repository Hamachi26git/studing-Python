import random

n = list([random.randint(1,100) for i in range(20)])
print(n)

G = list(n[0::2])
print("偶数：",G)

K = list(n[1::2])
print("奇数：",K)

Slist = []
for s in n:
    Slist.append(s)
    for Nm in range(2, s):
        if s % Nm == 0:
            break
print("素数：",Slist)
