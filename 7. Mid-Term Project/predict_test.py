import requests

host = "bank-market-serving-env.eba-7imiivpm.ap-south-1.elasticbeanstalk.com"
url = f"http://{host}/predict"

customer = {
    'poutcome':'success',
    'month':'nov',
    'contact':'cellular',
    'job':'retired',
    'education':'university.degree',
    'duration':208,
    'nr.employed':4963.6,
    'pdays':1,
    'euribor3m':1.031,
    'emp.var.rate':-1.1
}

response = requests.post(url, json=customer).json()

print(response)