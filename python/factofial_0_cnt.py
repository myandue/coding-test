import sys
x = int(sys.stdin.readline())
cnt=0
for i in range(1, x+1):
    if i%5==0:
        tmp=i
        while tmp%5==0:
            cnt+=1
            tmp/=5
print(cnt)