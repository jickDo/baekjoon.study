place=input()
x,y=place[:1],place[1:]
cnt=0
steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

for i in range(steps):
    dx=x+steps[i][0]
    dy=y+steps[i][1]
    if dx<1 or dx>8 or dy<1 or dy>8:
        continue
    else:
        cnt+=1
print(cnt)
    