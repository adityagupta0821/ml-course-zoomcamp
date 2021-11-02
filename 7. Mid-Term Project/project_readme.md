# Mid-Term-Project

## Abstract
The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).

## Feature Description:
* [bank-additional-names.md](bank-additional-names.md)

## Steps To Run the this project:
* pipenv shell
* eb init -p docker -r ap-south-1 bank_market_serving
* eb create bank-market-serving-env
* python predict_test.py
* eb terminate
