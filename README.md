# Hrishikesh's Calculator with UI

## Overview
This project provides a visually appealing UI for the existing Hrishikesh's Calculator application. The UI allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division, and displays the results on the screen.

## File Structure
```
calculator/
├── ui.py
├── ui_controller.py
├── calculator.py
└── tests/
    └── test_ui.py
```

## Test Case Structure
The tests for the calculator UI functionality are located in the `calculator/tests/test_ui.py` file. The test suite covers the following operations:

- `test_add`
- `test_subtract`
- `test_multiply`
- `test_divide`
- `test_error_handling`

To run the tests, use the following command:

```
python -m unittest discover -s calculator/tests -p 'test_*.py'
```

## Run Book
To use the Hrishikesh's Calculator UI, follow these steps:

1. Run the `ui.py` file:

   ```
   python calculator/ui.py
   ```

2. The calculator UI will be displayed, and you can perform various arithmetic operations by clicking the buttons on the screen.

## Dependencies
This project requires the following dependencies:

- Python 3.7 or higher
- tkinter (comes pre-installed with Python)

## Setup Instructions
1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory in your terminal.
4. You can now run the `ui.py` file to start the calculator UI.

## Architecture
The calculator UI is implemented using the Tkinter library, which provides a cross-platform GUI toolkit for Python. The `CalculatorUI` class in `ui.py` is responsible for creating the UI elements and handling user interactions.

The `CalculatorUIController` class in `ui_controller.py` acts as an intermediary between the UI and the `Hrishikesh_Calculator` class, which contains the core calculator logic. This separation of concerns allows for better testability and maintainability of the application.

The test suite in `test_ui.py` ensures the correct integration between the UI and the calculator logic, and verifies the overall functionality of the calculator UI.
