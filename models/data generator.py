# import pandas as pd
# import random


# event_types = ["Conference", "Trade Show", "Festival", "Concert", "Workshop", "Webinar", "Seminar"]
# event_sizes = range(100, 10000)  # Random number of attendees
# event_durations = range(1, 5)  # Random event duration in days
# event_schedules = ["09:00 - 17:00", "10:00 - 18:00", "12:00 - 22:00", "19:00 - 22:00", "08:00 - 16:00", "14:00 - 20:00"]
# demographics = [
#     "18-25, Indore, Tech", "25-40, Bhopal, Business", "30-50, Delhi, Education",
#     "16-30, Banglore, Music", "18-35, Maharashtra, Arts", "20-45, Mumbai, Sports"
# ]
# engagement_metrics = ["85%, Positive", "75%, Neutral", "95%, Positive", "90%, Very Positive", "70%, Mixed", "80%, Negative"]

# # Generate 1000 rows of random data
# rows = []
# for _ in range(10000):
#     row = {
#         "Event Type": random.choice(event_types),
#         "Event Size (Attendees)": random.choice(event_sizes),
#         "Event Duration (Days)": random.choice(event_durations),
#         "Event Schedule (Start - End)": random.choice(event_schedules),
#         "Participant Demographics (Age, Location, Interests)": random.choice(demographics),
#         "Participant Engagement Metrics (Attendance, Feedback)": random.choice(engagement_metrics)
#     }
#     rows.append(row)

# # Create DataFrame
# df_large = pd.DataFrame(rows)

# # Save to CSV
# csv_file_path = "event_data.csv"
# df_large.to_csv(csv_file_path, index=False)

import pandas as pd
from datetime import datetime, timedelta
import random

# Function to generate a list of dates for a month
def generate_dates(start_date, num_dates):
    dates = []
    for i in range(num_dates):
        dates.append(start_date + timedelta(days=i))
    return dates

# Starting date of the month
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)

# Define the data with dates spanning over a month
event_types = ["Trade Show", "Conference", "Seminar", "Festival"]
event_sizes = [1170, 1041, 579, 6947]
event_durations = [2, 4, 1, 1]
event_schedules = ["10:00 - 18:00", "12:00 - 22:00", "09:00 - 17:00", "14:00 - 20:00"]
demographics = [
    "18-25, Indore, Tech", 
    "20-45, Mumbai, Sports", 
    "20-45, Mumbai, Sports", 
    "18-35, Maharashtra, Arts"
]
engagement_metrics = [
    "80%, Negative", 
    "80%, Negative", 
    "95%, Positive", 
    "75%, Neutral"
]

# Generate dates for the month
dates = generate_dates(start_date, (end_date - start_date).days + 1)

# Generate the event data with random dates based on event duration
rows = []
for _ in range(10000):
    event_type = random.choice(event_types)
    event_size = random.choice(event_sizes)
    event_duration = random.choice(event_durations)
    event_schedule = random.choice(event_schedules)
    demographic = random.choice(demographics)
    engagement_metric = random.choice(engagement_metrics)
    
    # Randomly pick a start date for the event within the month
    event_start_date = random.choice(dates)
    
    # Calculate the event's end date based on the duration
    event_end_date = event_start_date + timedelta(days=event_duration - 1)
    
    # Convert both start and end dates to the string format
    event_start_date_str = event_start_date.strftime('%Y-%m-%d')
    event_end_date_str = event_end_date.strftime('%Y-%m-%d')
    
    # Add the row to the list
    row = {
        "Event Type": event_type,
        "Event Size (Attendees)": event_size,
        "Event Duration (Days)": event_duration,
        "Event Schedule (Start - End)": event_schedule,
        "Event Date (Start)": event_start_date_str,
        "Event Date (End)": event_end_date_str,
        "Participant Demographics (Age, Location, Interests)": demographic,
        "Participant Engagement Metrics (Attendance, Feedback)": engagement_metric
    }
    rows.append(row)

# Create DataFrame
df_large = pd.DataFrame(rows)

# Save to CSV
df_large.to_csv('event_details.csv', index=False)

print("CSV file 'event_details.csv' has been created successfully.")
