import numpy as np
from ballet import Feature
from ballet.eng.base import BaseTransformer

input = 'Exterior 1st'

class RandomValue(BaseTransformer):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return np.random.random(X.shape[0])

transformer = RandomValue()
feature = Feature(input=input, transformer=transformer)

if __name__ == "__main__":
    from ballet.util.log import enable
    from ballet.project import Project
    from ballet.validation.main import _load_class
    from ballet_predict_house_prices.features import build
    from ballet_predict_house_prices.load_data import load_data

    enable(level='INFO')

    X_df, y_df = load_data()
    out = build(X_df, y_df)
    X_df, y, features = out.X_df, out.y, out.features

    project = Project.from_path(".")
    Accepter = _load_class(project, 'validation.feature_accepter')
    
    accepter = Accepter(X_df, y, features, feature)
    assert accepter.judge()
