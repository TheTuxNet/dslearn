# 03 Indicizzazione array
import numpy as np

# Lista standard *******************
lista = [1, 2, 3, 4, 5]
# print(lista)
# print(lista[3])

# Array 1 dimensione ***************
arr1D = np.array([1, 2, 3, 4, 5])
# print(arr1D)
# print(arr1D[3])

# Array 2 dimensioni ***************
arr2D = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# print(arr2D)
# print(arr2D[0, 2])

# Array 3 dimensioni ***************
arr3D = np.array([
    [
        [11, 12, 13], [14, 15, 16]
    ],
    [
        [21, 22, 23], [24, 25, 26]
    ]
])
print(arr3D)
print(arr3D.ndim)
print(arr3D[0, 1, 1])

# Indice negativo *****************
print(arr3D[0, 1, -2])
print(arr3D[-1, -1, -1])
print(arr3D[-1, -2, -2])
