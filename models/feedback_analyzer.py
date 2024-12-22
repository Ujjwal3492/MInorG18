from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import pickle

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["Minor"]
collection = db["FeedBack"]

# Fetch feedback texts from the database
feedback_list = [fb["text"] for fb in collection.find()]

# Load Pre-trained Models and Vectorizer
with open("sentiment_vectorizer.pkl", "rb") as vec_file:
    sentiment_vectorizer = pickle.load(vec_file)
with open("sentiment_model.pkl", "rb") as model_file:
    sentiment_model = pickle.load(model_file)
with open("suggestion_vectorizer.pkl", "rb") as vec_file:
    suggestion_vectorizer = pickle.load(vec_file)
with open("suggestion_model.pkl", "rb") as model_file:
    suggestion_model = pickle.load(model_file)

# Analyze Feedback
def analyze_feedback(feedback):
    # Predict sentiment
    sentiment_vector = sentiment_vectorizer.transform([feedback])
    sentiment = sentiment_model.predict(sentiment_vector)[0]

    # Predict suggestion classification
    suggestion_vector = suggestion_vectorizer.transform([feedback])
    suggestion_prediction = suggestion_model.predict(suggestion_vector)[0]
    
    # Check the exact value returned by the model
    is_suggestion = suggestion_prediction == "suggestion"

    return {
        "feedback": feedback,
        "sentiment": sentiment,
        "is_suggestion": is_suggestion
    }

# Perform analysis
analysis_results = [analyze_feedback(fb) for fb in feedback_list]

# Debugging: Check unique values in suggestion predictions
suggestion_predictions = [res["is_suggestion"] for res in analysis_results]
print("Unique suggestion predictions:", set(suggestion_predictions))

# Aggregate Results
summary = {
    "Total Feedbacks": len(feedback_list),
    "Positive Feedbacks": sum(res["sentiment"] == "positive" for res in analysis_results),
    "Negative Feedbacks": sum(res["sentiment"] == "negative" for res in analysis_results),
    "Neutral Feedbacks": sum(res["sentiment"] == "neutral" for res in analysis_results),
    "Total Suggestions": sum(res["is_suggestion"] for res in analysis_results),  # Ensure this is a proper boolean sum
}

# Display Results
print("Feedback Analysis Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")

# Debugging: Show all analysis results to ensure is_suggestion is working
# print("\nAll Analysis Results:")
# for res in analysis_results:
#     print(f"Feedback: {res['feedback']} | Is Suggestion: {res['is_suggestion']}")

# print("\nSample Suggestions:")
# for res in filter(lambda r: r["is_suggestion"], analysis_results):
#     print(f"- {res['feedback']} (Sentiment: {res['sentiment']})")

