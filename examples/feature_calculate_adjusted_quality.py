from ballet import Feature

input = ["Overall Qual", "Overall Cond"]
transformer = lambda df: df["Overall Qual"] - df["Overall Cond"]
name = "Adjusted Overall Quality"
feature = Feature(input=input, transformer=transformer, name=name)
