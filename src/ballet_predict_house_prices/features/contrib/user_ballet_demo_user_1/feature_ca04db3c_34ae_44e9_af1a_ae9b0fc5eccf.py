from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = ["Full Bath", "Half Bath"]
transformer = SimpleFunctionTransformer(lambda df: df["Full Bath"] + df["Half Bath"])
name = "Total Bath"
feature = Feature(input=input, transformer=transformer, name=name)
