m = [[1,2,3],[4,5,6],[7,8,9]]
for row in m:
    print(row)
trns = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print('\n')
for row in trns:
    print(row)
    
    

    
    
import numpy as np

matrix = np.array([[1,2,3],
                  [4,2,6],
                  [7,8,9]])

print('Matrix: ')
print(matrix)
inv_matrix = np.linalg.inv(matrix)

print('\n Inverse of a Matrix')
print(inv_matrix)