from ballet import Feature
from ballet.eng import NullFiller

input = "Mas Vnr Area"
transformer = NullFiller()
name = "Cleaned Masonry Veneer Area"
feature = Feature(input=input, transformer=transformer, name=name)
