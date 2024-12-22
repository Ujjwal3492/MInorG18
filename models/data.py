import pandas as pd
from pymongo import MongoClient

file_path = "feedback_data.xlsx"
data = pd.read_excel(file_path)

client = MongoClient("mongodb://localhost:27017")
db = client["Minor"]
collection = db["FeedBack"]

data_dict = data.to_dict(orient="records")

collection.insert_many(data_dict)

print(f"Data inserted successfully! Total records: {len(data_dict)}")