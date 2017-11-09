import pandas as pd
import utils
from sklearn import linear_model

train=pd.read_csv('train.csv')
utils.clean_data(train)

target=train['Survived'].values
features=train[['Age','Sex','Pclass','Fare','Embarked','Parch','SibSp']].values

classifier=linear_model.LogisticRegression()
classifier_=classifier.fit(features,target)

print classifier_.score(features,target)

















