from pyspark.sql import SparkSession
from pysparl.sql.functions import col, min, max

# Cria objeto da SparkSession
spark = (SparkSession
        .builder
        .appName("Transform")
        .enableHiveSupport()
        .getOrCreate()
)

# Leitura dos dados da zona bronze
rais_2020 = (
    spark.read.format("csv")
    .option("inferSchema", True)
    .option("header", True)
    .option("delimiter", ";")
    .option("encoding", "latin1")
    .load("s3://dados-rais-2020-edc/bronze/*.txt")
)

# Escreve os dados na zona silver em formato parquet
print("Writing parquet table...")
(
    rais_2020
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://dados-rais-2020-edc/silver/rais_2020")
)