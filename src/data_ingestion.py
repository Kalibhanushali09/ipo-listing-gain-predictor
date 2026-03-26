import os
import pandas as pd
from dataclasses import dataclass

df_original = pd.read_excel("Initial Public Offering.xlsx")
df_original.to_csv("artifacts/raw_data.csv", index=False)

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self, file_path):
        df = pd.read_excel(file_path)
        os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
        df.to_csv(self.config.raw_data_path, index=False)
        return self.config.raw_data_path