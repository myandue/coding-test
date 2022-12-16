import sys
put=sys.stdin.readline
n=int(put())
li=[]
ans=[]
for i in range(n):
    x,y=map(int,put().split())
    li.append([x,y])
for j in li:
    x,y=j[0], j[1]
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
    ans.append(int(gcd*x*y))
print(*ans, sep='\n')