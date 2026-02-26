import os 
import sys
from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (GradientBoostingRegressor,AdaBoostRegressor,RandomForestRegressor)
from catboost import CatBoostRegressor
from xgboost import XGBRegressor    

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts',"model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1])
            models={
                "Linear Regression":LinearRegression(),
                "Decision Tree":DecisionTreeRegressor(),
                "Random Forest":RandomForestRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatBoosting Regressor":CatBoostRegressor(verbose=False),

                "AdaBoost Regressor":AdaBoostRegressor()
            }
            model_report=evaluate_model(X_train,y_train,X_test,y_test,models)
            best_model_name=sorted(model_report.items(),key=lambda x:x[1],reverse=True)[0][0]
            best_model_score=sorted(model_report.items(),key=lambda x:x[1],reverse=True)[0][1]
            if best_model_score<0.6:
                raise CustomException("No best model found",sys)
            logging.info(f"Best model found is {best_model_name}")
            

            best_model = models[best_model_name]
            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)

            best_model.fit(X_train,y_train)

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square
        
        except Exception as e:
            raise CustomException(e,sys)
            
