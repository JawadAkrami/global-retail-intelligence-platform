

from src.database.connection import engine
from src.utils.logger import logger


class DataLoader:

    def load_bronze(self, datasets):

        for name, df in datasets.items():

            logger.info(f"Loading {name}")

            df.to_sql(
                name,
                engine,
                schema="bronze",
                if_exists="replace",
                index=False,
            )

        logger.info("Bronze loading complete.")