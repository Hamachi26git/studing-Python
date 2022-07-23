n = int(input("正の整数n= "))
i=1
ans=1
while(i<n):
    ans += ans * i
    i += 1
print("1から",n,"までの階乗=",ans)