from ballet import Feature
from sklearn.preprocessing import OneHotEncoder

input = ["Neighborhood"]
transformer = OneHotEncoder()
name = "Neighborhood Quality"
feature = Feature(input=input, transformer=transformer, name=name)
