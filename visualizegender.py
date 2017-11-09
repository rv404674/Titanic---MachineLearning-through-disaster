import pandas as pd
import matplotlib.pyplot as plt

female_color="#FA0000"

df=pd.read_csv("train.csv")
fig=plt.figure(figsize=(18,6))

#total no of survived and not survived person
plt.subplot2grid((3,4),(0,0))
df.Survived.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Survived 1-Yes 0-No")

#no of survived men
plt.subplot2grid((3,4),(0,1))
df.Survived[df.Sex=='male'].value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title("Men Survived")

#no of women survived
plt.subplot2grid((3,4),(0,2))
df.Survived[df.Sex=='female'].value_counts(normalize=True).plot(kind='bar',alpha=0.5,color=female_color)
plt.title("Women Survived")

#sex of survived
plt.subplot2grid((3,4),(0,3))
df.Sex[df.Survived==1].value_counts(normalize=True).plot(kind='bar',alpha=0.5,color=[female_color,'b'])
plt.title('Sex of Survived')

#kde between class and survived
plt.subplot2grid((3,4),(1,0),colspan=4)
for x in [1,2,3]:
    df.Survived[df.Pclass==x].plot(kind="kde")
plt.title("class wrt survived")
plt.legend(("1st","2nd","3rd"))

#rich men survived
plt.subplot2grid((3,4),(2,0))
df.Survived[ (df.Sex=='male') & (df.Pclass==1) ].value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title("Rich men survived")

#poor men survived
plt.subplot2grid((3,4),(2,1))
df.Survived[ (df.Sex=='male') & (df.Pclass==3)].value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title("Poor men survived")


#rich women died
plt.subplot2grid((3,4),(2,2))
df.Survived[ (df.Sex=='female') & (df.Pclass==1)].value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title("Rich women died")


#poor women died
plt.subplot2grid((3,4),(2,3))
df.Survived[ (df.Sex=='female') & (df.Pclass==3)].value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title("Poor women died")









        
























plt.show()


