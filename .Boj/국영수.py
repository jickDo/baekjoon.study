from sys import stdin

people=int(stdin.readline().strip())
grade=[]

for i in range(people):
    input_data=stdin.readline().strip().split()
    grade.append((input_data[0],int(input_data[1]),int(input_data[2]),int(input_data[3])))

grade.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for j in grade:
    print(j[0])