# SDLC_Test Calculator Application

## Overview

This repository contains a simple calculator application developed as part of an SDLC test. The application provides basic arithmetic operations through a command-line interface (CLI) and a graphical user interface (GUI).

**Recent Enhancements:**
The calculator now features an advanced expression evaluator capable of handling complex mathematical expressions, including operator precedence (e.g., multiplication and division before addition and subtraction), parentheses for grouping, and unary minus (e.g., `-5`, `-(2+3)`). The GUI has been improved with more specific error messages and a 'Clear' button for better user experience.

## Architecture

The application is structured into several key components:

-   `calculator/calculator.py`: Contains the core arithmetic logic (add, subtract, multiply, divide). This module is designed to be independent of the UI.
-   `calculator/ui_controller.py`: Acts as an intermediary between the UI and the core calculator logic. It is responsible for parsing and evaluating mathematical expressions using a robust shunting-yard-like algorithm, managing operator precedence, and handling unary minus. It also incorporates comprehensive error handling and logging for evaluation processes.
-   `calculator/ui.py`: Implements the Graphical User Interface (GUI) using Tkinter. It interacts with the `UIController` to process user input and display results. The UI now provides specific feedback for calculation errors and includes a 'Clear' button.
-   `calculator/cli.py`: (Assumed to exist, though not directly modified in this task) Provides a command-line interface for the calculator.
-   `calculator/tests/test_calculator.py`: Contains unit tests for both the `Calculator` core logic and the `UIController`'s expression evaluation. These tests cover basic operations, operator precedence, parentheses, unary minus, edge cases like division by zero, and various valid and invalid expression formats.

## Setup and Installation

To set up and run the application:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HrishikeshKhurpe/SDLC_Test.git
    cd SDLC_Test
    ```

2.  **Install dependencies:**
    ```bash
    pip install ruff # For linting
    ```
    (Note: The core calculator has no external dependencies beyond standard Python libraries.)

## How to Run

### GUI Application

To run the graphical user interface:
```bash
python calculator/ui.py
```

### Running Tests

To execute the unit tests:
```bash
python -m unittest calculator/tests/test_calculator.py
```

## Continuous Integration

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) to ensure code quality. This workflow automatically runs tests and linting checks on every push and pull request to the `main` branch. It is configured to fail the build if any tests fail or linting issues are detected, ensuring a high standard of code quality.

## Contributing

Contributions are welcome! Please ensure your code adheres to the existing style, includes comprehensive tests, and passes all CI checks.
