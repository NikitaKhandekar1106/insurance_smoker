import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,roc_auc_score,roc_curve

df=pd.read_csv('insurance.csv')
print(df.head())

df.info()

df.isnull().sum()

df['region'].unique()
dummies1=pd.get_dummies(df['region'])
print(dummies1)

df['sex'].unique()

dummies2=pd.get_dummies(df['sex'],drop_first=True)
print(dummies2)

df=pd.concat([df,dummies2,dummies1],axis=1)
print(df)

df.drop(['sex','region'],inplace=True,axis=1)
print(df)

df['smoker']=df['smoker'].replace('yes',1).replace('no',0)
print(df)

df.info()
####################################################################
x=df.drop('smoker',axis=1)
y=df['smoker']
###################################################################
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
logistic_model=LogisticRegression()
logistic_model.fit(x_train,y_train)
####################################################################
print(logistic_model.score(x_train,y_train))
####################################################################
y_pred=logistic_model.predict(x_test)
print(y_pred)
######################################################################
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
#######################################################################
y_pred_prob=logistic_model.predict_proba(x_test)
print(y_pred_prob)
fpr,tpr,threshold=roc_curve(y_test,y_pred_prob[:,1])
print(fpr)
print(tpr)
print(threshold)
#####################################################################
plt.plot(fpr,tpr,label='logistic regression')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.legend(loc='best')
####################################################################
auc_score=roc_auc_score(y_test,y_pred_prob[:,1])
print(auc_score)

#####################################################################
################   DECISION TREE CLASSIFIER  ########################
#####################################################################

dtc_model=DecisionTreeClassifier()
dtc_model.fit(x_train,y_train)

y_pred=dtc_model.predict(x_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
######################################################################
plt.figure(figsize=(15,20))
plot_tree(decision_tree=dtc_model,rounded=True,filled=True,class_names=x.columns)
export_graphviz(dtc_model)

#######################################################################
####################### SAVE MODELS################################
#########################################################################
import pickle
models=[logistic_model,dtc_model]
pickle.dump(models,open('models.pickle','wb'))

import json
columns = {
    'data_columns' : [col.lower() for col in x.columns]
}
with open("columns1.json","w") as f:
    f.write(json.dumps(columns))