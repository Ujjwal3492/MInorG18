import pandas as pd
import random

# Generate sample data
data = {
    "feedback_id": [f"FB{i:04}" for i in range(1, 1001)],
    "text": [
        random.choice([
            "The product quality is excellent!",
            "Customer service needs improvement.",
            "Please add more payment options.",
            "I loved the design, keep it up!",
            "It would be great if you could reduce delivery time.",
            "Not satisfied with the performance.",
            "Amazing experience, would recommend to others.",
            "Can you include more size options?",
            "Neutral about the overall experience.",
            "The app is very slow, please fix it.",
        ])
        for _ in range(1000)
    ],
    "rating": [random.randint(1, 5) for _ in range(1000)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
file_path = "feedback_data.xlsx"
df.to_excel(file_path, index=False)

file_path
