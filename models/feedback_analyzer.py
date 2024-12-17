from pymongo import MongoClient
from transformers import pipeline

client = MongoClient("mongodb://localhost:27017/")
db = client["feedback_db"]
collection = db["feedbacks"]

feedback_data = collection.find()
feedback_list = [fb["text"] for fb in feedback_data]

# Sentiment Analysis Model
sentiment_analyzer = pipeline("sentiment-analysis")
classifier = pipeline("zero-shot-classification")

labels = ["suggestion", "general feedback"]

#Analyzing it
def analyze_feedback(feedback):
    # Sentiment Analysis
    sentiment_result = sentiment_analyzer(feedback)[0]
    sentiment = sentiment_result["label"]  # POSITIVE, NEGATIVE, or NEUTRAL

    # Suggestion Detection
    classification_result = classifier(feedback, labels)
    suggestion_label = classification_result["labels"][0]  # suggestion or general feedback

    return {
        "feedback": feedback,
        "sentiment": sentiment,
        "is_suggestion": suggestion_label == "suggestion"
    }

analysis_results = [analyze_feedback(fb) for fb in feedback_list]

positive_feedbacks = sum(1 for res in analysis_results if res["sentiment"] == "POSITIVE")
negative_feedbacks = sum(1 for res in analysis_results if res["sentiment"] == "NEGATIVE")
neutral_feedbacks = sum(1 for res in analysis_results if res["sentiment"] == "NEUTRAL")
total_suggestions = sum(1 for res in analysis_results if res["is_suggestion"])

summary = {
    "Total Feedbacks": len(feedback_list),
    "Positive Feedbacks": positive_feedbacks,
    "Negative Feedbacks": negative_feedbacks,
    "Neutral Feedbacks": neutral_feedbacks,
    "Total Suggestions": total_suggestions
}

print("Feedback Analysis Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")

print("\nSample Suggestions:")
for res in analysis_results:
    if res["is_suggestion"]:
        print(f"- {res['feedback']} (Sentiment: {res['sentiment']})")
