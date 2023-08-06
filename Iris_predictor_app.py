import pandas as pd 
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier



# Headling
st.write(''' 

# Iris flower Prediction 
''')


# header for sidebar 
st.sidebar.header('Parameter Input')

# sidebar sliders - Input Paramaters 
# name - min - max - default value 
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.2, 8.4, 5.0)
    sepal_width = st.sidebar.slider('Sepal width', 4.2, 4.2, 3.2)
    petal_length = st.sidebar.slider('Petal length', 1.2, 6.5, 1.0)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.4, 0.1)
    data ={'sepal_length': sepal_length,
           'sepal_width': sepal_width,
           'petal_length': petal_length,
           'petal_width': petal_width}
    features = pd.Dataframe(data, index=[0])
    return features


df = user_input_features()

#main and dataframe
st.subheader('Input Parameters')
st.write(df)

# x is input parameters  \ y is index numbers 01,02
iris =datasets.load_iris()
x = iris.data
y = iris.target


clf = RandomForestClassifier()
clf.fit(x, y)

prediction = clf.predict(df)
prediction_prrobs = clf.predict_proba(df)

st.subheader('Class labels and index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)


 














