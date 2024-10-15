"""Anonymize specified columns in a CSV file using PySpark with logging."""

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col
from typing import List
import logging


def anonymize_data(input_file: str, output_dir: str, columns_to_anonymize: List[str]) -> None:
    """Anonymize specified columns in the CSV file using PySpark.

    Args:
        input_file (str): Path to the input CSV file.
        output_dir (str): Path to the output directory.
        columns_to_anonymize (List[str]): List of column names to anonymize.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If columns_to_anonymize is empty.
    """
    logger = logging.getLogger("AnonymizeData")
    logger.info("Starting data anonymization process.")

    if not os.path.exists(input_file):
        logger.error(f"Input file '{input_file}' does not exist.")
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    if not columns_to_anonymize:
        logger.error("No columns specified for anonymization.")
        raise ValueError("No columns specified for anonymization.")

    spark = SparkSession.builder \
        .appName("AnonymizeData") \
        .getOrCreate()

    try:
        logger.info("Reading input data...")
        df = spark.read.csv(input_file, header=True)
        total_records = df.count()
        logger.info(f"Total records to process: {total_records}")

        logger.info("Anonymizing columns...")
        for column in columns_to_anonymize:
            if column not in df.columns:
                logger.error(f"Column '{column}' not found in input data.")
                raise ValueError(f"Column '{column}' not found in input data.")
            df = df.withColumn(column, sha2(col(column), 256))

        logger.info("Writing anonymized data to output...")
        df.coalesce(1).write.csv(output_dir, header=True, mode='overwrite')

        logger.info(f"Anonymized data saved to '{output_dir}'")
    except Exception as e:
        logger.exception("An error occurred during data anonymization.")
        raise e
    finally:
        spark.stop()
        logger.info("Spark session stopped.")


def main() -> None:
    """Main function to anonymize data."""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s]: %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger("AnonymizeDataMain")
    logger.info("Anonymizing data...")

    input_file = os.path.join('data', 'large_input.csv')
    output_dir = os.path.join('data', 'anonymized_output')
    columns_to_anonymize = ['first_name', 'last_name', 'address']

    try:
        anonymize_data(input_file, output_dir, columns_to_anonymize)
    except Exception as e:
        logger.error(f"An error occurred in the anonymization process: {e}")


if __name__ == '__main__':
    main()
