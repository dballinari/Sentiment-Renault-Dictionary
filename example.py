from Code.compute_sentiment import compute_sentiment

text = r'$SPY Want to see a bloodbath, take a look at the short ' \
       r'attack on $STRP! A scam company like $VRX called on their BS!'

sentiment_l1 = compute_sentiment(text, dictionary='l1')
sentiment_l2 = compute_sentiment(text, dictionary='l2')
