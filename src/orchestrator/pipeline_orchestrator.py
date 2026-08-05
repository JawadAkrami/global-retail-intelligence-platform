from src.clean.clean import DataCleaner
from src.extract.extract import DataExtractor
from src.load.load import DataLoader
from src.utils.logger import logger
from src.validate.validate import DataValidator


class PipelineOrchestrator:
    """Coordinates the ETL pipeline."""

    def __init__(self):
        self.extractor = DataExtractor()
        self.validator = DataValidator()
        self.cleaner = DataCleaner()
        self.loader = DataLoader()

    def run(self):

        logger.info("Pipeline execution started.")

        datasets = self.extractor.load_all()

        self.validator.validate_all(datasets)

        cleaned = self.cleaner.clean(datasets)

        self.loader.load_bronze(cleaned)

        logger.info("Pipeline execution finished.")


if __name__ == "__main__":

    pipeline = PipelineOrchestrator()

    pipeline.run()

    logger.info("=" * 60)
    logger.info("PIPELINE FINISHED SUCCESSFULLY")
    logger.info("=" * 60)