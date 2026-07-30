
from src.extract.extract import DataExtractor
from src.validate.validate import DataValidator
from src.utils.logger import logger


def main():

    logger.info("Pipeline started.")

    extractor = DataExtractor()
    datasets = extractor.load_all()

    validator = DataValidator()
    validator.validate_all(datasets)

    print("Validation completed successfully.")

    logger.info("Pipeline finished.")


if __name__ == "__main__":
    main()