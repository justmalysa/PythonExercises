import random

random.seed()
maximum = 100
vector = []

for i in range(0,50):
    vector.append(random.random()*maximum)

def sort_func(vector):
    size = len(vector)
    for i in range (size):
        for j in range(i+1, size):
            if vector[i] < vector[j]:
                pass
            else:
                n = vector[i]
                vector[i] = vector[j]
                vector[j] = n

sort_func(vector)
print(vector)
