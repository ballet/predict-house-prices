from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Electrical"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Electrical type"
feature = Feature(input=input, transformer=transformer, name=name)
