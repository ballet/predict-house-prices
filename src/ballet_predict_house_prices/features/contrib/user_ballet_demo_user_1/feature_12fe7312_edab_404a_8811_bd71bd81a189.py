from ballet import Feature

input = ["House Style"]
transformer = house_style_numbers_transform
name = "House Style Numbers"
feature = Feature(input=input, transformer=transformer, name=name)
