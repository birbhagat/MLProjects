import os
import sys
import dill
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score

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
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
 







