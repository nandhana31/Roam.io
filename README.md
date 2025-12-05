# Roamio - AI Travel Planning System

## Overview
Roamio is an AI-powered travel planning application that uses CrewAI to orchestrate multiple AI agents for creating comprehensive travel itineraries. The system considers activities, restaurants, budget optimization, weather conditions, and creates personalized day-by-day travel plans.

## Features
- **Activity Planning**: Personalized activity recommendations based on traveler preferences
- **Restaurant Discovery**: Curated dining experiences and local cuisine recommendations
- **Budget Optimization**: Smart cost management while maintaining quality experiences
- **Weather-Adaptive Planning**: Dynamic itinerary adjustments based on weather forecasts
- **Complete Itinerary**: Comprehensive day-by-day travel plans with all details

## Demo
https://github.com/user-attachments/assets/0cc0d6ce-7ae5-421c-b402-49c7aadd860a

## Prerequisites
- Python 3.10 or higher (up to 3.13)
- OpenAI API key
- Serper API key (for web search functionality)

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Roamio
```

### Step 2: Install Dependencies
You can use either Poetry or pip:

**Using pip:**
```bash
pip install crewai crewai-tools streamlit python-dotenv
```

**Using Poetry:**
```bash
poetry install
```

### Step 3: Configure API Keys
Create a `.env` file in the project root directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
```

Get your API keys:
- OpenAI API Key: https://platform.openai.com/api-keys
- Serper API Key: https://serper.dev/

## How to Run

### Option 1: Streamlit Web Application
Run the web-based user interface:

```bash
python -m streamlit run streamlit_app.py
```

Or if using conda/miniconda:
```bash
C:\Users\<username>\miniconda3\python.exe -m streamlit run streamlit_app.py
```

The application will open in your browser at `http://localhost:8501` or `http://localhost:8502`

### Option 2: Command Line Interface
Run the CLI version:

```bash
python -m src.main
```

Or using Poetry:
```bash
poetry run roamio
```

## Usage

### Web Interface
1. Launch the Streamlit app
2. Fill in the travel details:
   - Origin and destination airports
   - Traveler age
   - Preferred hotel area
   - Flight information
   - Trip duration (e.g., "7 days")
   - Budget (e.g., "$2500")
3. Click "Plan My Trip"
4. View your comprehensive travel itinerary

### Programmatic Usage
Edit `src/main.py` to customize travel parameters:

```python
travel_params = {
    'origin': 'New York, JFK',
    'destination': 'Paris, CDG',
    'age': 28,
    'hotel_location': 'Montmartre',
    'flight_information': 'Air France 123, leaving at March 15th, 2024, 14:00',
    'trip_duration': '7 days',
    'budget': '$2500'
}
```

## Project Structure
```
Roamio/
├── src/
│   ├── crew.py              
│   ├── main.py              
│   ├── config/
│   │   ├── agents.yaml      
│   │   └── tasks.yaml       
│   └── tools/
│       └── custom_tool.py   
├── streamlit_app.py         
├── pyproject.toml           
├── .env                    
└── README.md              
```

## AI Agents
The system uses five specialized AI agents:
1. **Activity Coordinator**: Plans personalized activities
2. **Dining Specialist**: Recommends restaurants and dining experiences
3. **Finance Manager**: Optimizes budget and finds cost-effective options
4. **Climate Analyst**: Adapts plans based on weather forecasts
5. **Schedule Organizer**: Compiles everything into a cohesive itinerary

## Troubleshooting

### Import Errors
If you get import errors, ensure all dependencies are installed:
```bash
pip install crewai crewai-tools streamlit python-dotenv
```

### API Key Errors
Verify your `.env` file exists in the project root and contains valid API keys.

### Python Version Issues
Ensure you're using Python 3.10-3.13:
```bash
python --version
```

