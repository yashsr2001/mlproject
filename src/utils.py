import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        params = {

            "Decision Tree": {
                "max_depth": [5, 10, 20]
            },

            "Random Forest": {
                "n_estimators": [50, 100],
                "max_depth": [5, 10]
            },

            "Linear Regression": {
                "fit_intercept": [True, False]
            },

            "XGBRegressor": {
                "n_estimators": [50, 100],
                "learning_rate": [0.01, 0.1]
            },

            "CatBoosting Regressor": {
                "depth": [6, 10],
                "learning_rate": [0.01, 0.1]
            },

            "AdaBoost Regressor": {
                "n_estimators": [50, 100],
                "learning_rate": [0.01, 0.1]
            }

        }


        for model_name, model in models.items():

            print(f"Training {model_name}")


            param_grid = params[model_name]


            grid = GridSearchCV(

                estimator=model,

                param_grid=param_grid,

                cv=3,

                scoring="r2",

                n_jobs=-1

            )


            grid.fit(X_train, y_train)


            best_model = grid.best_estimator_


            y_pred = best_model.predict(X_test)


            score = r2_score(y_test, y_pred)


            report[model_name] = score


        return report
    except Exception as e:
        raise CustomException(e, sys)

