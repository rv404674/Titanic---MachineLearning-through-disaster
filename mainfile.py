import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')

import pandas as pd
web_stats={ 'Day':[1,2,3,4,5,6],'Visitors':[43,34,65,56,29,76],
             'Bounce_Rate':[65,67,78,65,45,52] }
df=pd.DataFrame(web_stats)

#print (df.head())
#print (df.tail(2))

#df=df.set_index('Day')
df.set_index('Day',inplace=True)
#print df

#print (df.Visitors)
#print (df['Visitors'])


#df['Visitors'].plot()
#plt.show()

#df.plot()
#plt.show()

#print(df[['Visitors','Bounce_Rate']])
print (df['Visitors'].tolist())
print (df[['Visitors',



