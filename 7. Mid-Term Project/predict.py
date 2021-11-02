import pickle
from flask import Flask
from flask import request
from flask import jsonify

input_file = 'model_1.0.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

app = Flask('term_deposit')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    term_deposit = y_pred >= 0.6

    result = {
        'term_deposit_probability': float(y_pred),
        'term_deposit_happening': bool(term_deposit)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)