from ballet import Feature
from ballet.eng import NullFiller


input = ['Lot Area', 'Gr Liv Area', 'Garage Area']
transformer = [
    lambda ser: ser['Lot Area'] - ser['Gr Liv Area'] - ser['Garage Area'],
    NullFiller(),
]
name = "Total green area"
feature = Feature(input=input, transformer=transformer, name=name)