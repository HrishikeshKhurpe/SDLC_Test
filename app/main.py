import logging
from typing import List
from fastapi import FastAPI, HTTPException
from .services import tool_service
from .models.tool import Tool

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    """Returns a simple Hello World message."""
    return {"Hello": "World"}

@app.get("/tools", response_model=List[Tool])
def list_tools():
    """Lists all available tools."""
    try:
        return tool_service.get_tools()
    except Exception:
        logger.exception("Failed to get tools from service")
        raise HTTPException(status_code=500, detail="An internal server error occurred while fetching tools.")
