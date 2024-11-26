from tensorflow.keras.models import load_model

# Load the model
model = load_model('./model_creation/mnist_model.h5')

# Use the model to predict
import numpy as np
from PIL import Image

def predict_digit(image_path):
    # Load and preprocess the image
    img = Image.open(image_path).convert('L').resize((28, 28))
    img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0
    
    # Predict probabilities for each class
    prediction = model.predict(img_array)
    
    # Get the predicted digit and confidence score
    predicted_digit = np.argmax(prediction)
    confidence_score = np.max(prediction)  # Highest probability
    
    return predicted_digit, confidence_score

# Example usage
image_path = "3-sample.png"
digit, confidence = predict_digit(image_path)

print(f"Predicted Digit: {digit}")
print(f"Confidence Score: {confidence:.2f}")