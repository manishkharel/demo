import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['column1','column2','column3','column4'])
rst=df.head()
print(rst)

asd=df.to_csv('test1.csv')
print(asd)