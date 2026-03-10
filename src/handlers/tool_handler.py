from fastapi import APIRouter
from typing import List
from src.models.tool import Tool
from src.services.tool_service import tool_service

router = APIRouter()

@router.get("/tools", response_model=List[Tool], summary="Get all tools", tags=["Tools"])
async def get_tools():
    """
    Retrieve a list of all available tools.
    """
    try:
        return tool_service.get_all_tools()
    except Exception as e:
        # In a real-world scenario, you would have more specific exception handling
        # and logging. For this example, we'll re-raise a generic error.
        # from fastapi import HTTPException
        # raise HTTPException(status_code=500, detail="Could not retrieve tools.")
        print(f"An error occurred: {e}")
        raise
