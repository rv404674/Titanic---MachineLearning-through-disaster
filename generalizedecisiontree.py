import pandas as pd
import predictiontocsv
import utils
from sklearn import tree, model_selection

train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

print ('cleaning some data')

utils.clean_data(train)
utils.clean_data(test)

print ('extract target and features')
target=train['Survived'].values
feature_names=['Pclass','Age','Sex','Fare','Embarked','SibSp','Parch']
features=train[feature_names].values


generalized_tree=tree.DecisionTreeClassifier(
        random_state=1,
        max_depth=7,
        min_samples_split=2
        )

generalized_tree_=generalized_tree.fit(features,target)
#print generalized_tree_.score(features, target)

#print generalized_tree_.feature_importances_
print ('score on first iteration on training set of generalized decision tree', generalized_tree_.score(features,target) )

scores=model_selection.cross_val_score(generalized_tree, features, target, scoring='accuracy',cv=50)

print (scores)
print ('after 50 runs average')
print (scores.mean())

print ('writing new prediction in a csv file')
test_features=test[[ 'Pclass','Age','Sex','Fare','SibSp','Parch','Embarked']].values
prediction=generalized_tree.predict(test_features)

predictiontocsv.write_prediction(prediction,"generalizedtreepredcition.csv")
























