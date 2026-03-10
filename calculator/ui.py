import tkinter as tk
from tkinter import messagebox
import logging
from calculator.ui_controller import UIController
from calculator.calculator import Calculator # Assuming Calculator is needed for UIController init

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CalculatorUI:
    """
    Graphical User Interface for the calculator application.
    """
    def __init__(self, master: tk.Tk):
        """
        Initializes the CalculatorUI.

        Args:
            master: The root Tkinter window.
        """
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")
        master.resizable(False, False)

        self.calculator_instance = Calculator() # Create an instance of Calculator
        self.controller = UIController(self.calculator_instance)

        self.display_var = tk.StringVar()
        self.display_var.set("")

        self._create_widgets()

    def _create_widgets(self):
        """
        Creates and arranges all UI widgets (display, buttons).
        """
        # Display
        display_frame = tk.Frame(self.master, bd=4, relief="sunken")
        display_frame.pack(pady=10, padx=10, fill="x")

        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 24),
            anchor="e",
            bg="lightgray",
            height=2,
            padx=5
        )
        display_label.pack(expand=True, fill="both")

        # Buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10, padx=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('C', 5, 2) # Added 'C' button
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(button_frame, text=text, font=("Arial", 18), command=self.evaluate)
            elif text == 'C': # Handle 'C' button
                button = tk.Button(button_frame, text=text, font=("Arial", 18), command=self.clear_display)
            else:
                button = tk.Button(button_frame, text=text, font=("Arial", 18), command=lambda t=text: self.append_to_display(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Configure grid weights for responsive layout
        for i in range(5): # 5 rows for buttons
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4): # 4 columns for buttons
            button_frame.grid_columnconfigure(i, weight=1)

    def append_to_display(self, value: str):
        """
        Appends a character or number to the current display.

        Args:
            value: The string to append to the display.
        """
        current_text = self.display_var.get()
        # Prevent multiple leading zeros unless it's a decimal
        if current_text == "0" and value.isdigit() and value != "0" and "." not in current_text:
            self.display_var.set(value)
        elif current_text == "0" and value == "0":
            pass # Do nothing, keep single zero
        else:
            self.display_var.set(current_text + value)
        logging.info(f"Appended '{value}'. Display: {self.display_var.get()}")

    def clear_display(self):
        """
        Clears the calculator display.
        """
        self.display_var.set("")
        logging.info("Display cleared.")

    def evaluate(self):
        """
        Evaluates the expression currently in the display using the UIController.
        Displays the result or an error message.
        """
        expression = self.display_var.get()
        if not expression:
            messagebox.showwarning("Input Error", "Please enter an expression.")
            logging.warning("Attempted to evaluate empty display.")
            return

        try:
            result = self.controller.evaluate(expression)
            self.display_var.set(str(result))
            logging.info(f"Expression '{expression}' evaluated to '{result}'.")
        except ValueError as e:
            messagebox.showerror("Calculation Error", str(e))
            logging.error(f"Error evaluating expression '{expression}': {e}")
        except Exception as e:
            messagebox.showerror("An unexpected error occurred", "Please check the expression.")
            logging.critical(f"Unexpected error during evaluation of '{expression}': {e}", exc_info=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()
