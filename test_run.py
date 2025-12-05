#!/usr/bin/env python
import sys
import os
sys.path.append('src')

from surprise_travel.crew import SurpriseTravelCrew

def run():
    print("Starting Surprise Travel Crew...")
    
    inputs = {
        'origin': 'New York, JFK',
        'destination': 'Paris, CDG', 
        'age': 28,
        'hotel_location': 'Montmartre',
        'flight_information': 'Air France 123, leaving at March 15th, 2024, 14:00',
        'trip_duration': '7 days',
        'budget': '$2500'
    }
    
    print(f"Planning trip from {inputs['origin']} to {inputs['destination']}")
    print(f"Duration: {inputs['trip_duration']}")
    print("Initializing crew...")
    
    try:
        crew = SurpriseTravelCrew().crew()
        print("Crew initialized successfully!")
        print("Starting trip planning process...")
        
        result = crew.kickoff(inputs=inputs)
        print("\n" + "="*50)
        print("TRIP PLAN GENERATED!")
        print("="*50)
        print(result)
        
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run()