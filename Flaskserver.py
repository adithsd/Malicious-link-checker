# from flask import Flask, request, render_template
# from API import get_prediction,model_paths

# app = Flask(__name__)

# # model_path = r"D:/New website fraud/myenv/Machine_test/models/Malicious_URL_Prediction.h5"


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = None
#     if request.method == 'POST':
#         url = request.form.get('url', '')
#         if url:
#             probability = get_prediction(url, model_path)
#             if probability is not None:
#                 if probability >= 23:
#                     result = "Malicious link"
#                 else:
#                     result = "Legitimate link"
#             else:
#                 result = "Error in prediction"
#     return render_template('index.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
from API import get_prediction, model_paths  # Import the model paths and prediction function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_model = None
    if request.method == 'POST':
        url = request.form.get('url', '').strip()  # Get the URL input and remove extra spaces
        selected_model = request.form.get('model_name', '')  # Get the selected model name

        if url and selected_model in model_paths:  # Check if URL and model name are valid
            
            probability = get_prediction(url, selected_model)  # Get prediction from the API
            probability2=int(probability)

            if probability is not None:
                if probability2 >= 23:  # Threshold for malicious link
                    result = f"The link is malicious. Malicious Probability: {probability2:.2f}%"
                else:
                    result = f"The link is legitimate. Malicious Probability: {probability2:.2f}%"
            else:
                result = "Error in prediction. Please try again with a valid URL."
        else:
            result = "Invalid input. Ensure you enter a valid URL and select a model."

    return render_template('index.html', result=result, selected_model=selected_model, model_names=model_paths.keys())

if __name__ == '__main__':
     app.run(debug=False) 
