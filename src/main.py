#!/usr/bin/env python
import sys
from src.crew import TravelPlanningCrew


def run():
    travel_params = {
        'origin': 'São Paulo, GRU',
        'destination': 'New York, JFK',
        'age': 31,
        'hotel_location': 'Brooklyn',
        'flight_information': 'GOL 1234, leaving at June 30th, 2024, 10:00',
        'trip_duration': '14 days',
        'budget': '$3000'
    }
    planning_result = TravelPlanningCrew().crew().kickoff(inputs=travel_params)
    print(planning_result)


def train():
    training_params = {
        'origin': 'São Paulo, GRU',
        'destination': 'New York, JFK',
        'age': 31,
        'hotel_location': 'Brooklyn',
        'flight_information': 'GOL 1234, leaving at June 30th, 2024, 10:00',
        'trip_duration': '14 days',
        'budget': '$3000'
    }
    try:
        TravelPlanningCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=training_params)
    except Exception as error:
        raise Exception(f"An error occurred while training the crew: {error}")
