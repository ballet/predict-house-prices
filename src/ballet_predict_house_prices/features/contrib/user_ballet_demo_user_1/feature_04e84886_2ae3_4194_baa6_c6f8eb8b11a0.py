from ballet import Feature
from ballet.eng import NullFiller, SimpleFunctionTransformer
import numpy as np

input = ["LotArea", "GrLivArea", "YearBuilt"]
transformer = [
    SimpleFunctionTransformer(
        lambda df: (df["GrLivArea"] / df["LotArea"]) * np.log(df["YearBuilt"])
    ),
    NullFiller(),
]
name = "green_trade_off"
feature = Feature(input=input, transformer=transformer, name=name)
