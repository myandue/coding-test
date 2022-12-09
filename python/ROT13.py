s=input()
ans=[]
for i in s:
    if 'A'<=i<='Z':
        tmp=chr(ord(i)+13)
        if tmp>'Z':
            tmp=chr(ord(tmp)-ord('Z')+ord('A')-1)
        ans.append(tmp)
    elif 'a'<=i<='z':
        tmp=chr(ord(i)+13)
        if tmp>'z':
            tmp=chr(ord(tmp)-ord('z')+ord('a')-1)
        ans.append(tmp)
    else:
        ans.append(i)
print(''.join(ans))