from deepclassifier.config import ConfigurationManager
from deepclassifier.componets import DataIngestion
from deepclassifier import logger

Stage_Name = "Data Ingestion Stage"

def main():
    
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()



if __name__=='__main__':
    try:
        logger.info(f">>>>stage {Stage_Name} started<<<<")
        main()
        logger.info(f">>>>stage {Stage_Name} completed<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e    