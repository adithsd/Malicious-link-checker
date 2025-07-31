import pandas as pd
import numpy as np
from tensorflow import keras
from Feature_Extractor import extract_features
import joblib

# Paths to your saved models
model_paths = {
    "DecisionTree": "D:/New website fraud/Machine_test/Model training data/Link_Tester_DecisionTree.joblib",
    "RandomForest": "D:/New website fraud/Machine_test/Model training data/Link_Tester_RandomForest.joblib",
    "MLP": "D:/New website fraud/Machine_test/Model training data/Link_Tester_MultilevelPerceptron.joblib"
}

def get_prediction(url, model_name):
    try:
        # Ensure model name is valid
        if model_name not in model_paths:
            raise ValueError(f"Invalid model name: {model_name}")

        # Extract features from the URL
        url_features = extract_features(url)
        if url_features is None:
            return "Error: Unable to extract features from the URL"

        # Convert the list of features to a NumPy array
        url_features_array = np.array(url_features, dtype=np.float32)

        # Reshape the array to ensure it is 2D (1 sample with n features)
        url_features_array = url_features_array.reshape(1, -1)

        # Load the appropriate model
        model_path = model_paths[model_name]
        model = joblib.load(model_path)

        # Handle Keras model (MLP)
        if model_name == "MLP":
            # Keras model - assumes a binary classification with a sigmoid output layer
            probability1 = model.predict(url_features_array)[0][0] * 100  # Binary classification
            # probability = 100-int(probability1)
            return round(probability1, 3)

        # Handle scikit-learn models (Decision Tree, Random Forest)
        elif model_name in ["DecisionTree", "RandomForest"]:
            # For these models, we use `predict_proba()` to get class probabilities
            probability = model.predict_proba(url_features_array)[0][1] * 100
            return round(probability, 3)
       
    except Exception as e:
        # Return a user-friendly error message
        return f"Error: {str(e)}"