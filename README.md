## ML Model Integration and Deployment

### Steps:
- DecisionTreeClassifier model is used for prediction
- Model is exposed as a Rest API using FAST API
- Model is deployed as Azure Function

### How to Run locally?
``` uvicorn main:app --reload ```
### App Docs: 
http://localhost:8000/redoc
http://localhost:8000/docs#/default/form_create_iris_post
#### Data Set to train model
    IRIS Dataset from scikit-learn

### Deploy to Azure App Service:
Docker image at hub: venmaum/ml-simple-app

### References:
https://scikit-learn.org/stable/modules/tree.html
