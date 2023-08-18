def sample_function(data):
    return ((data+2)*4)

class Sample_Class:
    def __init__(self,data1,data2):
        self.data1 = data1
        self.data2 = data2

    def methos(self):
        return(self.data1+ self.data2)

import numpy as np
import pandas as pd

sample_array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

b = np.arange(1,6,1)
c = np.arange(0.1, 0.8,0.2)
d = np.tile("A", 5)
e = np.tile(0,4)
f = np.zeros(4)
g = np.zeros([2,3])
h = np.ones(3)
i = np.array([1,2,3,4,5])

df = pd.DataFrame({
    'col1' : i,
    'col2' : i*2,
    'col3' :["A","B","C","D","E"]
})

df_1 = pd.DataFrame({
    'col1': np.array([1,2,3]),
    'col2': np.array(["A","B","C"])
})
df_2 = pd.DataFrame({
    'col1': np.array([4,5,6]),
    'col2': np.array(["D","E","F"])
})
