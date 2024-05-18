from fastapi import FastAPI
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
app=FastAPI()
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns = iris.feature_names)
df['species'] = iris.target
X= df.iloc[:,0:4]
y=df.iloc[:,4]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
dt= DecisionTreeClassifier()
dt.fit(X_train,y_train)
model = joblib.dump(dt,'vuktales_iris_model')

