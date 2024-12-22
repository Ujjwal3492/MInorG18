import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class EventDataGenerator:
    def __init__(self):
        # Define event types and their typical characteristics
        self.event_types = {
            'Festival': {
                'size_range': (500, 7000),
                'duration_range': (1, 4),
                'typical_times': [
                    ('09:00', '17:00'),
                    ('10:00', '18:00'),
                    ('12:00', '22:00'),
                    ('14:00', '20:00')
                ]
            },
            'Conference': {
                'size_range': (300, 2000),
                'duration_range': (2, 4),
                'typical_times': [
                    ('09:00', '17:00'),
                    ('10:00', '18:00')
                ]
            },
            'Seminar': {
                'size_range': (50, 1200),
                'duration_range': (1, 4),
                'typical_times': [
                    ('09:00', '17:00'),
                    ('10:00', '18:00'),
                    ('12:00', '22:00')
                ]
            },
            'Trade Show': {
                'size_range': (500, 3000),
                'duration_range': (1, 4),
                'typical_times': [
                    ('10:00', '18:00'),
                    ('12:00', '22:00'),
                    ('14:00', '20:00')
                ]
            }
        }
        
        # Define demographic profiles
        self.demographic_profiles = [
            "18-25, Indore, Tech",
            "20-45, Mumbai, Sports",
            "18-35, Maharashtra, Arts",
            "25-50, Delhi, Business",
            "30-60, Bangalore, Education"
        ]
        
        # Define feedback patterns
        self.feedback_patterns = [
            ("95%, Positive"),
            ("80%, Negative"),
            ("75%, Neutral"),
            ("85%, Positive"),
            ("70%, Negative")
        ]

    def generate_random_date_range(self, start_date, end_date, duration_days):
        """Generate a random start date and calculate end date based on duration"""
        date_range = (end_date - start_date).days - duration_days
        if date_range < 0:
            raise ValueError("Date range is too short for the specified duration")
        
        random_start = start_date + timedelta(days=random.randint(0, date_range))
        random_end = random_start + timedelta(days=duration_days - 1)
        return random_start, random_end

    def generate_events(self, num_events, start_date, end_date):
        """Generate specified number of events within date range"""
        events = []
        
        for _ in range(num_events):
            # Select random event type and its characteristics
            event_type = random.choice(list(self.event_types.keys()))
            type_info = self.event_types[event_type]
            
            # Generate event duration
            duration = random.randint(*type_info['duration_range'])
            
            # Generate event dates
            event_start, event_end = self.generate_random_date_range(
                start_date, end_date, duration
            )
            
            # Select random time slot
            time_slot = random.choice(type_info['typical_times'])
            
            # Generate event size
            event_size = random.randint(*type_info['size_range'])
            
            # Generate other random attributes
            demographics = random.choice(self.demographic_profiles)
            engagement = random.choice(self.feedback_patterns)
            
            # Create event entry
            event = {
                'Event Type': event_type,
                'Event Size (Attendees)': event_size,
                'Event Duration (Days)': duration,
                'Event Schedule (Start - End)': f"{time_slot[0]} - {time_slot[1]}",
                'Event Date (Start)': event_start.strftime('%Y-%m-%d'),
                'Event Date (End)': event_end.strftime('%Y-%m-%d'),
                'Participant Demographics (Age, Location, Interests)': demographics,
                'Participant Engagement Metrics (Attendance, Feedback)': engagement
            }
            
            events.append(event)
        
        return pd.DataFrame(events)

    def save_to_csv(self, df, filename):
        """Save generated data to CSV file"""
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

def main():
    generator = EventDataGenerator()
    
    # Get user input for data generation
    while True:
        try:
            print("\n=== Event Data Generator ===")
            num_events = int(input("Enter number of events to generate: "))
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            end_date_str = input("Enter end date (YYYY-MM-DD): ")
            output_file = input("Enter output filename (e.g., event_data.csv): ")
            
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            
            if start_date >= end_date:
                print("Error: End date must be after start date")
                continue
                
            if num_events <= 0:
                print("Error: Number of events must be positive")
                continue
                
            # Generate and save data
            df = generator.generate_events(num_events, start_date, end_date)
            generator.save_to_csv(df, output_file)
            
            # Display sample of generated data
            print("\nSample of generated data:")
            print(df.head())
            print(f"\nTotal events generated: {len(df)}")
            
            # Show event type distribution
            print("\nEvent type distribution:")
            print(df['Event Type'].value_counts())
            
            break
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again with valid inputs")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again")

if __name__ == "__main__":
    main()