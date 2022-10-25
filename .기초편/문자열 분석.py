import sys

while True:
    String=sys.stdin.readline().rstrip('\n')
    if not String:
        break
    big,small,blank,num=0,0,0,0
    for i in String:
        if i.isupper():
            big+=1
        elif i.islower():
            small+=1
        elif i.isdigit():
            num+=1
        elif i.isspace():
            blank+=1

    print(small, big, num, blank) 