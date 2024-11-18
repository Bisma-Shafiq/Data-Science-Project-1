import sys
import pandas as pd
import os
sys.path.append(os.path.join(os.getcwd(), "src"))
from datascience.utils import load_object
from datascience.exception_handling import CustomException

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 writing_score: int,
                 reading_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.writing_score = writing_score
        self.reading_score = reading_score

    def get_data_frame(self):
        try:
            custom_data_input = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "writing score": [self.writing_score],
                "reading score": [self.reading_score],
            }

            return pd.DataFrame(custom_data_input)
        except Exception as e:
            raise CustomException(e, sys)
