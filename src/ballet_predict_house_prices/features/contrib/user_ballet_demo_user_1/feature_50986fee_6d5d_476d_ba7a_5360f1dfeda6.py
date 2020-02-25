import base64, pickle
from ballet import Feature
from ballet.eng import SimpleFunctionTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

keys = [
    "MS SubClass",
    "Lot Frontage",
    "Lot Area",
    "Enclosed Porch",
    "3Ssn Porch",
    "Open Porch SF",
]
wat_this = (
    b"gANjc2tsZWFybi5saW5lYXJfbW9kZWwuX2Jhc2UKTGluZWFyUmVncmVzc2l"
    + b"vbgpxACmBcQF9cQIoWA0AAABmaXRfaW50ZXJjZXB0cQOIWAkAAABub3JtYWxpemVxBIlYBg"
    + b"AAAGNvcHlfWHEFiFgGAAAAbl9qb2JzcQZOWAUAAABjb2VmX3EHY251bXB5LmNvcmUubXVsd"
    + b"GlhcnJheQpfcmVjb25zdHJ1Y3QKcQhjbnVtcHkKbmRhcnJheQpxCUsAhXEKQwFicQuHcQxS"
    + b"cQ0oSwFLBoVxDmNudW1weQpkdHlwZQpxD1gCAAAAZjhxEEsASwGHcRFScRIoSwNYAQAAADx"
    + b"xE05OTkr/////Sv////9LAHRxFGKJQzCs1DbrA2ATwJ+EvJ2cgXZAgOdkq43NAUBPL1Ngi7"
    + b"xiwDcFZw6sG1VAsa1vEjH/c0BxFXRxFmJYCQAAAF9yZXNpZHVlc3EXY251bXB5LmNvcmUub"
    + b"XVsdGlhcnJheQpzY2FsYXIKcRhoEkMI3Eon+jyJq0JxGYZxGlJxG1gFAAAAcmFua19xHEsGWAkAAABzaW5ndWxhcl9xHW"
    + b"gIaAlLAIVxHmgLh3EfUnEgKEsBSwaFcSFoEolDMB/pi7yTBxpByuth8u3RrEDOZGHPHa6qQK+4epK+NaJADgShEyZ3mkC"
    + b"rrRv+vjeVQHEidHEjYlgKAAAAaW50ZXJjZXB0X3EkaBhoEkMIC+mioaOz/kBxJYZxJlJxJ1gQAAAAX3NrbGVhcm5fdmVy"
    + b"c2lvbnEoWAYAAAAwLjIyLjFxKXViLg=="
)


def strange_thingy(df):
    magic = pickle.loads(base64.b64decode(wat_this))
    X = result["X_df"][keys].values
    X[np.isnan(X)] = 0.0
    return magic.predict(X)


input = keys
transformer = [SimpleFunctionTransformer(strange_thingy)]
name = "Strange Thingy (Cleaned, One-Hot Encoded)"
feature = Feature(input=input, transformer=transformer, name=name)
