# Event Management System

## Description

A full-stack event management system with machine learning capabilities for feedback analysis, event optimization, and personalized recommendations. The system includes a backend API, a React frontend, and a Streamlit dashboard for ML-powered features.

## Features

- **Feedback Analyzer**: Upload CSV files with event feedback to analyze sentiment and classify suggestions using pre-trained ML models.
- **Event Optimizer**: Input event details (attendees, duration, type, dates) to optimize event schedules.
- **Personalized Recommendations**: Get event recommendations based on user ID using collaborative filtering.
- **User Management**: RESTful API for managing users, organizers, participants, and events with JWT authentication.
- **Frontend Dashboard**: React-based UI with components for login, dashboards for organizers and participants, and event listings.

## Tech Stack

- **Backend**: Node.js, Express.js, MongoDB (with Mongoose), JWT, bcrypt
- **Frontend**: React, Vite, Tailwind CSS
- **Machine Learning**: Python, scikit-learn, pandas, Streamlit
- **Database**: MongoDB
- **Other**: HTML/CSS for additional frontend pages

## Project Structure

- `Backend/`: Node.js Express server with API routes, controllers, models, and middleware
- `Frontend/`: React application with components for various dashboards and pages
- `FRONTEND NEW/`: Additional HTML/CSS pages for login, event organization, and prediction dashboards
- `models/`: Python scripts for ML models, data generation, training, and analysis
- `app.py`: Main Streamlit dashboard application
- Data files: `event_data.csv`, `feedback_data.csv`, `users_data.csv`, `rec_events_data.csv`
- ML models: `sentiment_model.pkl`, `sentiment_vectorizer.pkl`, `suggestion_model.pkl`, `suggestion_vectorizer.pkl`

## Installation

### Prerequisites

- Node.js (v14 or higher)
- Python 3.x
- MongoDB
- npm or yarn

### Backend Setup

1. Navigate to the `Backend/` directory:
   ```
   cd Backend
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Create a `.env` file in the `Backend/` directory with the following variables:
   ```
   MONGO_URI=mongodb://localhost:27017/your-database-name
   JWT_SECRET=your-jwt-secret
   PORT=3000
   ```
4. Start the development server:
   ```
   npm run dev
   ```

### Frontend Setup

1. Navigate to the `Frontend/` directory:
   ```
   cd Frontend
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm run dev
   ```

### Python Environment Setup

1. Ensure Python 3.x is installed.
2. Install required Python packages:
   ```
   pip install streamlit pymongo pandas scikit-learn
   ```
3. Ensure MongoDB is running locally or update the connection string in the Python files.

## Usage

1. **Streamlit Dashboard**: Run the main application:
   ```
   streamlit run app.py
   ```
   Access the dashboard at the provided URL (usually `http://localhost:8501`).

2. **Backend API**: The API will be running at `http://localhost:3000` (or the port specified in `.env`).

3. **Frontend**: Access the React app at the Vite dev server URL (usually `http://localhost:5173`).

4. **Additional Pages**: Open HTML files in `FRONTEND NEW/` directly in a browser for alternative interfaces.

## Data and Models

- The system uses pre-trained ML models for sentiment analysis and suggestion classification.
- CSV files contain sample data for events, feedback, and users.
- MongoDB is used for persistent storage of user data, events, and feedback.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the ISC License.
