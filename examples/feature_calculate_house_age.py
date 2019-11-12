from ballet import Feature
from ballet.eng import NullFiller, SimpleFunctionTransformer

input = ["Yr Sold", "Year Remod/Add"]
transformer = [
    SimpleFunctionTransformer(lambda df: df["Yr Sold"] - df["Year Remod/Add"]),
    NullFiller(),
]
name = "House Age"
feature = Feature(input=input, transformer=transformer, name=name)
