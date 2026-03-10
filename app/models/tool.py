from pydantic import BaseModel

class Tool(BaseModel):
    """Pydantic model for a tool."""
    name: str
