

from src.utils.logger import logger


class DataCleaner:
    """Standardize and clean datasets."""

    def clean(self, datasets: dict) -> dict:

        cleaned = {}

        for name, df in datasets.items():

            logger.info(f"Cleaning {name}")

            # Remove duplicate rows
            df = df.drop_duplicates()

            # Standardize column names
            df.columns = (
                df.columns
                .str.strip()
                .str.lower()
            )

            cleaned[name] = df

        logger.info("Cleaning completed.")

        return cleaned