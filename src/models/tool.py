from pydantic import BaseModel

class Tool(BaseModel):
    """
    Represents a single tool in the system.
    """
    id: int
    name: str
    description: str
