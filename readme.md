# Python implementation of the social media dictionaries of Renault
## Introduction
This repository contains a Python implementation to compute 
the sentiment of finance related social media posts (Twitter and StockTwits) 
using the dictionaries created by 
[Renault (2017)](https://www.sciencedirect.com/science/article/pii/S0378426617301589). 
More precisely, the code takes as an input the text of a social media post and
returns its sentiment score ranging from -1 (bearish) to +1 (bullish). 

## Set-up
This project is constructed using Python 3.6 and the `nltk` module (version 3.5). 
The required modules can be installed by navigating to the root of this project and running 
`pip install -r requirements.txt`.

## Example
```python
from Code.compute_sentiment import compute_sentiment

text = r'$SPY Want to see a bloodbath, take a look at the short attack on $STRP! A scam company like $VRX called on their BS!'

sentiment_l1 = compute_sentiment(text, dictionary='l1')
sentiment_l2 = compute_sentiment(text, dictionary='l2')
```

## Details
Detailed descriptions of the data cleaning procedure and the construction of the two dictionaries 
can be found in the original paper of 
[Renault (2017)](https://www.sciencedirect.com/science/article/pii/S0378426617301589). The two 
dictionaries (L1 and L2) can be obtained directly from 
[Thomas Renault's webpage](http://www.thomas-renault.com/data.php).