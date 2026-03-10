# Simple Calculator API

This is a simple Flask-based API that performs basic arithmetic operations.

## Project Structure

- `src/main.py`: The main entry point for the Flask application.
- `src/calculator/routes.py`: Defines the API endpoints for the calculator.
- `src/calculator/service.py`: Contains the business logic for the calculations.
- `tests/test_calculator.py`: Unit and integration tests for the calculator API.
- `requirements.txt`: Python dependencies.
- `README.md`: This file.

## Setup and Running the Application

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python src/main.py
    ```
    The application will be running on `http://127.0.0.1:5000`.

## API Endpoint

### `POST /calculator/calculate`

Performs a calculation.

**Request Body (JSON):**

```json
{
  "operand1": "<number>",
  "operand2": "<number>",
  "operation": "<string>"
}
```

-   `operand1`, `operand2`: The numbers to operate on.
-   `operation`: The operation to perform. Supported operations are `add`, `subtract`, `multiply`, `divide`.

**Success Response (200 OK):**

```json
{
  "result": "<number>"
}
```

**Error Response (400 Bad Request):**

```json
{
  "error": "<error_message>"
}
```

**Example using cURL:**

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"operand1": 10, "operand2": 5, "operation": "add"}' \
http://127.0.0.1:5000/calculator/calculate
```

## Running Tests

To run the tests, use pytest:

```bash
pytest
```
