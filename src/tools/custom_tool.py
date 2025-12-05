from crewai_tools import BaseTool


class CustomTravelTool(BaseTool):
    tool_name: str = "Custom Travel Tool"
    tool_description: str = (
        "A custom tool for travel planning operations and data processing."
    )

    def _run(self, input_parameter: str) -> str:
        return "Custom tool execution completed successfully."
