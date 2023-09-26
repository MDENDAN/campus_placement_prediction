import joblib

# Load the trained SVM model
def load_model(model_filename):
    try:
        model = joblib.load(model_filename)
        return model
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")

# Make predictions using the loaded model
def predict(model, input_data):
    try:
        prediction = model.predict(input_data)
        return prediction[0]  # Return the first prediction (assuming it's a single sample)
    except Exception as e:
        raise Exception(f"Error making predictions: {str(e)}")

# You can add other functions related to your model here, such as training and evaluation functions
