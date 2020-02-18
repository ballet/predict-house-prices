[![ballet](https://img.shields.io/static/v1?label=built%20with&message=ballet&color=FCDD35)](https://github.com/HDI-Project/ballet)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/HDI-Project/ballet-predict-house-prices/master?urlpath=lab)

# Predict House Prices

This is a collaborative predictive modeling project built on the [ballet
framework](https://github.com/HDI-Project/ballet). The goal of this project
is to build a feature engineering pipeline that will be used to predict house
 prices for houses in the [Ames dataset](http://jse.amstat.org/v19n3/decock.pdf).

## Join the collaboration

Are you interested in joining the collaboration? In the open-source spirit,
anyone with an internet connection can contribute features to the
collaboration. In this demonstration project, every feature that is
well-formed will be accepted and no features will be pruned. (In a practical
deployment, Ballet uses a streaming feature selection algorithm to accept
only features that provide an information gain above some threshold, and to
prune older features that have been made redundant by newer ones.)

- Read the [Ballet Contributor Guide](https://hdi-project.github.io/ballet/contributor_guide.html)
- Browse the currently accepted features in the contributed features
    directory (`src/ballet_predict_house_prices/features/contrib`)
- Look at example features (`examples/`)

## Quickstart

### Explore the data

You can load the raw data as follows:

```python
from ballet_predict_house_prices.load_data import load_data
X_df, y_df = load_data()
```

The resulting variables are pandas DataFrames.
```python
X_df.head()
```

|       PID |   MS SubClass | MS Zoning   |   Lot Frontage |   Lot Area | Street   |   Alley | Lot Shape   | Land Contour   | Utilities   | Lot Config   | Land Slope   | Neighborhood   | Condition 1   | Condition 2   | Bldg Type   | House Style   |   Overall Qual |   Overall Cond |   Year Built |   Year Remod/Add | Roof Style   | Roof Matl   | Exterior 1st   | Exterior 2nd   | Mas Vnr Type   |   Mas Vnr Area | Exter Qual   | Exter Cond   | Foundation   | Bsmt Qual   | Bsmt Cond   | Bsmt Exposure   | BsmtFin Type 1   |   BsmtFin SF 1 | BsmtFin Type 2   |   BsmtFin SF 2 |   Bsmt Unf SF |   Total Bsmt SF | Heating   | Heating QC   | Central Air   | Electrical   |   1st Flr SF |   2nd Flr SF |   Low Qual Fin SF |   Gr Liv Area |   Bsmt Full Bath |   Bsmt Half Bath |   Full Bath |   Half Bath |   Bedroom AbvGr |   Kitchen AbvGr | Kitchen Qual   |   TotRms AbvGrd | Functional   |   Fireplaces | Fireplace Qu   | Garage Type   |   Garage Yr Blt | Garage Finish   |   Garage Cars |   Garage Area | Garage Qual   | Garage Cond   | Paved Drive   |   Wood Deck SF |   Open Porch SF |   Enclosed Porch |   3Ssn Porch |   Screen Porch |   Pool Area |   Pool QC | Fence   | Misc Feature   |   Misc Val |   Mo Sold |   Yr Sold | Sale Type   | Sale Condition   |
|----------:|--------------:|:------------|---------------:|-----------:|:---------|--------:|:------------|:---------------|:------------|:-------------|:-------------|:---------------|:--------------|:--------------|:------------|:--------------|---------------:|---------------:|-------------:|-----------------:|:-------------|:------------|:---------------|:---------------|:---------------|---------------:|:-------------|:-------------|:-------------|:------------|:------------|:----------------|:-----------------|---------------:|:-----------------|---------------:|--------------:|----------------:|:----------|:-------------|:--------------|:-------------|-------------:|-------------:|------------------:|--------------:|-----------------:|-----------------:|------------:|------------:|----------------:|----------------:|:---------------|----------------:|:-------------|-------------:|:---------------|:--------------|----------------:|:----------------|--------------:|--------------:|:--------------|:--------------|:--------------|---------------:|----------------:|-----------------:|-------------:|---------------:|------------:|----------:|:--------|:---------------|-----------:|----------:|----------:|:------------|:-----------------|
| 526301100 |            20 | RL          |            141 |      31770 | Pave     |     nan | IR1         | Lvl            | AllPub      | Corner       | Gtl          | NAmes          | Norm          | Norm          | 1Fam        | 1Story        |              6 |              5 |         1960 |             1960 | Hip          | CompShg     | BrkFace        | Plywood        | Stone          |            112 | TA           | TA           | CBlock       | TA          | Gd          | Gd              | BLQ              |            639 | Unf              |              0 |           441 |            1080 | GasA      | Fa           | Y             | SBrkr        |         1656 |            0 |                 0 |          1656 |                1 |                0 |           1 |           0 |               3 |               1 | TA             |               7 | Typ          |            2 | Gd             | Attchd        |            1960 | Fin             |             2 |           528 | TA            | TA            | P             |            210 |              62 |                0 |            0 |              0 |           0 |       nan | nan     | nan            |          0 |         5 |      2010 | WD          | Normal           |
| 526350040 |            20 | RH          |             80 |      11622 | Pave     |     nan | Reg         | Lvl            | AllPub      | Inside       | Gtl          | NAmes          | Feedr         | Norm          | 1Fam        | 1Story        |              5 |              6 |         1961 |             1961 | Gable        | CompShg     | VinylSd        | VinylSd        | None           |              0 | TA           | TA           | CBlock       | TA          | TA          | No              | Rec              |            468 | LwQ              |            144 |           270 |             882 | GasA      | TA           | Y             | SBrkr        |          896 |            0 |                 0 |           896 |                0 |                0 |           1 |           0 |               2 |               1 | TA             |               5 | Typ          |            0 | nan            | Attchd        |            1961 | Unf             |             1 |           730 | TA            | TA            | Y             |            140 |               0 |                0 |            0 |            120 |           0 |       nan | MnPrv   | nan            |          0 |         6 |      2010 | WD          | Normal           |
| 526351010 |            20 | RL          |             81 |      14267 | Pave     |     nan | IR1         | Lvl            | AllPub      | Corner       | Gtl          | NAmes          | Norm          | Norm          | 1Fam        | 1Story        |              6 |              6 |         1958 |             1958 | Hip          | CompShg     | Wd Sdng        | Wd Sdng        | BrkFace        |            108 | TA           | TA           | CBlock       | TA          | TA          | No              | ALQ              |            923 | Unf              |              0 |           406 |            1329 | GasA      | TA           | Y             | SBrkr        |         1329 |            0 |                 0 |          1329 |                0 |                0 |           1 |           1 |               3 |               1 | Gd             |               6 | Typ          |            0 | nan            | Attchd        |            1958 | Unf             |             1 |           312 | TA            | TA            | Y             |            393 |              36 |                0 |            0 |              0 |           0 |       nan | nan     | Gar2           |      12500 |         6 |      2010 | WD          | Normal           |
| 526353030 |            20 | RL          |             93 |      11160 | Pave     |     nan | Reg         | Lvl            | AllPub      | Corner       | Gtl          | NAmes          | Norm          | Norm          | 1Fam        | 1Story        |              7 |              5 |         1968 |             1968 | Hip          | CompShg     | BrkFace        | BrkFace        | None           |              0 | Gd           | TA           | CBlock       | TA          | TA          | No              | ALQ              |           1065 | Unf              |              0 |          1045 |            2110 | GasA      | Ex           | Y             | SBrkr        |         2110 |            0 |                 0 |          2110 |                1 |                0 |           2 |           1 |               3 |               1 | Ex             |               8 | Typ          |            2 | TA             | Attchd        |            1968 | Fin             |             2 |           522 | TA            | TA            | Y             |              0 |               0 |                0 |            0 |              0 |           0 |       nan | nan     | nan            |          0 |         4 |      2010 | WD          | Normal           |
| 527105010 |            60 | RL          |             74 |      13830 | Pave     |     nan | IR1         | Lvl            | AllPub      | Inside       | Gtl          | Gilbert        | Norm          | Norm          | 1Fam        | 2Story        |              5 |              5 |         1997 |             1998 | Gable        | CompShg     | VinylSd        | VinylSd        | None           |              0 | TA           | TA           | PConc        | Gd          | TA          | No              | GLQ              |            791 | Unf              |              0 |           137 |             928 | GasA      | Gd           | Y             | SBrkr        |          928 |          701 |                 0 |          1629 |                0 |                0 |           2 |           1 |               3 |               1 | TA             |               6 | Typ          |            1 | TA             | Attchd        |            1997 | Fin             |             2 |           482 | TA            | TA            | Y             |            212 |              34 |                0 |            0 |              0 |           0 |       nan | MnPrv   | nan            |          0 |         3 |      2010 | WD          | Normal           |

*For a detailed data dictionary, see
[here](https://s3.amazonaws.com/mit-dai-ballet/ames/DataDocumentation.txt).*

The resulting target is a pandas Series.

```python
y_df.head()
```

| SalePrice   |
|------------:|
|      215000 |
|      105000 |
|      172000 |
|      244000 |
|      189900 |

### Run the existing pipeline

You can see the feature values that are extracted by the existing feature
engineering pipeline:

```python
from ballet_predict_house_prices.features import build
result = build(X_df, y_df)
X_train, y_train = result['X'], result['y']
```

### Create your own feature

See detailed info in the [Contributor Guide](https://hdi-project.github.io/ballet/contributor_guide.html) and the [Feature Engineering
Guide](https://hdi-project.github.io/ballet/feature_engineering_guide.html).

Here are some hints on coming up with ideas for new features

1. Treat it like a real data science process, and through exploratory 
   analysis and your own intuition, try to find variables or combinations of 
   variables that when transformed appropriately have high predictive power 
   to the target (house selling price).
1. Look at example features that are provided alongside the project 
   (`examples/`).
1. Look at notebooks that Kagglers have created for this same problem
   (https://www.kaggle.com/c/house-prices-advanced-regression-techniques/notebooks).
