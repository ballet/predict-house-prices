from ballet.project import FeatureEngineeringProject

import ballet_predict_house_prices as package
from ballet_predict_house_prices.features.encoder import get_target_encoder
from ballet_predict_house_prices.load_data import load_data


api = FeatureEngineeringProject(
    package=package,
    encoder=get_target_encoder(),
    load_data=load_data,
)
