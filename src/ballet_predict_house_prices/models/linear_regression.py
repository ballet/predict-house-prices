"""This is an example model built on top of the feature engineering pipeline"""

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

from ballet_predict_house_prices.features import build


def train(X_df, y_df):
    out = build(X_df, y_df)
    feature_pipeline = out.mapper_X
    target_encoder = out.encoder_y
    model = LinearRegression()
    pipeline = Pipeline([('feature_engineering_pipeline', feature_pipeline),
                         ('linear_regression', model)])
    pipeline.fit(X_df, target_encoder.fit_transform(y_df))
    return pipeline, target_encoder


def predict(pipeline, target_encoder, x):
    # x is 1+ rows of a data frame
    # Observe that predictions are in the encoded space
    # TODO target_encoder must be able to inverse transform
    # FIXME x = X_df.iloc[355:356] yields IndexError
    return pipeline.predict(x)


if __name__ == '__main__':
    # demo the model;
    from ballet_predict_house_prices.load_data import load_data
    X_df, y_df = load_data()
    pipeline, _ = train(X_df, y_df)
    x = X_df.iloc[0:1]  # x is the first row of training data
    prediction = predict(pipeline, _, x)
    print('Row 0: Predicted {}, actual {}'
          .format(prediction.item(), y_df.iloc[0]))