from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS  # ✅ To allow frontend to access backend

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Backend is running and reachable!'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symptoms_input = data.get('symptoms', '')

    if not symptoms_input.strip():
        return jsonify({'error': 'No symptoms provided'}), 400

    try:
        vectorized_input = vectorizer.transform([symptoms_input])
        prediction = model.predict(vectorized_input)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
