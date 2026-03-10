# SDLC_Test - Calculator Application

## Overview
This repository contains a simple calculator application built with Python and Tkinter. It demonstrates basic SDLC practices including code organization, testing, and robust error handling. The application provides a user-friendly interface for performing standard arithmetic operations.

## Architecture
The application follows a Model-View-Controller (MVC) like pattern to separate concerns:
-   `calculator/calculator.py`: **(Model)** Encapsulates the core arithmetic logic (e.g., add, subtract, multiply, divide). This module is purely functional and independent of the UI.
-   `calculator/ui_controller.py`: **(Controller)** Acts as an intermediary between the UI and the core calculator logic. It handles expression parsing, operator precedence, and delegates arithmetic operations to the `Calculator` class. It also manages error propagation from the core logic to the UI.
-   `calculator/ui.py`: **(View)** Implements the Tkinter-based graphical user interface. It captures user input, displays expressions and results, and presents error messages.

## Run Book

### How to Run
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HrishikeshKhurpe/SDLC_Test.git
    cd SDLC_Test
    ```
2.  **Run the application:**
    ```bash
    python calculator/ui.py
    ```

### How to Use
-   **Number Buttons (0-9):** Click to input digits.
-   **Operator Buttons (+, -, *, /):** Click to perform arithmetic operations. The controller handles operator precedence (e.g., multiplication and division before addition and subtraction).
-   **Decimal Point (.):** Use to input decimal numbers. The UI prevents multiple decimal points within a single number.
-   **Equals (=):** Click to evaluate the current expression and display the result.
-   **Clear (C):** Clears the entire expression and resets the display to "0".
-   **Backspace (DEL):** Removes the last character from the current expression. If the expression becomes empty, the display resets to "0".
-   **Display:** Shows the current expression or the result of the last calculation. Error messages will also appear here, accompanied by a pop-up.

## Testing
To run the unit tests:
```bash
python -m unittest discover calculator/tests
```
The tests cover the core arithmetic logic, expression parsing, operator precedence, and various edge cases including division by zero and invalid expression formats.

## Error Handling
The application includes robust error handling:
-   **Division by Zero:** Attempting to divide by zero will result in a specific error message.
-   **Invalid Expressions:** Malformed expressions (e.g., `10 +`, `abc`) are caught and reported with informative error messages.
-   **UI Feedback:** Errors are displayed both in the calculator's main display and via Tkinter `messagebox` pop-ups for clear user notification.
-   **Logging:** Detailed logs are generated for key operations and errors, aiding in debugging and monitoring.
