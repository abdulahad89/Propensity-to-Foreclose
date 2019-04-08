# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:38:58 2019

@author: Abdul Ahad
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

main=pd.read_excel('D:\\Data\\Foreclosure\\LMS_31JAN2019.xlsx')
df1=pd.read_excel('D:\\Data\\Foreclosure\\Customers_31JAN2019.xlsx')
df2=pd.read_csv('D:\\Data\\Foreclosure\\train_foreclosure.csv')
test=pd.read_csv('D:\\Data\\Foreclosure\\test_foreclosure.csv')

#merging main data   
data=pd.merge(main,df2,on=['AGREEMENTID'],how='inner')  
data=pd.merge(data,df1,on=['CUSTOMERID'],how='inner')

data.to_csv('D:\Data\Foreclosure\data.csv')

#merging test data
data_test=pd.merge(test,main,on=['AGREEMENTID'],how='inner')  
data_test=pd.merge(data,df1,on=['CUSTOMERID'],how='inner')
data_test.to_csv('D:\\Data\\Foreclosure\\test.csv')

#   EDA
y=df1['CUSTOMERID'].unique()
x1=main['AGREEMENTID'].value_counts()
x2=main['CUSTOMERID'].value_counts()
z=df2['AGREEMENTID'].unique()

data=pd.read_csv('D:\Data\Foreclosure\data.csv')
data=data.drop(columns=['Unnamed: 0','Unnamed: 0.1'])
data.isnull().sum()
data.isna().sum()
#(data['PRE_EMI_OS_AMOUNT'] == 0).all()
#CHECKING FOR 0 values in different columns
#To check for different columns change the name of column
os=data[data['BALANCE_EXCESS'] != 0]

#data=data.drop(columns=['Unnamed: 0','PROFESSION','OCCUPATION','POSITION','NPA_IN_LAST_MONTH',
                #   'NPA_IN_CURRENT_MONTH','PRE_JOBYEARS'])
#data=data.drop(columns=['Unnamed: 0','Unnamed: 0.1'])

###################CHOOSING THECOLUMNS##############
#Excluding the features which are not useful
x=data.iloc[:,[0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
               ,31,32,33,34,35,37,38,39,40,41,42,43,44,45]]


################HEATMAP OF CORRELATION###################
corr_mat=x.corr() 
f,ax=plt.subplots(figsize=(20,15))
ax.set_xticklabels(rotation=75)
sns.heatmap(corr_mat,square=True,annot=True,fmt='.0f')

#Based on heatmap checking how many datapoints are equal so that we can drop similar columns
loan=data[data['LOAN_AMT']==data['NET_DISBURSED_AMT']]
pre=data[data['PRE_EMI_DUEAMT']==data['PRE_EMI_RECEIVED_AMT']]
excess=data[data['EXCESS_AVAILABLE']==data['EXCESS_ADJUSTED_AMT']]

########BATCH  1 ######
#Id, INCOME, loan&disbursed,PRE EMi received & due,dates
x1=data.iloc[:,[0,1,3,6,7,8,9,10,12,13,16,17,18,19,20,21,22,23,24,25,26,28,29,30
               ,31,32,33,34,37,38,39,40,41,42,43]]
x1.to_csv('D:\\Data\\Foreclosure\\Trials\\tr1.csv')