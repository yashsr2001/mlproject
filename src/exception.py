class CustomException(Exception):
    """Custom exception class for ML project errors."""
    
    def __init__(self, message: str, error_details=None):
        self.message = message
        self.error_details = error_details
        super().__init__(self.message)
    
    def __str__(self):
        if self.error_details:
            return f"{self.message}\nDetails: {self.error_details}"
        return self.message