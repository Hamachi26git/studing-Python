n = int(input("2以上の自然数n＞"))
count=0

for i in range(2, n):
        for j in range(2, i):
                if i%j == 0:
                        break
        else:
                print(i, end=' ')
                count+=1
print("")
print(n,"までの素数は",count,"個です。")
