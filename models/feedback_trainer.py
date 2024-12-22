
import pandas as pd
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import pickle

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["Minor"]  # Replace with your database name
collection = db["Feed-Back"]  # Replace with your collection name

# Load Data from MongoDB
data = pd.DataFrame(list(collection.find()))

# Preprocess Data
data['sentiment'] = data['rating'].apply(lambda x: "positive" if x > 3 else "negative" if x < 3 else "neutral")
data['is_suggestion'] = data['text'].str.contains(
    r"can|please|would|improve|add|excellent|want|need|should|recommend|request|wish|suggest|hope|like|advise|consider|could you|maybe|it would be nice if|how about|if possible|I would like|could you please|I suggest|please consider|might be better if|fix|change|enhance|adjust|revise|optimize|refine|update|increase", 
    case=False, 
    na=False
)

# Function to train and evaluate a model
def train_and_evaluate_model(X, y, model_class, vectorizer_class):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    vectorizer = vectorizer_class()
    X_train_vectors = vectorizer.fit_transform(X_train)
    model = model_class()
    model.fit(X_train_vectors, y_train)
    
    # Evaluate the model
    accuracy = model.score(vectorizer.transform(X_test), y_test)
    return model, vectorizer, accuracy

# Train and evaluate sentiment analysis model
sentiment_model, sentiment_vectorizer, sentiment_accuracy = train_and_evaluate_model(
    data['text'], 
    data['sentiment'], 
    MultinomialNB, 
    TfidfVectorizer
)

# Train and evaluate suggestion classification model
suggestion_model, suggestion_vectorizer, suggestion_accuracy = train_and_evaluate_model(
    data['text'], 
    data['is_suggestion'], 
    SVC, 
    TfidfVectorizer
)

# Save Models and Vectorizers
with open("sentiment_vectorizer.pkl", "wb") as vec_file:
    pickle.dump(sentiment_vectorizer, vec_file)
with open("sentiment_model.pkl", "wb") as model_file:
    pickle.dump(sentiment_model, model_file)
with open("suggestion_vectorizer.pkl", "wb") as vec_file:
    pickle.dump(suggestion_vectorizer, vec_file)
with open("suggestion_model.pkl", "wb") as model_file:
    pickle.dump(suggestion_model, model_file)

# Print Accuracy
print(f"Sentiment Model Accuracy: {sentiment_accuracy:.2f}")
print(f"Suggestion Model Accuracy: {suggestion_accuracy:.2f}")