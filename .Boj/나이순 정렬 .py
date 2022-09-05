from sys import stdin

m=int(stdin.readline().strip())

age=[]

for i in range(m):
    input_data=stdin.readline().strip().split()
    age.append((int(input_data[0]),input_data[1]))

new_age=sorted(age,key=lambda x:(x[0]))

for j in new_age:
    print(j[0], end=' ')
    print(j[1])