import random
import numpy as np

random.seed()
maximum = 100
matrix = []
det = 0

for i in range(0,7):
    matrix.append([])
    for j in range(0,7):
           matrix[i].append(random.random()*maximum)

det = np.linalg.det(matrix) 

print(matrix)
print(det)
