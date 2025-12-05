#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv
load_dotenv()

print("=" * 60)
print("🌍 SURPRISE TRAVEL PLANNER")
print("=" * 60)
print()

openai_key = os.getenv('OPENAI_API_KEY')
serper_key = os.getenv('SERPER_API_KEY')

if not openai_key:
    print("ERROR: OPENAI_API_KEY not found in .env file")
    sys.exit(1)

if not serper_key:
    print("⚠️  WARNING: SERPER_API_KEY not found in .env file")
    print("   Web search functionality may be limited")
    print()

print("API Keys loaded successfully")
print()

try:
    from surprise_travel.crew import SurpriseTravelCrew
    print("Modules imported successfully")
    print()
except ImportError as e:
    print(f"ERROR importing modules: {e}")
    print()
    print("Please run: poetry install")
    sys.exit(1)

# Trip inputs
inputs = {
    'origin': 'New York, JFK',
    'destination': 'Paris, CDG', 
    'age': 28,
    'hotel_location': 'Montmartre',
    'flight_information': 'Air France 123, leaving at March 15th, 2024, 14:00',
    'trip_duration': '7 days',
    'budget': '$2500'
}

print("📋 Trip Details:")
print(f"   From: {inputs['origin']}")
print(f"   To: {inputs['destination']}")
print(f"   Duration: {inputs['trip_duration']}")
print(f"   Budget: {inputs['budget']}")
print()
print("-" * 60)
print()

print("🚀 Initializing AI crew...")
try:
    crew = SurpriseTravelCrew().crew()
    print(" Crew initialized successfully!")
    print()
    print("🤖 AI agents are planning your trip...")
    print("   This may take a few minutes...")
    print()
    
    result = crew.kickoff(inputs=inputs)
    
    print()
    print("=" * 60)
    print("🎉 TRIP PLAN GENERATED!")
    print("=" * 60)
    print()
    print(result)
    print()
    
except Exception as e:
    print()
    print("=" * 60)
    print(" ERROR occurred:")
    print("=" * 60)
    print(f"{type(e).__name__}: {e}")
    print()
    import traceback
    traceback.print_exc()
    sys.exit(1)

print()
print("=" * 60)
print(" Process completed!")
print("=" * 60)
