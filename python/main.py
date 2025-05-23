from flask import Flask, request, jsonify
import requests
from module import prediction
from generate import generate
import time

app = Flask("__name__")
app.config['SECRET_KEY'] = '8BYkEfB7C0sKR6b'


@app.route('/predict', methods=["GET", "POST"])
def predict():
    # Check if file is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files['file']

    # Get the extra inputs (date and integer)
    date = request.form.get("date")
    hour = request.form.get("value")

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Invalid file format. Please upload a CSV file"})

    res = prediction(file, date, hour)
    return jsonify(res)


@app.route('/generate', methods=["GET", "POST"])
def generate_ai():
    # Check if file is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files['file']

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Invalid file format. Please upload a CSV file"})

    res = generate(file)
    return jsonify(res)

#
# url = "http://127.0.0.1:5000/generate"
#
# with open("company_small.csv", "rb") as file:
#     response = requests.post(url, files={"file": file})
#
# # Print the response (JSON output)
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())



if __name__ == '__main__':
    app.run(debug=True)
