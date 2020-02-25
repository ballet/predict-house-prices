from ballet import Feature

from sklearn.impute import SimpleImputer

input = ["Wood Deck SF"]
transformer = SimpleImputer(strategy="mean")
name = "Wood Deck SF"
feature = Feature(input=input, transformer=transformer, name=name)
