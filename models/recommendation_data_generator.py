import pandas as pd
import random

# Define some sample categories and interests
categories = ["music", "sports", "tech", "food", "art", "coding", "gaming", "travel"]

#Generate Event Data
def generate_event_data(num_events):
    events = []
    for event_id in range(1, num_events + 1):
        event = {
            "event_id": event_id,
            "event_name": f"Event {event_id}",
            "event_category": random.choice(categories),
            "popularity": random.randint(1, 100),
        }
        events.append(event)
    return pd.DataFrame(events)

#Generate User Data
def generate_user_data(num_users, num_events):
    users = []
    for user_id in range(1, num_users + 1):
        interests = random.sample(categories, random.randint(1, 3))
        attended_events = random.sample(range(1, num_events + 1), random.randint(0, 5))
        user = {
            "user_id": user_id,
            "interests": ", ".join(interests),
            "attended_events": attended_events,
        }
        users.append(user)
    return pd.DataFrame(users)

# Generate data
num_events = 100
num_users = 50

events_df = generate_event_data(num_events)
users_df = generate_user_data(num_users, num_events)

# Save to CSV files
events_file = "rec_events_data.csv"
users_file = "users_data.csv"

events_df.to_csv(events_file, index=False)
users_df.to_csv(users_file, index=False)

events_file, users_file
