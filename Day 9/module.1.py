#2D array creation
array_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)  #print array total
print(array_2d[1,1])  #print a specific element
print(array_2d.ndim)  #show the dimensions
print(array_2d.shape) # show how many rows and columns
print(array_2d.size)  #shows number of elements

array_sub=array_2d[:2,:2]
print(array_sub)
rev_array_sub=array_2d[-2:,-2:]
print(rev_array_sub)
#dsh find other manipulation with numpy


sum=np.sum(array_2d)#find total
print(sum)
mean=np.mean(array_2d)#find mesatare
print(mean)

sum_columns=np.sum(array_2d,axis=0)
print(sum_columns)
