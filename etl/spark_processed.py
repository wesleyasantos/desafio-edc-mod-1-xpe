import logging
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, min, max, lit

# Config de logs da aplicação
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('datalake_enem_small_upsert')
logger.setLevel(logging.DEBUG)

# Define a SparkSession
spark = (sparkSession
        .builder
        .appName("Processed")
        .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("sparl.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .getOrCreate()
)

logger.info("Importing delta.tables...")
from delta.tables import *

logger.info("Produzindo novos dados...")
rais_2020 = (
    spark
    .read
    .format("delta")
    .load("s3://dados-rais-2020-edc/gold/rais_2020")
)

# Gera o manifesto symlink para realizar consultas dos arquivos `delta` no AWS Athena
logger.info("Gera manifesto symlink...")
rais_2020.generate("symlink_format_manifest")

logger.info("Manifesto gerado.")