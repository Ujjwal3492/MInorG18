import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import pickle

# Load Data
data = pd.read_excel("feedback_data.xlsx")

# Preprocess Data
data['sentiment'] = data['rating'].apply(
    lambda x: "positive" if x > 3 else "negative" if x < 3 else "neutral"
)
data['is_suggestion'] = data['text'].str.contains(r"can|please|would|improve|add|excellent|want|need|should|recommend|request|wish|suggest|hope|like|advise|consider|could you|maybe|it would be nice if|how about|if possible|I would like|could you please|I suggest|please consider|might be better if|fix|change|enhance|adjust|revise|optimize|refine|update|increase", case=False, na=False)

# Split Data for Sentiment Analysis
X_sentiment = data['text']
y_sentiment = data['sentiment']
X_train_sent, X_test_sent, y_train_sent, y_test_sent = train_test_split(
    X_sentiment, y_sentiment, test_size=0.2, random_state=42
)

# Split Data for Suggestion Classification
X_suggestion = data['text']
y_suggestion = data['is_suggestion']
X_train_sugg, X_test_sugg, y_train_sugg, y_test_sugg = train_test_split(
    X_suggestion, y_suggestion, test_size=0.2, random_state=42
)

# Train Sentiment Analysis Model
sentiment_vectorizer = TfidfVectorizer()
sentiment_model = MultinomialNB()
X_train_sent_vectors = sentiment_vectorizer.fit_transform(X_train_sent)
sentiment_model.fit(X_train_sent_vectors, y_train_sent)

# Train Suggestion Classification Model
suggestion_vectorizer = TfidfVectorizer()
suggestion_model = SVC(probability=True)
X_train_sugg_vectors = suggestion_vectorizer.fit_transform(X_train_sugg)
suggestion_model.fit(X_train_sugg_vectors, y_train_sugg)

# Save Models and Vectorizers
with open("sentiment_vectorizer.pkl", "wb") as vec_file:
    pickle.dump(sentiment_vectorizer, vec_file)
with open("sentiment_model.pkl", "wb") as model_file:
    pickle.dump(sentiment_model, model_file)
with open("suggestion_vectorizer.pkl", "wb") as vec_file:
    pickle.dump(suggestion_vectorizer, vec_file)
with open("suggestion_model.pkl", "wb") as model_file:
    pickle.dump(suggestion_model, model_file)

# Evaluate Models
X_test_sent_vectors = sentiment_vectorizer.transform(X_test_sent)
sentiment_accuracy = sentiment_model.score(X_test_sent_vectors, y_test_sent)

X_test_sugg_vectors = suggestion_vectorizer.transform(X_test_sugg)
suggestion_accuracy = suggestion_model.score(X_test_sugg_vectors, y_test_sugg)

print(f"Sentiment Model Accuracy: {sentiment_accuracy:.2f}")
print(f"Suggestion Model Accuracy: {suggestion_accuracy:.2f}")
