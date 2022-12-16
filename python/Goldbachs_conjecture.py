import sys, math

def isPrime(p):
    i=2
    while i<=math.sqrt(p):
        if(p%i==0):
            return False
        i+=1
    return True

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
        if isPrime(i-j):
            ans.append([i, j, i-j])
            break
        else:
            if j==2:
                j+=1
            else :
                while True:
                    j+=2
                    if isPrime(j):
                        break
for i in ans:
    if i[0]==-1:
        print("Goldbach's conjecture is wrong.")
    else:
        print(i[0],'=',i[1],'+',i[2])