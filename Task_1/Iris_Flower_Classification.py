
## Task

Iris flower has three species; setosa, versicolor, and virginica, which differs according to their
measurements. Now assume that you have the measurements of the iris flowers according to
their species, and here your task is to train a machine learning model that can learn from the
measurements of the iris species and classify them

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report


df=pd.read_csv('Iris.csv')
df.head()

df.tail()

df=df.drop(columns=['Id'])
df.head()

df.describe()

df.info()

df['Species'].value_counts()

df.shape

df.dtypes

pd.DataFrame({"Missing value (%)": df.isnull().sum()/len(df.index)*100})

data=df.groupby('Species')
print(data)

data.head()

df['Species'].unique()

## Data Visualization

plt.boxplot(df['SepalLengthCm'])

plt.boxplot(df['SepalWidthCm'])

plt.boxplot(df['PetalLengthCm'])

plt.boxplot(df['PetalWidthCm'])

df['SepalLengthCm'].hist()

df['SepalWidthCm'].hist()

df['PetalLengthCm'].hist()

df['PetalWidthCm'].hist()

species_counts = df['Species'].value_counts()
plt.pie(species_counts, labels=species_counts.index, autopct='%1f%%')
plt.axis('equal')
plt.title('Iris DataSet Distribution')
plt.show()

sns.heatmap(df.corr())

X=df.drop('Species',axis=1)
print(X)

Y=df['Species']
print(Y)

## Train and Test Data

X_train,X_test,Y_train,Y_test= train_test_split(X, Y, test_size=0.20, random_state=2)

scaler= StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

classifier=LogisticRegression(multi_class='ovr', solver='lbfgs')
classifier.fit(X_train,Y_train)

Y_pred=classifier.predict(X_test)

### Accuracy

accuracy=accuracy_score(Y_test,Y_pred)
print(accuracy)

### Classification Report

class_report=classification_report(Y_test,Y_pred)
print(class_report)

