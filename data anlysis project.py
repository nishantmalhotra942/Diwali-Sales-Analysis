import numpy as np
import pandas as pd
import matplotlib.pyplot as plt;
import seaborn as sns;
#loading csv file r special characters ke liye he
filepath = r"C:\Users\LENOVO\Desktop\Diwali.csv"
df = pd.read_csv(filepath,encoding='latin-1');
print(df.head(10));
#data cleaning
#ye hme pure dataset ki info derha he
print(df.info());
'''
13  Status            0 non-null      float64
 14  unnamed1          0 non-null      float64
 inke andar koi value nhi he to hum inhe delete kr denge
 '''
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
print(df.info())
#ye hme btayega ki dataset me kitne values null he or true ya false ki form me pr hum sum() use krngejisse hr column me kitne null values he unka sum ajayega
print(pd.isnull(df).sum())
#ab hum dropna() use krenge or null value ko delete krenge inplace dataset me chnges save krta he
print(df.dropna(inplace= True));
print(pd.isnull(df).sum())
#.astype() use krke hum kisi bhi variable ka dtype change kr skte he
df['Amount'] = df['Amount'].astype('int');
print(df['Amount'].dtypes)
print(df[['Age','Amount','Orders']].describe());
#Data Analysis
#Gender
ax = sns.countplot(x = 'Gender',data = df)
for bars in ax.containers:
    ax.bar_label(bars)
    plt.show();
sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False);
sns.barplot(x='Gender',y='Amount',data= sales_gen)
plt.show()
#Age hue='Gender' isse hum gender bhi pta laga skte he age group ka
ax = sns.countplot(x = 'Age Group',data = df,hue='Gender')
plt.show()
#State 
ax = sns.countplot(x = 'State',data = df)
sns.set(rc={'figure.figsize':(95,5)})
plt.show()
Sales_state= df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False);
sns.set(rc={'figure.figsize':(95,5)})
sns.barplot(x='State',y='Orders',data= Sales_state)
plt.show()
mar= df.groupby(['Marital_Status'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False);
sns.set(rc={'figure.figsize':(5,5)})
sns.barplot(x='Marital_Status',y='Amount',data= mar)
plt.show()

'''countplot()
seaborn.countplot() method is used to Show the counts of observations in each categorical bin using bars.
'''
ax = sns.countplot(x = 'State' ,data = df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()
state = df.groupby('State',as_index = False)['Amount'].sum().sort_values(by=['Amount'],ascending=False)
sns.barplot(x = 'State',y = 'Amount',data=state)
plt.show()
