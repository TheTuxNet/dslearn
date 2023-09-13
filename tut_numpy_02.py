import numpy as np
# Lezionne 2 - Array n dimensioni ********************************

arr0D = np.array(42)
arr1D = np.array([1, 2, 3])
arr2D = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
arr3D = np.array(
    [
        [
            [11, 12, 13],
            [14, 15, 16]
        ],
        [
            [21, 22, 23],
            [24, 25, 26]
        ],
    ]
)

print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

arr5D = np.array([1, 2, 3], ndmin=5)
print(arr5D)
print(arr5D.ndim)

# Generazione array con elementi da range (escuso valore finale) con step indicato
arrArange = np.arange(5, 50, 3)
print(arrArange)

# Generazione array multidimensionale, riepito con 0
arrZeros = np.zeros((3, 2, 4))
print(arrZeros)

# Generazione array multidimensionale, riepito con 1
arrOnes = np.ones((2, 2, 2))
print(arrOnes)
