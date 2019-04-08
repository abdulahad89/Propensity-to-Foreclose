# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:56:44 2019

@author: Abdul Ahad
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('file:///D:\\Data\\Foreclosure\\Trials\\tr1.csv')
df=df.dropna(axis=0,how='any')
#data=pd.read_csv('D:\Data\Foreclosure\data.csv')
x=df.iloc[:,3:36]
y=df.iloc[:,2].values

from sklearn.preprocessing import LabelEncoder,StandardScaler
le=LabelEncoder()
x['CITY']=le.fit_transform(x['CITY'])
x['PRODUCT']=le.fit_transform(x['PRODUCT'])
x['SEX']=le.fit_transform(x['SEX'])
x['MARITAL_STATUS']=le.fit_transform(x['MARITAL_STATUS'])
x['QUALIFICATION']=le.fit_transform(x['QUALIFICATION'])

Sc=StandardScaler()
x=Sc.fit_transform(x)

var=[]
from sklearn.decomposition import PCA 
for i in range(0,25):
    pca=PCA(n_components=i)
    pca.fit_transform(x)
    var.append(pca.explained_variance_ratio_.sum())
    #print('Explained variance: %.4f' % pca.explained_variance_ratio_.sum())
    
plt.plot(range(0,25),var)
plt.show()

pca1=PCA(n_components=15)
x_pca=pca1.fit_transform(x)

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_pca,y,test_size=0.3,random_state=0)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
    
y_pred=classifier.predict(x_test)
prob=classifier.predict_proba(x_test)
    
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

##################TEST CASE   ########################   
 
test=pd.read_csv('D:\\Data\\Foreclosure\\test.csv')
test=test.drop(columns=['Unnamed: 0'])
x_final=test.iloc[:,[3,6,7,8,9,10,12,13,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,
                     34,39,40,42,43,44,45,46]]
qual=test.iloc[:,45]

x_final['SEX']=x_final['SEX'].fillna('A')
x_final['MARITAL_STATUS']=x_final['MARITAL_STATUS'].fillna('A')
x_final['QUALIFICATION']=x_final['QUALIFICATION'].fillna('A')
x_final=x_final.fillna(0)  #Dropping 0 vals

x_final.isnull().sum()

from sklearn.preprocessing import LabelEncoder,StandardScaler
le=LabelEncoder()
x_final['CITY']=le.fit_transform(x_final['CITY'])
x_final['PRODUCT']=le.fit_transform(x_final['PRODUCT'])
x_final['SEX']=le.fit_transform(x_final['SEX'])
x_final['MARITAL_STATUS']=le.fit_transform(x_final['MARITAL_STATUS'])
x_final['QUALIFICATION']=le.fit_transform(x_final['QUALIFICATION'])

Sc=StandardScaler()
x_final_sc=Sc.fit_transform(x_final)

x_pca_final=pca1.fit_transform(x_final_sc)

y_pred_final=classifier.predict(x_pca_final)
prob_final=classifier.predict_proba(x_pca_final)

p_f=pd.DataFrame({'AGREEMENTID':0,'FORECLOSURE':prob_final[:,1]})
x_final=test.iloc[:,[0,3,6,7,8,9,10,12,13,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,
                     34,39,40,42,43,44,45,46]]
x_final=x_final.fillna(0) 

for i in range(0,120869):
    p_f.iloc[i,0]=x_final.iloc[i,0]

vals=p_f.groupby('AGREEMENTID')['FORECLOSURE'].mean()  #Taking mean of probabilites with same agreement id

vals.to_csv('D:\Data\Foreclosure\Trials\predict_tr2.csv')

#MErging main test set with aour test set values
#Some test cases are missing so we cant predict them so we fill the values with 0.01
t1=pd.read_csv('D:\Data\Foreclosure\Trials\predict_tr2.csv')
t2=pd.read_csv('D:\\Data\\Foreclosure\\test_foreclosure.csv')
t3=pd.merge(t1,t2,on='AGREEMENTID',how='outer')
t3=t3.fillna('0.01')
t3.to_csv('D:\Data\Foreclosure\Trials\predict_t.csv')