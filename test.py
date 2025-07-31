from API import get_prediction

# Test URL
test_url = "https://www.google.co.in/"

# Choose a model (DecisionTree, RandomForest, MLP)
model_name = "DecisionTree"
# Get prediction
prediction = get_prediction(test_url, model_name)

print(f"Prediction for {test_url}: {prediction}% malicious")

