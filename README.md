
# Student Performance Indicator
#### An End-to-End Machine Learning Project with Flask Web Application
![alt text](image.png)

![alt text](image-1.png)

### Overview
The Student Performance Indicator project is an end-to-end machine learning pipeline designed to predict student performance based on academic and demographic factors. It incorporates robust data processing, machine learning model development, evaluation, and deployment as an interactive web application powered by Flask.

This project is designed with scalability and real-world applicability in mind, ensuring clean architecture, maintainable code, and industry-standard practices.
### Key Features

##### Data Ingestion: 
Efficient loading and preprocessing of raw datasets.
##### Exploratory Data Analysis (EDA): 
Insightful visualizations and statistical analyses to understand key trends.
##### Feature Engineering:
 Data cleaning, transformation, and feature selection for optimal performance.
##### Model Development:
Implementation of state-of-the-art ML algorithms (e.g., Random Forest, Gradient Boosting).
##### Hyperparameter optimization for model fine-tuning.
##### Model Evaluation: 
Comprehensive evaluation using metrics such as Accuracy, Precision, Recall, F1-score, and ROC-AUC.
##### Web Deployment: 
Seamless integration of the ML model into a Flask-based web application for user interaction.

### Project Structure

student-performance-indicator/


├── templates/             # HTML templates for the Flask app

├── data/                  # Raw and processed datasets

├── models/                # Trained ML model files

├── src/

│   ├── __init__.py        # Initialization scripts

│   ├── data_ingestion.py  # Data loading and preprocessing logic

│   ├── eda.py             # Exploratory data analysis scripts

│   ├── model_training.py  # Model training and tuning scripts

│   ├── model_evaluation.py # Model evaluation scripts

│   ├── Flask_app.py             # Flask application entry point

│
├── setup.py , template.py/                 # Unit and integration tests

├── requirements.txt       # Python dependencies

├── README.md              # Project documentation

└── .gitignore             # Ignore unnecessary files in version control
### Setup Instructions
#### Prerequisites
1- Python 3.8 or higher

2- Pip or Conda for package management
### Workflow
#### Upload Dataset: Users can upload a dataset or use the pre-loaded dataset.
#### EDA Dashboard: View insights through visualizations.
#### Model Prediction: Predict student performance based on custom inputs.

### Technologies Used
#### Backend
Python (Pandas, NumPy, Scikit-learn, CatBoost)

Flask (Route integration)
#### Frontend
HTML

