import os
import sys
import dill
import pandas as pd
import numpy as np
import pickle

from src.exception import CustomException
def save_object(file_path, obj):
    try:
        # Ensure the directory exists before writing the file
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)  # ✅ Create directory if it doesn't exist

        # Open file in write-binary mode and save object
        with open(file_path, "wb") as file:  # ✅ Open in write-binary mode
            pickle.dump(obj, file)  # ✅ Save object
    except Exception as e:
        raise CustomException(e, sys)







