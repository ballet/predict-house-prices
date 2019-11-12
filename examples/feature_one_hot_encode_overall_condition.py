from ballet import Feature
from sklearn.preprocessing import OneHotEncoder

input = ["Overall Cond"]
transformer = OneHotEncoder()
name = "Overall Condition One-Hot Encoded"
feature = Feature(input=input, transformer=transformer, name=name)
