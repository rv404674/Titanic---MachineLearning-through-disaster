def clean_data(data):
    #fill all empty fare rows with median of fare
    data["Fare"]=data["Fare"].fillna(data["Fare"].dropna().median())
    data["Age"]=data["Age"].fillna(data["Age"].dropna().median())
     
     #for female-1 for male-0
    data.loc[data.Sex=='male',"Sex"]=0
    data.loc[data.Sex=='female',"Sex"]=1

    #similarly fill for boarding points    
    data.Embarked=data.Embarked.fillna("S")
    data.loc[data.Embarked=="S","Embarked"]=0
    data.loc[data.Embarked=="C","Embarked"]=1
    data.loc[data.Embarked=="Q","Embarked"]=2






















