import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)

with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]
churn = y_pred >= 0.5

result = {
    'churn_probability': float(y_pred),
    'churn': bool(churn)
}

print(result)