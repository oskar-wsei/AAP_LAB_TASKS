import re 


POS_WORDS = {"good","great","excellent","wonderful","love","best","amazing","brilliant","perfect"}
NEG_WORDS = {"bad","worst","awful","terrible","hate","boring","waste","poor","horrible"}


def sentiment_score(text: str) -> int:
    """CPU-bound: tokenizuj, policz pozytywne minus negatywne."""
    tokens = re.findall(r'\w+', text.lower())
    pos_count = sum(1 for token in tokens if token in POS_WORDS)
    neg_count = sum(1 for token in tokens if token in NEG_WORDS)
    return pos_count - neg_count
