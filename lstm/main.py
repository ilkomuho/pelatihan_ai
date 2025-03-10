from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load model H5
model = load_model("model_lstm_regression.h5")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data input dari request JSON
        data = request.json['input']  # Data input harus berupa array 2D
        input_data = np.array(data).reshape((1, len(data), 1))  # Sesuaikan dimensi input

        # Prediksi
        prediction = model.predict(input_data)
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
