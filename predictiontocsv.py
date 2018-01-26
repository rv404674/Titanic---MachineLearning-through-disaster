import pandas as pd
import numpy as np

test=pd.read_csv('test.csv')

def write_prediction(prediction,name):
    PassengerId=np.array(test['PassengerId']).astype(int)
    solution=pd.DataFrame(prediction,PassengerId,columns=['Survived'])
    solution.to_csv(name,index_label=['PassengerId'])
