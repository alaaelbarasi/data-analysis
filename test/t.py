import numpy as np
import pandas as pd
df=pd.DataFrame(np.arange(0,20).reshape(5,4), index=['row1','row2','row3','row4','row5'], columns=['1','2','3','4'])
print(df.head())
df.to_csv('test1.csv')