import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from datetime import datetime

data = pd.read_csv('event_details.csv')

data = data.dropna()

data['Event Type'] = pd.Categorical(data['Event Type']).codes

data['Event Date (Start)'] = pd.to_datetime(data['Event Date (Start)'])
data['Event Date (End)'] = pd.to_datetime(data['Event Date (End)'])

data['Event Start Ordinal'] = data['Event Date (Start)'].map(lambda x: x.toordinal())
data['Event End Ordinal'] = data['Event Date (End)'].map(lambda x: x.toordinal())

data['Event Overlap'] = data['Participant Engagement Metrics (Attendance, Feedback)'].apply(lambda x: int(x.split('%')[0]))

features = data[['Event Size (Attendees)', 'Event Duration (Days)', 'Event Type', 'Event Start Ordinal', 'Event End Ordinal']]

X_train, X_test, y_train, y_test = train_test_split(features, data['Event Overlap'], test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')

new_event_data = pd.DataFrame({
    'Event Size (Attendees)': [1000],
    'Event Duration (Days)': [3],
    'Event Type': [4],
    'Event Start Ordinal': [datetime(2024, 1, 25).toordinal()],  # Example start date
    'Event End Ordinal': [datetime(2024, 1, 28).toordinal()]     # Example end date
})

training_date_range_start = data['Event Date (Start)'].min()
training_date_range_end = data['Event Date (End)'].max()

if new_event_data['Event Start Ordinal'].iloc[0] < training_date_range_start.toordinal() or new_event_data['Event End Ordinal'].iloc[0] > training_date_range_end.toordinal():
    print(f"Warning: New event dates ({new_event_data['Event Start Ordinal'].iloc[0]}, {new_event_data['Event End Ordinal'].iloc[0]}) fall outside the ]date range!")
else:
    new_event_overlap = model.predict(new_event_data)
    print(f'Predicted Event Overlap: {new_event_overlap[0]:.2f}')

    if new_event_overlap[0] > 60:
        print("The events are overlapping strongly, change the time frame or date.")
    else:
        print("No overlapping between the events.")
