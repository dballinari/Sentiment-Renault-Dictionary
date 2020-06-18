from Code.clean_text import clean_text
from Code.load_dictionary import L1_DICTIONARY, L2_DICTIONARY
import nltk
import re


def compute_sentiment(text, dictionary='l1'):
    """
    Args:
        text: tweet string
        dictionary: dictionary name to be used; one of 'l1' and 'l2'

    Returns: numeric sentiment score (float)

    """
    # Clean text
    text = clean_text(text)
    # Select dictionary
    if dictionary == 'l1':
        dictionary = L1_DICTIONARY
    elif dictionary == 'l2':
        dictionary = L2_DICTIONARY
    else:
        return print('No valid dictionary')
    # Split text in tokens
    tokens = text.split()
    # From the tokens, create bi-grams
    bigrams = list(map(' '.join, nltk.bigrams(tokens)))
    # Keep only bi-grams that are in the dictionary
    bigrams = [s for s in bigrams if s in dictionary]
    # Get the sentiment scores associated with the bi-grams
    scores = [dictionary[s] for s in bigrams]
    # Remove bi-grams which have a sentiment score from the text as these tokens are not considered
    # when evaluating the sentiment scores of the uni-grams
    RE_BIGRAMS = r'|'.join([re.escape(s) for s in bigrams])
    text = re.sub(RE_BIGRAMS, '', text)
    # Get uni-grams and their sentiment scores
    unigrams = text.split()
    scores += [dictionary[s] for s in unigrams if s in dictionary]
    # Compute average sentiment of the tweet
    if len(scores) == 0:
        sentiment = 0
    else:
        sentiment = sum(scores)/len(scores)
    return sentiment

