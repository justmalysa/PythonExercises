import random

random.seed()
maximum = 100
matrix1 = []
matrix2 = []
matrix3 = []

for i in range(0,8):
    matrix1.append([])
    for j in range(0,8):
           matrix1[i].append(random.random()*maximum)

for i in range(0,8):
    matrix2.append([])
    for j in range(0,8):
           matrix2[i].append(random.random()*maximum)

for i in range(0,8):
    matrix3.append([])
    for j in range(0,8):
           matrix3[i].append(0)
           
for i in range(0,8):
    for j in range(0,8):
        for k in range(0,8):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]


print(matrix1)
print(matrix2)
print(matrix3)
