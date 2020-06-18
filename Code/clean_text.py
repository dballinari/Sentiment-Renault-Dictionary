import re

# URLs are tagged as first: avoids issues when removing special symbols and so on
RE_URL = r'(?:https?://|www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# Expression to remove before tagging
RE_EMAIL = '\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b'
RE_EMOJI = u"""\ud83c[\udf00-\udfff]|\ud83d[\udc00-\ude4f\ude80-\udeff]|[\u2600-\u26FF\u2700-\u27BF]"""
STOP_WORDS = [r'a', r'an', r'the']
RE_STOP_WORDS = r'|'.join([r'\b' + s + r'\b' for s in STOP_WORDS])
SYMBOLS_BEFORE = u'</\"_\\§|´ˇ°[]<>{}~^&*%\xa3€`#'
RE_SYMBOL_BEFORE = r'|'.join([re.escape(s) + r'+' for s in SYMBOLS_BEFORE])

RE_REMOVE_BEFORE = re.compile(r'|'.join([RE_EMAIL, RE_EMOJI, RE_STOP_WORDS, RE_SYMBOL_BEFORE]), re.UNICODE)

# Expressions to be tagged
RE_TAG_NUM = r'\b\d*\'?\d*(,|\.)?\d+\b'
RE_TAG_CASHTAG = r'[$][a-z]+'
RE_TAG_MENTION = r'@[a-zA-Z0-9_]+'
EMOTICONS_POS = [r';)', r':)', r':-)', r'=)', r':D']
RE_EMOTICONS_POS = r'|'.join([re.escape(s) for s in EMOTICONS_POS])
EMOTICONS_NEG = [r':(', r':-(', r'=(']
RE_EMOTICONS_NEG = r'|'.join([re.escape(s) for s in EMOTICONS_POS])

# Expression to remove after tagging
SYMBOLS_AFTER = r'().,\'=$;:'
RE_SYMBOL_AFTER = r'|'.join([re.escape(s) + r'+' for s in SYMBOLS_AFTER])

# Expression for splitting words and punctuation
RE_SPLIT_WORD_PUNCT = r'(\w+)([!?+-]+)'
RE_SPLIT_PUNCT_WORD = r'([!?+-]+)(\w+)'

# Expressions of negation:
NEGATIONS = [r'not', r'no', r'none', r'neither', r'never', r'nobody']
RE_NEGATIONS = r'(' + r'|'.join([s + r'\s+' for s in NEGATIONS]) + r')(\w+)'


def clean_text(text):
    """
    Args:
        text: tweet string

    Returns: cleaned tweet string

    """
    text = text.lower()
    # tag urls:
    text = re.sub(RE_URL, r' linktag ', text)
    # first expressions to be removed
    text = RE_REMOVE_BEFORE.sub(r' ', text)
    # expression to replace with tags:
    text = re.sub(RE_TAG_CASHTAG, r' cashtag ', text)
    text = re.sub(RE_TAG_NUM, r' numbertag ', text)
    text = re.sub(RE_TAG_MENTION, r' usertag ', text)
    text = re.sub(RE_EMOTICONS_POS, r' emojipos ', text)
    text = re.sub(RE_EMOTICONS_NEG, r' emojineg ', text)

    # second expressions to be removed
    text = re.sub(RE_SYMBOL_AFTER, r' ', text)

    # split words and punctuations
    text = re.sub(RE_SPLIT_WORD_PUNCT, r'\1 \2', text)
    text = re.sub(RE_SPLIT_PUNCT_WORD, r'\1 \2', text)

    # add negations to words
    text = re.sub(RE_NEGATIONS, r'negtag_\2', text)

    # remove multiple white spaces
    text = re.sub(r'\s+', ' ', text)

    return text

