from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    print("✅ Model and vectorizer loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model or vectorizer: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data or 'symptoms' not in data:
            return jsonify({'error': 'No symptoms provided in request'}), 400

        symptoms_input = data['symptoms'].strip()

        if not symptoms_input:
            return jsonify({'error': 'Symptoms field is empty'}), 400

        # Vectorize input
        vectorized_input = vectorizer.transform([symptoms_input])

        # Make prediction
        prediction = model.predict(vectorized_input)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return jsonify({
            'error': 'Prediction failed',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
