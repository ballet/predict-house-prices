import pandas as pd
from ballet import Feature
from ballet.eng import SimpleFunctionTransformer
from sklearn.preprocessing import OneHotEncoder


def calc_porch_type(df):
    # Porch features
    total_porch_area = df.sum(axis=1)
    porch_type = pd.Series("Unknown", index=df.index)
    porch_type[
        (total_porch_area == df["Enclosed Porch"]) & (df["Enclosed Porch"] > 0)
    ] = "Enclosed"
    porch_type[(total_porch_area == df["3Ssn Porch"]) & (df["3Ssn Porch"] > 0)] = "3Ssn"
    porch_type[
        (total_porch_area == df["Open Porch SF"]) & (df["Open Porch SF"] > 0)
    ] = "Open"
    return porch_type


input = ["Enclosed Porch", "3Ssn Porch", "Open Porch SF"]
transformer = [
    SimpleFunctionTransformer(calc_porch_type),
    OneHotEncoder(),
]
name = "Porch Type (Cleaned, One-Hot Encoded)"
feature = Feature(input=input, transformer=transformer, name=name)
