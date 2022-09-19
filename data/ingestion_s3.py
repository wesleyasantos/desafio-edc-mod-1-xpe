import boto3
# import pandas as pd

# Cria um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

# Download de um arquivo do s3
# s3_client.download_file("my_bucket",
#                         "endereço_do_arquivo/arquivo.csv",
#                         "endereço_para_salvar_o_arquivo/arquivo.csv")


# Ler o arquivo baixado
# df = pd.read_csv("endereço_do_arquivo/arquivo.csv")
# print(df)

### Upload dos arquivos da RAIS 2020 para o Bucket S3
s3_client.upload_file("RAIS_VINC_PUB_CENTRO_OESTE.txt",
                      "dados-rais-2020-edc",
                      "bronze/centro_oeste.txt")

s3_client.upload_file("RAIS_VINC_PUB_MG_ES_RJ.txt",
                      "dados-rais-2020-edc",
                      "bronze/mg_es_rj.txt")

s3_client.upload_file("RAIS_VINC_PUB_NORDESTE.txt ",
                      "dados-rais-2020-edc",
                      "bronze/nordeste.txt")

s3_client.upload_file("RAIS_VINC_PUB_NORTE.txt",
                      "dados-rais-2020-edc",
                      "bronze/norte.txt")

s3_client.upload_file("RAIS_VINC_PUB_SP.txt",
                      "dados-rais-2020-edc",
                      "bronze/sp.txt")

s3_client.upload_file("RAIS_VINC_PUB_SUL.txt",
                      "dados-rais-2020-edc",
                      "bronze/sul.txt")          