from itertools import product


list = [(1,2,3),(1,2,3),(1,2,3)]
for i in list:
    for y in i:
        print(f"{y}")

for i,y in product(list):
    print(i,y)