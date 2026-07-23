

from pathlib import Path

import pandas as pd

from src.config.datasets import DATASETS
from src.config.settings import RAW_DATA_DIR
from src.utils.logger import logger


class DataExtractor:
    """Load all required datasets into memory."""

    def __init__(self):
        self.datasets = {}

    def load_dataset(self, name: str, filename: str):

        file_path = RAW_DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found.")

        logger.info(f"Loading {filename}")

        df = pd.read_csv(file_path)

        logger.info(f"{filename}: {len(df):,} rows loaded")

        return df

    def load_all(self):

        for name, filename in DATASETS.items():
            self.datasets[name] = self.load_dataset(name, filename)

        logger.info("All datasets successfully loaded.")

        return self.datasets