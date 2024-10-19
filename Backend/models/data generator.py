import pandas as pd
import random

# Define possible values for each feature
event_types = ["Conference", "Trade Show", "Festival", "Concert", "Workshop", "Webinar", "Seminar"]
event_sizes = range(100, 10000)  # Random number of attendees
event_durations = range(1, 5)  # Random event duration in days
event_schedules = ["09:00 - 17:00", "10:00 - 18:00", "12:00 - 22:00", "19:00 - 22:00", "08:00 - 16:00", "14:00 - 20:00"]
demographics = [
    "18-25, Indore, Tech", "25-40, Bhopal, Business", "30-50, Delhi, Education",
    "16-30, Banglore, Music", "18-35, Maharashtra, Arts", "20-45, Mumbai, Sports"
]
engagement_metrics = ["85%, Positive", "75%, Neutral", "95%, Positive", "90%, Very Positive", "70%, Mixed", "80%, Negative"]

# Generate 1000 rows of random data
rows = []
for _ in range(10000):
    row = {
        "Event Type": random.choice(event_types),
        "Event Size (Attendees)": random.choice(event_sizes),
        "Event Duration (Days)": random.choice(event_durations),
        "Event Schedule (Start - End)": random.choice(event_schedules),
        "Participant Demographics (Age, Location, Interests)": random.choice(demographics),
        "Participant Engagement Metrics (Attendance, Feedback)": random.choice(engagement_metrics)
    }
    rows.append(row)

# Create DataFrame
df_large = pd.DataFrame(rows)

# Save to CSV
csv_file_path = "event_data.csv"
df_large.to_csv(csv_file_path, index=False)

csv_file_path
