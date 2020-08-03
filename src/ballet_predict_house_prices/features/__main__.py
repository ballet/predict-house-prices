import logging

from ballet.util.io import save_features, save_targets
import click

from ballet_predict_house_prices.load_data import load_data
from ballet_predict_house_prices.features import build

logger = logging.getLogger(__name__)


@click.command()
@click.argument('input_dir', type=click.Path(
    exists=True, file_okay=False, readable=True))
@click.argument('output_dir', type=click.Path(file_okay=False))
def main(input_dir, output_dir):
    """Engineer features"""

    import ballet.util.log
    ballet.util.log.enable(logger=logger, level='INFO', echo=False)
    ballet.util.log.enable(logger=ballet.util.log.logger, level='INFO',
                           echo=False)

    X_df, y_df = load_data(input_dir=input_dir)
    out = build()

    mapper_X = out.mapper_X
    encoder_y = out.encoder_y

    X_ft = mapper_X.transform(X_df)
    y_ft = encoder_y.transform(y_df)

    save_features(X_ft, output_dir)
    save_targets(y_ft, output_dir)


if __name__ == '__main__':
    main()
