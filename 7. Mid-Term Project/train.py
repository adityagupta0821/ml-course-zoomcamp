#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
import pickle

df = pd.read_csv("bank-additional-full.csv", sep=";")

df = df[~(df['job']=="unknown")]
df = df[~(df['marital']=="unknown")]
df = df[~(df['education']=="unknown")]
df = df[~(df['default']=="unknown")]
df = df[~(df['housing']=="unknown")]
df = df[~(df['loan']=="unknown")]

df["y"] = df["y"].map({"yes":1, "no":0})

#train test split
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

top_cat_col = ["poutcome", "month", "contact", "job", "education"]

top_num_col = ["duration", "nr.employed", "pdays", "euribor3m", "emp.var.rate"]

def train(df_train, y_train, C=1.0):
    dicts = df_train[top_cat_col + top_num_col].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    
    return dv, model

def predict(df, dv, model):
    dicts = df[top_cat_col + top_num_col].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

C=1.0
n_splits = 10
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.y.values
    y_val = df_val.y.values

    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

print('C=%s %.3f +- %.3f' % (C, np.mean(scores), np.std(scores)))

dv, model = train(df_full_train, df_full_train.y.values, C=1.0)
y_pred = predict(df_test, dv, model)
y_test = df_test.y.values
auc = roc_auc_score(y_test, y_pred)

# Save the model

output_file = f'model_{C}.bin'

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

