from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List, Optional

class TravelActivity(BaseModel):
    activity_name: str = Field(..., description="Name of the activity")
    activity_location: str = Field(..., description="Location of the activity")
    activity_description: str = Field(..., description="Description of the activity")
    activity_date: str = Field(..., description="Date of the activity")
    cuisine_type: str = Field(..., description="Cuisine of the restaurant")
    suitability_reason: str = Field(..., description="Why it's suitable for the traveler")
    user_reviews: Optional[List[str]] = Field(..., description="List of reviews")
    user_rating: Optional[float] = Field(..., description="Rating of the activity")

class DailySchedule(BaseModel):
	schedule_date: str = Field(..., description="Date of the day")
	daily_activities: List[TravelActivity] = Field(..., description="List of activities")
	dining_options: List[str] = Field(..., description="List of restaurants")
	flight_details: Optional[str] = Field(None, description="Flight information")

class TripItinerary(BaseModel):
  itinerary_title: str = Field(..., description="Name of the itinerary, something funny")
  schedule_list: List[DailySchedule] = Field(..., description="List of day plans")
  accommodation_info: str = Field(..., description="Hotel information")

@CrewBase
class TravelPlanningCrew():
    config_agents = 'config/agents.yaml'
    config_tasks = 'config/tasks.yaml'

    @agent
    def activity_coordinator(self) -> Agent:
        return Agent(
            config=self.config_agents['personalized_activity_planner'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def dining_specialist(self) -> Agent:
        return Agent(
            config=self.config_agents['restaurant_scout'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def finance_manager(self) -> Agent:
        return Agent(
            config=self.config_agents['budget_optimizer'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def climate_analyst(self) -> Agent:
        return Agent(
            config=self.config_agents['weather_adaptive_planner'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def schedule_organizer(self) -> Agent:
        return Agent(
            config=self.config_agents['itinerary_compiler'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False,
        )

    @task
    def activity_planning_operation(self) -> Task:
        return Task(
            config=self.config_tasks['personalized_activity_planning_task'],
            agent=self.activity_coordinator()
        )

    @task
    def dining_discovery_operation(self) -> Task:
        return Task(
            config=self.config_tasks['restaurant_scenic_location_scout_task'],
            agent=self.dining_specialist()
        )

    @task
    def budget_management_operation(self) -> Task:
        return Task(
            config=self.config_tasks['budget_optimization_task'],
            agent=self.finance_manager()
        )

    @task
    def weather_planning_operation(self) -> Task:
        return Task(
            config=self.config_tasks['weather_adaptive_planning_task'],
            agent=self.climate_analyst()
        )

    @task
    def itinerary_assembly_operation(self) -> Task:
        return Task(
            config=self.config_tasks['itinerary_compilation_task'],
            agent=self.schedule_organizer(),
            output_json=TripItinerary
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
