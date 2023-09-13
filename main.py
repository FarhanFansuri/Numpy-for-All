import numpy as np

# initialization

a = np.array([1, 2, 3], dtype='int16')
b = np.array([[4, 5, 6], [7, 8, 9]])

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

# get a specific element [a,b,...,n-dimension]
print(a[2])

# # output
# print(a_total)
# print(b_total)
