import sys
from src.logger import logging
class CustomException(Exception):

    def __init__(self, message, error_details=sys):

        self.message = message

        _, _, exc_tb = error_details.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename

        self.line_number = exc_tb.tb_lineno

        super().__init__(self.message)

    def __str__(self):

        return f"Error in file [{self.file_name}] at line [{self.line_number}] : {self.message}"