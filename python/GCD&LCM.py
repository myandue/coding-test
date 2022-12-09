x,y=map(int,input().split())
num=[]
i=2
while i<=min(x,y):
    i=2
    while i<=min(x,y):
        if x%i==0 and y%i==0:
            num.append(i)
            x/=i
            y/=i
            break;
        else:
            i+=1
gcd=1
for i in num:
    gcd*=i
print(gcd)
print(int(gcd*x*y))