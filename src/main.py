from fastapi import FastAPI
from src.handlers import tool_handler

app = FastAPI(
    title="Tools API",
    description="A simple API to manage a list of tools.",
    version="1.0.0",
)

# Include the tool handler router
# All routes in tool_handler will be prefixed with /api/v1
app.include_router(tool_handler.router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint to welcome users to the API.
    """
    return {"message": "Welcome to the Tools API!"}
