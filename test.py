import numpy as np
import seaborn as sns
import pandas as pd

my_lst1=[1,2,3,4,5]
my_lst2=[3,4,5,6,7]
my_lst3=[4,5,6,7,8]

arr=np.array([my_lst1,my_lst2,my_lst3])

# print (arr)
# print(arr.shape)
# print(arr.reshape(5,3))

# arr1= arr[1:2,1:4]
# print(arr1)


arr=np.arange(0,10)  .reshape(5,2)
print(arr)

arr1=arr
arr1[3:6]=500
print(arr1)
print(arr)

rndm=np.random.randn(4,4)
print (rndm)


# rst= sns.displot(pd.DataFrame(rndm ))
# print (rst)

rsult=np.random.randint(0,10,1)
print(rsult)