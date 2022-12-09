s=input()
ans=[]
i,l=0,len(s)
while i<l:
    ans.append(''.join(s[i:l]))
    i+=1
ans.sort()
for i in ans:
    print(i)