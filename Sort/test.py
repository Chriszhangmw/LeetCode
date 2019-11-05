from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()
test = "VADER is smart, handsome, and funny."
print(analyzer.polarity_scores(test))


