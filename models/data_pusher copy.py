import pandas as pd
from pymongo import MongoClient
import sys

def load_csv_to_mongodb():
    try:
        # Read CSV file
        print("Reading CSV file...")
        df = pd.read_csv('event_data.csv')
        print(f"Successfully read {len(df)} records from CSV")

        # Connect to MongoDB
        print("\nConnecting to MongoDB...")
        client = MongoClient('mongodb://localhost:27017/')
        db = client['Minor']
        collection = db['Event']
        
        # Convert DataFrame to list of dictionaries
        records = df.to_dict('records')
        
        # Insert records into MongoDB
        print("Inserting records into MongoDB...")
        result = collection.insert_many(records)
        
        # Verify insertion
        print(f"\nSuccess! Inserted {len(result.inserted_ids)} documents into MongoDB")
        
        # Display sample of inserted data
        print("\nSample of inserted data:")
        for doc in collection.find().limit(3):
            print(doc)
            
        # Display collection stats
        print(f"\nTotal documents in collection: {collection.count_documents({})}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
    finally:
        if 'client' in locals():
            client.close()
            print("\nMongoDB connection closed")

if __name__ == "__main__":
    load_csv_to_mongodb()