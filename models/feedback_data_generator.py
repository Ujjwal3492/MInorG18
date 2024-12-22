import pandas as pd
import random
import faker

# Initialize Faker for random data generation
fake = faker.Faker()

# Define feedback templates for different categories
suggestion_templates = [
    "Can you please improve the {aspect}?",
    "It would be great if you could add {feature}.",
    "Please consider {action} in the next update.",
    "It would be helpful if {action} could be added.",
    "Can you include more {options}?"
]

general_templates = [
    "I loved the {feature}, great job!",
    "I had an amazing experience with the {service}!",
    "Not satisfied with the {performance}.",
    "Overall good experience, but {improvement} could help.",
    "The customer service was great, but {suggestion} would be appreciated."
]

# Function to generate feedback
def generate_feedback(feedback_id):
    rating = random.choice([1, 2, 3, 4, 5])  # Random rating between 1 and 5
    feedback_type = random.choice(["suggestion", "general"])

    if feedback_type == "suggestion":
        # Select a random suggestion template and insert a random aspect/feature
        template = random.choice(suggestion_templates)
        aspect = random.choice(["delivery time", "size options", "payment methods", "customer service", "payment options"])
        feature = random.choice(["faster delivery", "more sizes", "better support", "more payment options"])
        action = random.choice(["adding more features", "reducing processing time", "improving support"])
        options = random.choice(["payment options", "delivery options", "size options"])
        feedback_text = template.format(aspect=aspect, feature=feature, action=action, options=options)  # Ensure all placeholders are filled
    else:
        # Select a general feedback template and insert a random feature/improvement
        template = random.choice(general_templates)
        feature = random.choice(["design", "service", "experience", "performance"])
        improvement = random.choice(["better support", "faster delivery", "more choices"])
        suggestion = random.choice(["adding more options", "faster responses", "clearer instructions"])
        service = random.choice(["product", "service", "platform"])
        performance = random.choice(["quality", "design", "speed", "features"])
        feedback_text = template.format(feature=feature, improvement=improvement, suggestion=suggestion, service=service, performance=performance)

    return {
        "feedback_id": feedback_id,
        "text": feedback_text,
        "rating": rating
    }

# Generate a large amount of data
def generate_data(num_samples=10000):
    data = []
    for i in range(1, num_samples + 1):
        feedback = generate_feedback(f"FB{str(i).zfill(4)}")
        data.append(feedback)
    return data

# Generate 1000 samples of feedback
sample_data = generate_data(10000)

# Convert to DataFrame
df = pd.DataFrame(sample_data)

# Save the data to Excel
df.to_excel("feedback_data.xlsx", index=False)

print("Sample feedback data generated and saved to 'feedback_data.xlsx'")
