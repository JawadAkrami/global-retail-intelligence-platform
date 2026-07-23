


from src.extract.extract import DataExtractor
from src.utils.logger import logger


def main():

    logger.info("Pipeline started.")

    extractor = DataExtractor()

    datasets = extractor.load_all()

    print("\nDatasets Loaded:\n")

    for name, df in datasets.items():
        print(f"{name:<15} {df.shape}")

    logger.info("Pipeline finished.")


if __name__ == "__main__":
    main()