'''
Created on 2024. 8. 12.

@author: user
'''

import numpy as np

a = 100
print(a)
print(type(a))

arr1 = [1,2,3,4]
print(arr1)
print(type(arr1))

arr2 = [[1,2,3,4],[5,6,7,8]]
print(arr2)
print(type(arr2))

b = np.array(200)
print(b)
print(type(b))
print(b.ndim) # 차원
print(b.shape) # 형태
print()

b = np.array([1,2,3])
print(b)
print(type(b))
print(b.ndim) # 차원
print(b.shape) # 형태
print()

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))
print(b.ndim) # 차원
print(b.shape) # 형태
print(b.shape[0]) # 행의 갯수
print(b.shape[1]) # 열의 갯수
print(b[0][1])
print()

for i in range(0, b.shape[0]) :
    for j in range(0, b.shape[1]) :
        print(b[i][j], end = " ")
    print()
    
    
b = np.array([[1,2,3]])
print(b)
print(type(b))
print(b.ndim) # 차원
print(b.shape) # 형태
print()    
    
c = np.arange(6).reshape([3,2])
print(c)
print(type(c))    
print('-----------------------------')

arr = np.array([1.57, 2.48, 3.93, 4.33])
print('arr:', arr)

result = np.sum(arr)
print(result)

result = np.max(arr)
print(result)    
    
result = np.average(arr)
print(result)     
    
result = np.ceil(arr)
print(result)      
    
result = np.floor(arr)
print(result)     

result = np.round(arr)
print(result)   

result = np.round(arr, 1)
print(result) 

result = (np.sum(arr), np.min(arr), np.mean(arr))
print(result) 

arr = np.array([1.57, 2.48, 3.93, 4.33])
arr2 = np.array([1.57, -2.48, 3.93, -4.33])

result = np.maximum(arr,arr2)
print(result)

result = np.equal(arr,arr2)
print(result)
