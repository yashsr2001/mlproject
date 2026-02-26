import pandas as pd # type: ignore
from pathlib import Path
from typing import Union

class DataIngestion:
    """Handle data loading and ingestion from various sources."""
    
    def __init__(self, data_path: Union[str, Path]):
        self.data_path = Path(data_path)
    
    def load_csv(self, filename: str) -> pd.DataFrame:
        """Load data from CSV file."""
        file_path = self.data_path / filename
        return pd.read_csv(file_path)
    
    def load_excel(self, filename: str, sheet_name: str = 0) -> pd.DataFrame:
        """Load data from Excel file."""
        file_path = self.data_path / filename
        return pd.read_excel(file_path, sheet_name=sheet_name)
    
    def load_json(self, filename: str) -> pd.DataFrame:
        """Load data from JSON file."""
        file_path = self.data_path / filename
        return pd.read_json(file_path)
    
    def validate_data(self, df: pd.DataFrame) -> bool:
        """Basic data validation."""
        if df.empty:
            raise ValueError("DataFrame is empty")
        return True