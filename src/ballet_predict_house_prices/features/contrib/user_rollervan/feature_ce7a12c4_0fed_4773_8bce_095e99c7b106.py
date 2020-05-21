from ballet import Feature
from ballet.eng import NullFiller

input = ["Total Bsmt SF", "1st Flr SF", "2nd Flr SF"]
transformer = [
    lambda df: 0.5 * df["Total Bsmt SF"] + 1 * df["1st Flr SF"] + 2 * df["2nd Flr SF"],
    NullFiller(),
]
name = "Total Area"
feature = Feature(input=input, transformer=transformer, name=name)
