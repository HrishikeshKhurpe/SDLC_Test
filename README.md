# Tools API

A simple REST API to demonstrate a basic application structure using FastAPI.

## Project Structure

```
/
|-- src/
|   |-- __init__.py
|   |-- main.py               # Main FastAPI application entry point
|   |-- services/
|   |   |-- __init__.py
|   |   |-- tool_service.py   # Business logic for tools
|   |-- models/
|   |   |-- __init__.py
|   |   |-- tool.py           # Pydantic data model for a Tool
|   |-- handlers/
|       |-- __init__.py
|       |-- tool_handler.py   # API route handlers for tools
|-- README.md
```

## API Endpoints

### Get All Tools

- **GET** `/api/v1/tools`
- **Description**: Retrieves a list of all available tools.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    [
      {
        "id": 1,
        "name": "Hammer",
        "description": "A tool for pounding nails."
      },
      {
        "id": 2,
        "name": "Screwdriver",
        "description": "A tool for turning screws."
      },
      {
        "id": 3,
        "name": "Wrench",
        "description": "A tool for gripping and turning nuts and bolts."
      }
    ]
    ```

## How to Run

1.  **Install dependencies**:
    ```bash
    pip install "fastapi[all]"
    ```

2.  **Start the server**:
    ```bash
    uvicorn src.main:app --reload
    ```

3.  **Access the API**:
    -   Open your browser to [http://127.0.0.1:8000/api/v1/tools](http://127.0.0.1:8000/api/v1/tools)
    -   Access the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
