# Data Ingestion
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.components.data_transformation import DataTransformation 
from src.utils import save_object

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Methods Starts")
        
        try:
            # import Dataset
            df = pd.read_csv(os.path.join("Notebooks\Data\Diamond.csv"))
            
            logging.info("Dataset Read as pandas Dataframe")
            
            # Make Directory
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            # create path of raw data file path
            df.to_csv(self.ingestion_config.raw_data_path, index = False)
            
            logging.info("Train Test Split")
            
            # split the dataframe into train & test
            train_set, test_set = train_test_split(df, test_size=.30, random_state=42)
            
            # create train & test csv files
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            
            logging.info("Data Ingestion is Completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Exception occurs at Data Ingestion")
            raise CustomException(e, sys)
        
# Run "Data Ingestion Class"

if __name__ == '__main__':
    # create object of 'DataIngestion' class
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    