from sys import stdin

input_data=stdin.readline().strip()

input_0=input_data.split('1')
input_0=' '.join(input_0).split()
input_1=input_data.split('0')
input_1=' '.join(input_1).split()

print(min(len(input_0),len(input_1)))