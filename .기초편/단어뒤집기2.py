import sys
S=list(sys.stdin.readline().strip())
stack=[]
word=''
while S:
    if S[0]=='<':
        if word!='':
            word=word[::-1]
            stack.append(word)
            word=''
        stack.append(S.pop(0))
        while S[0]!='>':
            stack.append(S.pop(0))
        stack.append(S.pop(0))
    else:
        if S[0]==' ':
            word=word[::-1]
            stack.append(word)
            stack.append(S.pop(0))
            word=''
        elif len(S)==1:
            word+=S.pop(0)
            word=word[::-1]
            stack.append(word)
        else:
            word+=S.pop(0)
stack=''.join(stack)
print(stack)