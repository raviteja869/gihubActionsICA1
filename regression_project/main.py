import os
from flask import Flask, jsonify
from src.data_preparation import generate_regression_data
from src.model import create_regression_model
from src.train import train_regression_model
from src.predict import predict_regression

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    # Example input for prediction
    sample_input = [[0.5]]
    predicted_value = predict_regression(regression_model, sample_input)
    return jsonify({"Predicted value": predicted_value[0][0]})

# Generate synthetic regression data
X_train, y_train = generate_regression_data()

# Create and train the regression model
regression_model = create_regression_model(X_train.shape[1:])
train_regression_model(regression_model, X_train, y_train, epochs=100, batch_size=32)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
