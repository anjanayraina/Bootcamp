import numpy as np

print(np.abs(-10))
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr)
arr2 = np.array([[-1, -2, -3], [1,2,3],[4,5,6]])
print(arr2)
print(arr.ndim)
print(arr2.ndim)
arr3 = np.array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10, 11 , 12]] ])
print(arr3)
print(arr3.ndim)
print(arr3[1][1][1])
print(arr3[0] + arr3[1])

arr2 = [[1,2,3] , [4,5,6]]
print(arr2[0][1])
print(arr[1:4:2]) # slicing takes in 3 parameters start , end and step and the end index insnt included in the slice , so for a slice of 1:5 will always go till the 4th index
print(arr[:4])

str_array = np.array([1,2,3,4] ,dtype= 'S') # this will typecast the array to string
print(str_array)
print(str_array.dtype) # S1 is the string datatype
print(arr3.shape)
arr4 = np.arange(0 , 10)
print(arr4)
arr4 = arr4.reshape(2,5 )
print(arr4)

temp1  = np.array([1,2,3])
temp2 = np.array([4,5,6])
# print(np.concatenate(temp1 , temp2))
print(np.zeros((10,2)))
print(np.array([1,2,3,4] , dtype = float))
print(len(arr3))
print(np.linspace(2 , 10 , 6)) # arange takes in the step whereas linspace takes in the total count of values to genereate


print(np.arange(10) + np.arange(10))

indices = np.where(arr > 2) # this returns the indices of the values that are greater than 2 in the array
print(indices)
# this can also be used as a ternary operator

print(np.where(arr > 3 , "Greater" , "Lesser")) #so the values that are greater than 3 will return greater and the others will return lesser

temp1 = np.array([[1,2 , 3,4,5] , [6,7,8,9,10]])
print(temp1.flatten()) # this makes any n dimensional array into a single dimension array
print(temp1.transpose())

print(temp1[-1 , len(temp1[-1])-3 : len(temp1[-1]) ]) # get the last 3 elements from the last index of the array