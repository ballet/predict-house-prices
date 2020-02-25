from ballet import Feature
from ballet.eng import BaseTransformer


def house_style_numbers_transform(X):
    return X["House Style"].map(
        {
            "1Story": 1,
            "2Story": 2,
            "1.5Fin": 1.5,
            "SFoyer": 0,
            "SLvl": 0,
            "2.5Unf": 2.5,
            "1.5Unf": 1.5,
            "2.5Fin": 2.5,
        }
    )


input = ["House Style"]
transformer = house_style_numbers_transform
name = "House Style Numbers"
feature = Feature(input=input, transformer=transformer, name=name)
