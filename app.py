import streamlit as st
from models.feedback_analyzer import analyze_feedback
from models.event_optimizer import optimize_event
from models.recommendation_System import recommend_events

# Import additional required libraries
from pymongo import MongoClient
import pandas as pd
import pickle

# Load Models
with open("sentiment_vectorizer.pkl", "rb") as vec_file:
    sentiment_vectorizer = pickle.load(vec_file)
with open("sentiment_model.pkl", "rb") as model_file:
    sentiment_model = pickle.load(model_file)
with open("suggestion_vectorizer.pkl", "rb") as vec_file:
    suggestion_vectorizer = pickle.load(vec_file)
with open("suggestion_model.pkl", "rb") as model_file:
    suggestion_model = pickle.load(model_file)

# App Title
st.title("Event Management Dashboard")
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Feedback Analyzer", "Event Optimizer", "Recommendations"])

if options == "Feedback Analyzer":
    st.header("Feedback Analyzer")
    uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])
    if uploaded_file:
        feedback_df = pd.read_csv(uploaded_file)
        feedback_texts = feedback_df["feedback"].tolist()

        # Analyze feedback
        results = []
        for text in feedback_texts:
            result = analyze_feedback(
                feedback=text,
                sentiment_vectorizer=sentiment_vectorizer,
                sentiment_model=sentiment_model,
                suggestion_vectorizer=suggestion_vectorizer,
                suggestion_model=suggestion_model
            )
            results.append(result)

        # Display Results
        st.write("Analysis Results:")
        st.dataframe(pd.DataFrame(results))

elif options == "Event Optimizer":
    st.header("Event Optimizer")
    st.write("Enter event details for optimization:")
    
    # Form for user input
    with st.form("event_form"):
        attendees = st.number_input("Number of Attendees", min_value=1)
        duration = st.number_input("Event Duration (days)", min_value=1)
        event_type = st.selectbox("Event Type", ["Type 1", "Type 2", "Type 3", "Type 4"])
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        submitted = st.form_submit_button("Optimize Schedule")

    if submitted:
        event_details = {
            "Event Size (Attendees)": [attendees],
            "Event Duration (Days)": [duration],
            "Event Type": [event_type],
            "Event Start Ordinal": [start_date.toordinal()],
            "Event End Ordinal": [end_date.toordinal()],
        }
        prediction = optimize_event(event_details)
        st.write("Optimization Result:")
        st.write(prediction)

elif options == "Recommendations":
    st.header("Personalized Recommendations")
    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    if st.button("Get Recommendations"):
        recommended_events = recommend_events(user_id)
        st.write("Recommended Events:")
        st.dataframe(recommended_events)
