import numpy as np
from sklearn.preprocessing import FunctionTransformer


def get_target_encoder():
    """Get encoder for the prediction target

    Returns:
        transformer-like
    """
    return FunctionTransformer(func=np.log, inverse_func=np.exp)
