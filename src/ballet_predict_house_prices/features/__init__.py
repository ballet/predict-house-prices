import logging

import ballet
import ballet.contrib
import ballet.util.mod
import numpy as np
from ballet.pipeline import EngineerFeaturesResult, FeatureEngineeringPipeline
from sklearn.preprocessing import FunctionTransformer
from stacklog import stacklog

import ballet_predict_house_prices
from ballet_predict_house_prices.load_data import load_data


logger = logging.getLogger(__name__)


def collect_contrib_features():
    """Get contrib features for this project

    Returns:
        List[ballet.Feature]: list of Feature objects
    """
    return ballet.contrib.collect_contrib_features(ballet_predict_house_prices)


def get_target_encoder():
    """Get encoder for the prediction target

    Returns:
        transformer-like
    """
    return FunctionTransformer(func=np.log, inverse_func=np.exp)


@stacklog(logger.info, 'Building features and target')
def build(X_df=None, y_df=None):
    """Build features and target

    Args:
        X_df (DataFrame): raw variables
        y_df (DataFrame): raw target

    Returns:
        dict with keys X_df, features, mapper_X, X, y_df, encoder_y, y
    """
    if X_df is None:
        X_df, _ = load_data()
    if y_df is None:
        _, y_df = load_data()

    features = collect_contrib_features()
    mapper_X = FeatureEngineeringPipeline(features)
    X = mapper_X.fit_transform(X_df)

    encoder_y = get_target_encoder()
    y = encoder_y.fit_transform(y_df)

    return EngineerFeaturesResult(X_df=X_df, features=features, mapper_X=mapper_X, X=X,
                                  y_df=y_df, encoder_y=encoder_y, y=y)
