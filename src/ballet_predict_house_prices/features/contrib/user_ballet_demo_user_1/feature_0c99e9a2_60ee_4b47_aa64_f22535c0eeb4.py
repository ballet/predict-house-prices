from ballet import Feature
from sklearn import preprocessing

input = ["Pool Area"]
name = "PA"
feature = Feature(input=input, transformer=preprocessing.Binarizer(), name=name)
