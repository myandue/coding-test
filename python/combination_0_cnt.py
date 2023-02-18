import sys
def zero(x,y):
    cnt=0
    j=1
    while 5**j <= x:
        tmp = 5**j 
        for i in range(y, x+1):
            if i%tmp==0:
                cnt+=1
        j+=1
    return cnt
n, m = map(int, sys.stdin.readline().split())
if n-m<m:
    m=n-m
print(zero(n, n-m+1)-zero(m, 1))
