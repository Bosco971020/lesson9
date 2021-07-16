a=1#0,1,1,2,3,5,8,
b=0

z=int(input('輸入一個值'))
for i in range(z//2):#0,1,2,3..        ans=a+b
        a=a+b
        b=b+a
if z%2==1:
    b=a+b
print(b)