import pandas as pd
import utils

'''This predictiontocsv is created by me'''
import predictiontocsv
from sklearn import linear_model, preprocessing,model_selection

train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

utils.clean_data(train)
utils.clean_data(test)


target=train['Survived'].values
features=train[['Age','Sex','Pclass','Fare','Embarked','Parch','SibSp']].values

print 'using logistic regression'
classifier=linear_model.LogisticRegression()
#classifier_=classifier.fit(features,target)

test_features=test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

print 'use logistic regression with polynomial features'
'''Use polynomial features'''

poly=preprocessing.PolynomialFeatures(degree=2)
poly_features=poly.fit_transform(features)

classifier=linear_model.LogisticRegression(C=10)
classifier.fit(poly_features, target)
print classifier.score(poly_features, target)

scores=model_selection.cross_val_score(classifier,poly_features,target,scoring='accuracy',cv=100)
print scores

print 'average after 100 runs'
print scores.mean()

print 'output results of logregression on train.csv in a csv file'
test_features_=poly.fit_transform(test_features)
predictiontocsv.write_prediction(classifier.predict(test_features_), "logisticregprediction.csv")
















