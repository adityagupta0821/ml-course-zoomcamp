# Mid-Term-Project

## Abstract
The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).

## Feature Description:
* [bank-additional-names.md](bank-additional-names.md)

## Dependencies Required and how to install:
* numpy, scikit-learn==0.24.1, flask, gunicorn, pipenv
* pip install pipenv
* pipenv install numpy, scikit-learn==0.24.1, flask, gunicorn

## Steps to Run Dockerfile:
* docker build -t bank_market
* docker run -it --rm -p 9696:9696 bank_market

## Steps To Run the this project:
* [Video to Run this project](2021_11_02_213154.mp4)
* pipenv shell
* eb init -p docker -r ap-south-1 bank_market_serving
* eb create bank-market-serving-env
* python predict_test.py
* eb terminate
