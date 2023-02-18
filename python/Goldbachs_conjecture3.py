import sys, math

range_n = 1000000
prime = [True]*(range_n+1)
for i in range(2, math.floor(math.sqrt(range_n))):
    if prime[i]==True:
        for j in range(2*i, range_n+1, i):
            prime[j]=False

li=[]
ans=[]
while True:
    x=int(sys.stdin.readline())
    if x==0:
        break
    li.append(x)
for i in li:
    j=2
    while True:
        if j>=i:
            ans.append(-1)
            break
        if prime[i-j]:
            ans.append([i, j, i-j])
            break
        else:
            if j==2:
                j+=1
            else:
                while True:
                    j+=2
                    if prime[j]:
                        break
for i in ans:
    if i==-1:
        print("Goldbach's conjecture is wrong.")
    else:
        print(i[0], '=', i[1], '+', i[2])