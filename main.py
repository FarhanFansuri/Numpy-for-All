import numpy as np
import math

# initialization

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='int16')
b = np.array([[4, 5, 6], [7, 8, 9]])
c = np.array([[[1, 2, 3], [11, 12, 13]], [[111, 23, 21], [65, 34, 76]]])

# get dimension of array
a_dim = a.ndim
b_dim = b.ndim

# get the shape
a_shape = a.shape
b_shape = b.shape

# get data type
a_dtype = a.dtype
b_dtype = b.dtype

# get size
a_itemsize = a.itemsize
b_itemsize = b.itemsize

# get the number of items
a_items = a.size
b_items = b.size

# total memory
a_total = a.nbytes
b_total = b.nbytes

# # get a specific element [a,b,...,n-dimension]
# print(a[2])

# # get a specific row [n,:]
# print(b[1, :])

# # get a specific column [:,n]
# print(b[:, 1])

# # get elements with steps
# print(a[1:-1:2])

# # # change elements
# # a[5] = 100
# print(b)
# b[:, 1] = [100, 200]
# print(b)

# arange
d = np.arange(10, 0, -1)
e = np.arange(0, 21, 2)
f = np.arange(11)

# linspace
g = np.linspace(0, 100, 5)

# convert data type
h = g.astype('int16')

# string array
i = np.array(['hello world'])

# zeros and ones
j = np.zeros((2, 3))
k = np.ones((2, 3))

# full
l = np.full((2, 3), 21)

# random
m = np.random.rand(2, 4)*10

# random integer
n = np.random.randint(1, 5, size=(2, 3))

# identity
o = np.identity(4, dtype='int16')

# cosinus
p = np.array([0])
p_2 = np.sin(p)

# np.matmul
q_1 = np.array([[1, 2, 3], [4, 5, 6]])
q_2 = np.array([[1, 4], [2, 5], [3, 6]])
q = np.matmul(q_1, q_2)
q_r = q_1 @ q_2

# determinnat
r = np.array([[1, 2, 21], [4, 12, 6], [7, 8, 9]])
r_det = np.linalg.det(r)

# min and max
s_min = np.min(r)
s_max = np.max(r)

# # output
# print(a)
# print(b)
arr = np.array([[1, 2, 3], [4, 5, 6]])
total_rows = np.sum(arr, axis=0)  # Menjumlahkan kolom (axis=0)
total_columns = np.sum(arr, axis=0)
print(q)
