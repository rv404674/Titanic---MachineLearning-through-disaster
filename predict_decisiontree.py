import pandas as pd
import utils
from sklearn import tree

train=pd.read_csv('train.csv')
utils.clean_data(train)

target=train['Survived'].values
feature_names=['Pclass','Age','Sex','Fare','Embarked','SibSp','Parch']
features=train[feature_names].values


decision_tree=tree.DecisionTreeClassifier(random_state=1)
decision_tree_=decision_tree.fit(features,target)

print 'Suffers with problem of overfitting'
print decision_tree_.score(features,target)


generalized_tree=tree.DecisionTreeClassifier(
        random_state=1,
        max_depth=7,
        min_samples_split=2
        )

generalized_tree_=generalized_tree.fit(features,target)
#used to generate dot file
tree.export_graphviz(generalized_tree_,feature_names=feature_names,out_file="tree.dot")


























