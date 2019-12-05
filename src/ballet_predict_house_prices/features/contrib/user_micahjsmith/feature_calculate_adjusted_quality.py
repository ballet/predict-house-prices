from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = ["Overall Qual", "Overall Cond"]
transformer = SimpleFunctionTransformer(
    lambda df: df["Overall Qual"] - df["Overall Cond"]
)
name = "Adjusted Overall Quality"
feature = Feature(input=input, transformer=transformer, name=name)
