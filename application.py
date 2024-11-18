from flask import Flask, render_template, request
import os
import sys

# Ensure the custom module is imported correctly
sys.path.append(os.path.join(os.getcwd(), "src"))
from datascience.pipelines.prediction_pipeline import CustomData, PredictionPipeline

# Initialize the Flask application
application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predicted", methods=['GET', 'POST'])
def prediction_data():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Collect data from the form and create a CustomData instance
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race/ethnicity'),
                parental_level_of_education=request.form.get('parental level of education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test preparation course'),
                reading_score=int(request.form.get('reading score')),
                writing_score=int(request.form.get('writing score'))
            )

            # Convert to DataFrame
            pred_df = data.get_data_frame()
            print("Prediction DataFrame:", pred_df)

            # Use the prediction pipeline to make a prediction
            predict_pipeline = PredictionPipeline()
            results = predict_pipeline.predict(pred_df)

            return render_template('home.html', results=results[0])
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
