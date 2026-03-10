# Calculator API

A simple REST API for a calculator built with FastAPI.

## Features

- Perform basic arithmetic operations: add, subtract, multiply, divide.
- JSON-based API.
- Error handling for invalid operations and division by zero.

## API Endpoint

### `POST /calculator`

Performs a calculation.

**Request Body:**

```json
{
  "number1": 10,
  "number2": 5,
  "operation": "divide"
}
```

- `number1` (float, required): The first number.
- `number2` (float, required): The second number.
- `operation` (string, required): The operation to perform. Must be one of `"add"`, `"subtract"`, `"multiply"`, `"divide"`.

**Success Response (200 OK):**

```json
{
  "result": 2.0
}
```

**Error Response (400 Bad Request):**

For division by zero.

```json
{
  "detail": "Division by zero is not allowed."
}
```

**Error Response (422 Unprocessable Entity):**

For invalid request body (e.g., wrong data types, missing fields, or invalid operation).

```json
{
    "detail": [
        {
            "loc": [
                "body",
                "operation"
            ],
            "msg": "unexpected value; permitted: 'add', 'subtract', 'multiply', 'divide'",
            "type": "value_error.const"
        }
    ]
}
```

## Setup and Running the Application

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**

    The application is located in `src/calculator/main.py`. To run it with Uvicorn:

    ```bash
    uvicorn src.calculator.main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

3.  **API Documentation:**

    Once the server is running, interactive API documentation (Swagger UI) is available at `http://127.0.0.1:8000/docs`.

## Running Tests

To run the unit tests, use pytest:

```bash
pytest
```
