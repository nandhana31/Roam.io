import streamlit as st
import sys
import os
from dotenv import load_dotenv

load_dotenv()

from src.crew import TravelPlanningCrew
import json

st.set_page_config(
    page_title="Surprise Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Surprise Travel Planner")
st.markdown("Plan your perfect surprise trip with AI-powered travel agents!")

with st.form("travel_form"):
    form_col1, form_col2 = st.columns(2)
    
    with form_col1:
        departure_city = st.text_input("Origin (Airport Code)", value="New York, JFK", placeholder="e.g., New York, JFK")
        arrival_city = st.text_input("Destination (Airport Code)", value="Paris, CDG", placeholder="e.g., Paris, CDG")
        traveler_age = st.number_input("Age", min_value=1, max_value=100, value=28)
    
    with form_col2:
        preferred_area = st.text_input("Preferred Hotel Area", value="Montmartre", placeholder="e.g., Montmartre")
        flight_details = st.text_input("Flight Information", value="Air France 123, leaving at March 15th, 2024, 14:00")
        travel_length = st.text_input("Trip Duration", value="7 days", placeholder="e.g., 7 days")
        total_budget = st.text_input("Budget", value="$2500", placeholder="e.g., $2500")
    
    form_submitted = st.form_submit_button("🚀 Plan My Trip", use_container_width=True)

if form_submitted:
    travel_params = {
        'origin': departure_city,
        'destination': arrival_city,
        'age': traveler_age,
        'hotel_location': preferred_area,
        'flight_information': flight_details,
        'trip_duration': travel_length,
        'budget': total_budget
    }
    
    with st.spinner("🤖 AI agents are planning your surprise trip..."):
        try:
            planning_crew = TravelPlanningCrew().crew()
            trip_result = planning_crew.kickoff(inputs=travel_params)
            
            st.success("🎉 Your surprise trip has been planned!")
            
            if hasattr(trip_result, 'json_dict') and trip_result.json_dict:
                trip_plan = trip_result.json_dict
                
                st.header(f"🎯 {trip_plan.get('itinerary_title', 'Your Trip Itinerary')}")
                
                if 'accommodation_info' in trip_plan:
                    st.subheader("🏨 Hotel")
                    st.info(trip_plan['accommodation_info'])
                
                if 'schedule_list' in trip_plan:
                    st.subheader("📅 Daily Itinerary")
                    
                    for day_index, daily_plan in enumerate(trip_plan['schedule_list']):
                        with st.expander(f"Day {day_index+1}: {daily_plan.get('schedule_date', f'Day {day_index+1}')}"):
                            
                            if daily_plan.get('weather'):
                                weather_data = daily_plan['weather']
                                weather_col1, weather_col2 = st.columns(2)
                                with weather_col1:
                                    st.markdown(f"🌤️ **Weather:** {weather_data.get('condition', 'N/A')}")
                                    st.markdown(f"🌡️ **Temperature:** {weather_data.get('temperature', 'N/A')}")
                                with weather_col2:
                                    if weather_data.get('packing_recommendation'):
                                        st.markdown(f"🎒 **Pack:** {weather_data['packing_recommendation']}")
                            
                            if daily_plan.get('flight_details'):
                                st.markdown(f"✈️ **Flight:** {daily_plan['flight_details']}")
                            
                            if daily_plan.get('daily_activities'):
                                st.markdown("🎯 **Activities:**")
                                for single_activity in daily_plan['daily_activities']:
                                    activity_category = "🏠 Indoor" if single_activity.get('indoor') else "🌞 Outdoor"
                                    st.markdown(f"- {activity_category} **{single_activity.get('activity_name', 'Activity')}** at {single_activity.get('activity_location', 'Location')}")
                                    st.markdown(f"  {single_activity.get('activity_description', '')}")
                                    if single_activity.get('user_rating'):
                                        st.markdown(f"  ⭐ Rating: {single_activity['user_rating']}")
                                    if single_activity.get('cost'):
                                        st.markdown(f"  💰 Cost: {single_activity['cost']}")
                            
                            if daily_plan.get('dining_options'):
                                st.markdown("🍽️ **Restaurants:**")
                                for dining_place in daily_plan['dining_options']:
                                    st.markdown(f"- {dining_place}")
                            
                            if daily_plan.get('daily_budget'):
                                st.markdown(f"💰 **Daily Budget:** {daily_plan['daily_budget']}")
                
                if 'total_budget' in trip_plan:
                    st.subheader("💰 Budget Summary")
                    budget_col1, budget_col2, budget_col3 = st.columns(3)
                    with budget_col1:
                        st.metric("Total Budget", trip_plan.get('total_budget', total_budget))
                    with budget_col2:
                        st.metric("Estimated Cost", trip_plan.get('estimated_cost', 'N/A'))
                    with budget_col3:
                        budget_remaining = trip_plan.get('remaining_budget', 'N/A')
                        st.metric("Remaining", budget_remaining)
                
                if 'weather_summary' in trip_plan:
                    st.subheader("🌤️ Weather Overview")
                    st.info(trip_plan['weather_summary'])
            
            else:
                st.subheader("📋 Trip Plan")
                st.markdown(str(trip_result))
                
        except Exception as error:
            st.error(f"❌ Error: {str(error)}")
            st.info("💡 Make sure your API keys are properly configured in the .env file")

with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This app uses CrewAI to orchestrate five AI agents:
    
    🎯 **Activity Planner**  
    Finds activities matching your interests
    
    🍽️ **Restaurant Scout**  
    Discovers great dining experiences
    
    💰 **Budget Optimizer**  
    Optimizes costs while maintaining quality
    
    🌤️ **Weather-Adaptive Planner**  
    Adapts activities based on weather forecasts
    
    📋 **Itinerary Compiler**  
    Creates your complete travel plan
    """)
    
    st.header("⚙️ Configuration")
    st.markdown("""
    Make sure to set your API keys in `.env`:
    - `OPENAI_API_KEY`
    - `SERPER_API_KEY`
    """)
    
    st.header("🌤️ Weather Features")
    st.markdown("""
    - Daily weather forecasts
    - Indoor/outdoor activity suggestions
    - Packing recommendations
    - Weather-adapted itinerary
    """)
    
    st.header("💰 Budget Features")
    st.markdown("""
    - Cost optimization
    - Daily budget breakdown
    - Money-saving alternatives
    - Budget tracking
    """)