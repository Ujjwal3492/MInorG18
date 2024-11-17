import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#loading the data
data = pd.read_csv('event_data.csv')

# # Check the columns of the DataFrame
# print("Columns in DataFrame:", data.columns)

# # Clean column names by removing leading/trailing spaces
# data.columns = data.columns.str.strip()

# Preprocess the data
data = data.dropna()  # Handle missing values


data['Event Type'] = pd.Categorical(data['Event Type']).codes


features = data[['Event Size (Attendees)', 'Event Duration (Days)', 'Event Type']]

data['Event Overlap'] = data['Participant Engagement Metrics (Attendance, Feedback)'].apply(lambda x: int(x.split('%')[0]))  # Example conversion

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, data['Event Overlap'], test_size=0.2, random_state=42)

# Train a random forest regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')
# Example new event data
new_event_data = pd.DataFrame({
    'Event Size (Attendees)': [1000],
    'Event Duration (Days)': [3],
    'Event Type': [0]  # Assuming '0' corresponds to a specific event type
})

new_event_overlap = model.predict(new_event_data)
print(f'Predicted Event Overlap: {new_event_overlap[0]:.2f}')
if new_event_overlap>.60:
    print("The events are overlapping strongly, change the time frame or date.")
else:
    print("No overlapping between the events.")