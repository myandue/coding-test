import sys
input=sys.stdin.readline
s = list(str(input()))
answer=[]
stack=[]

for i in range(len(s)-1):
    if s[i].isalpha():
        answer.append(s[i])
    elif s[i]=='(':
        stack.append(s[i])
    elif s[i]==')':
        while len(stack)!=0:
            x=stack.pop()
            if x=='(':
                break
            answer.append(x)
    else:
        l=len(stack)
        if s[i]=='*' or s[i]=='/':
            if l!=0:
                if stack[l-1] =='*' or stack[l-1]=='/':
                    answer.append(stack.pop())
        else:
            if l!=0:
                while len(stack)!=0:
                    x=stack.pop()
                    if x=='(':
                        stack.append(x)
                        break
                    answer.append(x)
        stack.append(s[i])

l=len(stack)
if l!=0:
    for i in range(l):
        answer.append(stack.pop())
print(''.join(answer))