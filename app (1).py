from flask import Flask, request, jsonify

app = Flask(__name__)
    
@app.route('/api/v1.0/predict')
def predict():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))

    prediction = 1 if (num1 + num2) > 5.8 else 0

    response = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    }

    return jsonify(response)
if __name__ == '__main__':
    app.run()
