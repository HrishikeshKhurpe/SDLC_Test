from typing import List
from src.models.tool import Tool

class ToolService:
    """
    Handles the business logic for tools.
    """
    def __init__(self):
        # In a real application, this data would come from a database,
        # configuration file, or another service.
        self._tools: List[Tool] = [
            Tool(id=1, name="Hammer", description="A tool for pounding nails."),
            Tool(id=2, name="Screwdriver", description="A tool for turning screws."),
            Tool(id=3, name="Wrench", description="A tool for gripping and turning nuts and bolts."),
        ]

    def get_all_tools(self) -> List[Tool]:
        """
        Retrieves all tools.
        
        Returns:
            A list of Tool objects.
        
        Raises:
            Exception: If there's an issue retrieving the tools.
        """
        try:
            # This is where you would typically have database query logic.
            return self._tools
        except Exception as e:
            # Log the error for debugging purposes
            print(f"Error fetching tools: {e}")
            # Re-raise the exception to be handled by the caller (e.g., the API handler)
            raise

# Singleton instance of the service to be used across the application.
# This is a simple approach for this example. For larger applications,
# dependency injection frameworks (like FastAPI's Depends) are recommended.
tool_service = ToolService()
