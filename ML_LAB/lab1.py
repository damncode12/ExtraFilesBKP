"""
# 1. Install Numpy
# 2. Check the Numpy version installed
"""

"""
3. Create 1-D Array in numpy
"""
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)

"""
4. Use list to create 1D array (you may also specify data type i.e. dtype=’int16’)
"""
b = np.array([1, 2, 3, 4, 5], dtype='int16')
print(b)
"""
5. User tuple to create 1D array
"""
c = np.array((1, 2, 3, 4, 5))
print(c)
"""
6. Use arange function to create 1D array of int
"""
d = np.arange(1, 10)
print(d)
"""
7. Use arange function to create 1D array of float ( may use dtype = symbols(int->‘i’, uint-
>’u’,float->’f’,double->’d’,complex->’D’,bool->’b’)
"""
e = np.arange(1, 10, dtype='f')
print(e)
"""
8. Create 1D array of mixed elements int and float, and print the array and see the output
"""
f = np.array([1, 2, 3, 4, 5, 6.0])
print(f)
"""
9. Create 1D array of mixed elements int, float, and str, then print the array and see the
output
"""
g = np.array([1, 2, 3, 4, 5, 6.0, 'a'])
print(g)
"""
10. Create a 2D array of dimensions 2x2
"""
h = np.array([[1, 2], [3, 4]])
print(h)
"""
11. Print the shape, size, and memory used by this array in bytes (use itemsize, or nbytes)
"""
print(h.shape)
print(h.size)
print(h.itemsize)
print(h.nbytes)
"""
12. Check the type of any array variable
"""
print(type(h))
"""
13. Check indexing on array with help of examples
"""
print(h[0, 0])
print(h[0, 1])
print(h[1, 0])
"""
14. Using arange function create an 3D array of dimensions = (2,3,4) , first element of this
array is 0 and last element is 23 in increasing order, store this array in a variable b.
"""
i = np.arange(24).reshape(2, 3, 4)
print(i)
"""
15. What index can produce output:
array([[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11]])
"""
print(i[0, :, :])
"""
16. What index can produce output: 0
"""
print(i[0, 0, 0])
"""
17. What index can produce output: array([4, 5, 6, 7])
"""
print(i[0, 1, :])
"""
18. What index can produce output: array([0,12])
"""
print(i[:, 0, 0])
"""
19. What index can produce output: array([4,6])
"""
print(i[0, 1, 0::2])
"""
20. Check the output of b[… , 1]
"""
print(i[..., 1])
"""
21. What index can produce output: array( [1, 5, 9] )
"""
print(i[0, :, 1])
"""
22. What index can produce output: array([3,7,11])
"""
print(i[0, :,3])
"""
23. What index can produce output: array([11, 7,3])
"""
print(i[0, :,3][::-1])
"""
24. What index can produce output: array([3,11])
"""
print(i[0, :3][::2])
"""
25. Use function ravel() with array b, and observe the output
"""
print(i.ravel())
"""
26. Use function flatten() with array b, and observe the output
"""
print(i.flatten())
"""
27. Use function transpose() with array b, check the output
"""
print(i.transpose())
"""
28. Use function T() with array b, check the output
"""
print(i.T)
"""
29. Use function concatenate on two 2-D arrays with axis 0, and axis 1 and observe the
output: i.e np.concatenate((arr1,arr2),axis=0) & np.concatenate((arr1,arr2),axis=1)
"""
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
print(np.concatenate((arr1, arr2), axis=0))
print(np.concatenate((arr1, arr2.T), axis=1))
"""
30. Use function astype() to convert the array to an array on another type
A=array([[0, 1], [2, 3],[4, 5]])
A.astype(float) or A.astype(‘f’) or A.astype(‘float64’)
A.astype(bool)
"""
A = np.array([[0, 1], [2, 3], [4, 5]])
print(A.astype(float))
print(A.astype(bool))
"""
31. Check the output of “ np.eye(3)” and “np.zeros(3)”
"""
print(np.eye(3))
print(np.zeros(3))
"""
32. Find minimum, maximum, and average of an array
"""
print(np.min(A))
print(np.max(A))
print(np.average(A))
"""
33. Find matrix multiplication use dot function
"""
B=np.array([[1,2],[3,4]])
print(np.dot(A, B))
"""
34. Find element wise multiplication of two matrices using multiply function
"""
print(np.multiply(A, A))


arr=np.arange(9).reshape(1,3,3)
print(arr[0, :,0][0],arr)


ds=np.arange(25).reshape(5,5)
print(ds)
print(ds.flatten()[::(ds.shape[0]+1)])
print()
print(ds[:,::-1].flatten()[::(ds.shape[0]+1)])

