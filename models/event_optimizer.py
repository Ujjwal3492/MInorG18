import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from datetime import datetime, time

def load_and_prepare_data(file_path):
    """Load and prepare the training data."""
    data = pd.read_csv(file_path)
    data = data.dropna()
    
    # Convert Event Type to categorical codes
    data['Event Type'] = pd.Categorical(data['Event Type']).codes
    
    # Process dates
    data['Event Date (Start)'] = pd.to_datetime(data['Event Date (Start)'])
    data['Event Date (End)'] = pd.to_datetime(data['Event Date (End)'])
    data['Event Start Ordinal'] = data['Event Date (Start)'].map(lambda x: x.toordinal())
    data['Event End Ordinal'] = data['Event Date (End)'].map(lambda x: x.toordinal())
    
    # Process time slots
    data[['Start Time', 'End Time']] = data['Event Schedule (Start - End)'].str.split(' - ', expand=True)
    data['Start Time'] = pd.to_datetime(data['Start Time'], format='%H:%M').dt.hour
    data['End Time'] = pd.to_datetime(data['End Time'], format='%H:%M').dt.hour
    
    # Extract attendance percentage
    data['Event Overlap'] = data['Participant Engagement Metrics (Attendance, Feedback)'].apply(lambda x: int(x.split('%')[0]))
    
    return data

def check_time_overlap(existing_events, new_event):
    """Check for time overlap between events"""
    for _, event in existing_events.iterrows():
        # Check if dates overlap
        if not (new_event['Event Date (End)'] < event['Event Date (Start)'] or 
                new_event['Event Date (Start)'] > event['Event Date (End)']):
            # Check if times overlap
            if not (new_event['End Time'] <= event['Start Time'] or 
                    new_event['Start Time'] >= event['End Time']):
                return True
    return False

def train_model(data):
    """Train the Random Forest model."""
    features = data[['Event Size (Attendees)', 'Event Duration (Days)', 
                    'Event Type', 'Event Start Ordinal', 'Event End Ordinal',
                    'Start Time', 'End Time']]
    X_train, X_test, y_train, y_test = train_test_split(
        features, data['Event Overlap'], test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Calculate and print model accuracy
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Model Mean Absolute Error: {mae:.2f}')
    
    return model, data['Event Date (Start)'].min(), data['Event Date (End)'].max()

def get_user_input():
    """Get event details from user input."""
    try:
        print("\nPlease enter the following event details:")
        event_size = int(input("Event Size (number of attendees): "))
        event_duration = int(input("Event Duration (days): "))
        event_type = int(input("Event Type (0=Conference, 1=Festival, 2=Seminar, 3=Trade Show): "))
        
        while True:
            try:
                start_date = input("Event Start Date (YYYY-MM-DD): ")
                start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
                
                end_date = input("Event End Date (YYYY-MM-DD): ")
                end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
                
                if end_datetime < start_datetime:
                    print("End date must be after start date. Please try again.")
                    continue
                
                start_time = input("Event Start Time (HH:MM, 24-hour format): ")
                end_time = input("Event End Time (HH:MM, 24-hour format): ")
                
                start_hour = datetime.strptime(start_time, '%H:%M').hour
                end_hour = datetime.strptime(end_time, '%H:%M').hour
                
                break
            except ValueError:
                print("Invalid date/time format. Please use YYYY-MM-DD for dates and HH:MM for times.")
        
        return pd.DataFrame({
            'Event Size (Attendees)': [event_size],
            'Event Duration (Days)': [event_duration],
            'Event Type': [event_type],
            'Event Start Ordinal': [start_datetime.toordinal()],
            'Event End Ordinal': [end_datetime.toordinal()],
            'Start Time': [start_hour],
            'End Time': [end_hour],
            'Event Date (Start)': [start_datetime],
            'Event Date (End)': [end_datetime]
        })
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def predict_overlap(model, new_event_data, data, training_start, training_end):
    """Predict overlap for new event data."""
    if new_event_data['Event Start Ordinal'].iloc[0] < training_start.toordinal() or \
       new_event_data['Event End Ordinal'].iloc[0] > training_end.toordinal():
        print("\nWarning: New event dates fall outside the training data date range!")
        print(f"Training data range: {training_start.date()} to {training_end.date()}")
    
    # Check for direct time conflicts
    has_overlap = check_time_overlap(data, new_event_data.iloc[0])
    if has_overlap:
        print("\nWarning: Direct time conflict detected with existing events!")
        return 100.0
    
    # Predict overlap probability
    features = new_event_data[['Event Size (Attendees)', 'Event Duration (Days)', 
                              'Event Type', 'Event Start Ordinal', 'Event End Ordinal',
                              'Start Time', 'End Time']]
    overlap_prediction = model.predict(features)[0]
    print(f'\nPredicted Event Overlap: {overlap_prediction:.2f}%')
    
    if overlap_prediction > 60:
        print("Warning: High event overlap predicted. Consider changing the time frame or date.")
    else:
        print("Event overlap is within acceptable range.")
    
    return overlap_prediction

def main():
    try:
        data = load_and_prepare_data('event_data.csv')
        model, training_start, training_end = train_model(data)
        
        while True:
            new_event_data = get_user_input()
            if new_event_data is None:
                continue
            
            predict_overlap(model, new_event_data, data, training_start, training_end)
            
            if input("\nWould you like to predict another event? (yes/no): ").lower() != 'yes':
                break
        
        print("\nThank you for using the Event Overlap Predictor!")
    
    except FileNotFoundError:
        print("Error: Could not find 'event_details.csv'. Please ensure the file exists in the current directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()