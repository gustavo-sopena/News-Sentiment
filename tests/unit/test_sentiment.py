from headlines_sentiment.sentiment import score_headline


def test_score_positive():
    label, score = score_headline("This is a good and great result")
    assert label == "Positive"
    assert score > 0


def test_score_negative():
    label, score = score_headline("This is a bad and worse outcome")
    assert label == "Negative"
    assert score < 0


def test_score_neutral():
    label, score = score_headline("This headline has neutral wording")
    assert label in ("Neutral", "Unknown")
