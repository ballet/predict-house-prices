from ballet import Feature
from sklearn.preprocessing import OneHotEncoder

input = ["Yr Sold"]
transformer = OneHotEncoder()
name = "LX Year sold one-hot encoded."
feature = Feature(input=input, transformer=transformer, name=name)
