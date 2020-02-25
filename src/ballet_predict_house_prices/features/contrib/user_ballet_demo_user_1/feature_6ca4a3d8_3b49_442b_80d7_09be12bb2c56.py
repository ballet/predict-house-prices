from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = ["Garage Area", "Garage Cars"]
transformer = SimpleFunctionTransformer(lambda x: x["Garage Area"] / x["Garage Cars"])
name = "Garage area allocated per car"
feature = Feature(input=input, transformer=transformer, name=name)
