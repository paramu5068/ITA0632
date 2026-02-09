import numpy as np

# a
marks = np.array([78,85,90,67,88,76,95,82,70,89])
print("a)", marks, marks.shape, marks.dtype)

# b
arr = np.arange(10,101,10)
print("b)", arr[0], arr[-1], arr[2:7])

# c
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
print("c) Add:", x+y, "Mul:", x*y)

# d
nums = np.array([23,55,67,45,89,12,60,30])
print("d)", nums[nums>50])

# e
print("e)\n", np.arange(1,13).reshape(3,4))
