import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('train.csv')
fig=plt.figure(figsize=(80,30))
#print df.shape
#print df.count()

#figure1- shows passengers survived with passengers id
#plt.subplot2grid((2,3),(0,0))
#df['Survived'].plot()
#plt.title('survived  with id')
##plt.show()

#figure2- in percentage how many survived
plt.subplot2grid((2,3),(0,0))
df.Survived.value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title('1-Survived, 0-not survived')
#plt.show()

#figure3 - shows relationship between age and survived
plt.subplot2grid((2,3),(0,1))
plt.scatter(df.Survived,df.Age,alpha=0.1)
plt.title('Age wrt survived')

#shows relationship b/w passengers and class
plt.subplot2grid((2,3),(0,2))
df.Pclass.value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title('class 1-richest 3-poorest')


#kernel density estimation bw class and passengers age
plt.subplot2grid((2,3),(1,0),colspan=2)
for x in [1,2,3]:
    df.Age[df.Pclass==x].plot(kind="kde")
plt.title("class wrt to Age")
plt.legend(("1st","2nd","3rd"))

plt.subplot2grid((2,3),(1,2))
df.Embarked.value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title("boarding point")
#S-southampton (england) C-cherbourg (france)  Q-queenstown(Ireland)

plt.show()


