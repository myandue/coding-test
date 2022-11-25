import sys
input=sys.stdin.readline
s = list(str(input()))
answer=[]
stack=[]

for i in range(len(s)):
    if s[i].isalpha():
        answer.append(s[i])
    else:
        l=len(stack)
        if l==0 or stack[l-1]=='(' or s[i]=='*' or s[i]=='/' or s[i]=='(':
            pass
        else:
            for j in range(l):
                x=stack.pop()
                if x!='(' and x!=')':
                    answer.append(x)
        stack.append(s[i])

print(''.join(answer))