

from src.validate.rules import REQUIRED_COLUMNS
from src.utils.logger import logger


class DataValidator:

    def validate_columns(self, dataset_name, df):

        required = REQUIRED_COLUMNS.get(dataset_name, [])

        missing = [
            column
            for column in required
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"{dataset_name}: Missing columns {missing}"
            )

        logger.info(
            f"{dataset_name}: Required columns validated."
        )

    def validate_empty(self, dataset_name, df):

        if df.empty:
            raise ValueError(
                f"{dataset_name}: Dataset is empty."
            )

        logger.info(
            f"{dataset_name}: Dataset is not empty."
        )

    def validate_all(self, datasets):

        logger.info("Starting validation.")

        for name, df in datasets.items():

            self.validate_empty(name, df)

            self.validate_columns(name, df)

        logger.info("Validation completed.")


