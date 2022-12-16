import sys
put=sys.stdin.readline
n=int(put())
li=[]
ans=[]
for i in range(n):
    x,y=map(int,put().split())
    li.append([x,y])
for i in li:
    x,y=max(i[0],i[1]), min(i[0],i[1])
    while y!=0:
        x, y = max(x%y,y), min(x%y, y)
    ans.append(int(i[0]*i[1]/x))
print(*ans, sep='\n')