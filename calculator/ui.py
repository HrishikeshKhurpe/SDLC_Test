import tkinter as tk
import logging
from tkinter import messagebox
from .ui_controller import CalculatorUIController

# Configure logging for the main application entry point
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CalculatorUI:
    """
    Graphical User Interface for the calculator application.
    """

    def __init__(self, master):
        """
        Initializes the CalculatorUI.

        Args:
            master: The Tkinter root window.
        """
        self.master = master
        master.title("Calculator")
        self.controller = CalculatorUIController()
        self.expression = ""

        self.display = tk.Entry(master, width=30, borderwidth=5, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.display.insert(0, "0")

        self.create_buttons()

    def create_buttons(self):
        """
        Creates and places all calculator buttons on the UI.
        """
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('DEL', 5, 1) # Clear and Backspace buttons
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, padx=20, pady=20,
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure column and row weights so buttons expand proportionally
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(6): # Rows 0-5
            self.master.grid_rowconfigure(i, weight=1)

    def button_click(self, char: str):
        """
        Handles button clicks and updates the expression display.

        Args:
            char: The character corresponding to the clicked button.
        """
        current_display = self.display.get()
        is_operator = char in ['+', '-', '*', '/']
        
        # Determine if the last character in the current expression is an operator
        last_char_is_operator = self.expression and self.expression[-1] in ['+', '-', '*', '/']

        if char == 'C': # Clear button
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            logging.info("Clear button clicked. Expression reset.")
            return
        elif char == 'DEL': # Backspace button
            if self.expression:
                self.expression = self.expression[:-1]
                if not self.expression: # If expression becomes empty, show "0"
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "0")
                else:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, self.expression)
            logging.info(f"DEL button clicked. Expression: {self.expression}")
            return
        elif char == '=':
            self.evaluate()
            return
        elif char == '.':
            # If the expression is empty or ends with an operator, start with "0."
            if not self.expression or last_char_is_operator:
                self.expression += "0."
            else:
                # Find the last operator to determine the current number segment
                last_op_index = -1
                for op in ['+', '-', '*', '/']:
                    if op in self.expression:
                        r_index = self.expression.rfind(op)
                        if r_index > last_op_index:
                            last_op_index = r_index
                
                current_number_segment = self.expression[last_op_index + 1:]
                if '.' in current_number_segment:
                    logging.warning(f"Attempted to add multiple decimal points in current number segment: '{current_number_segment}'")
                    return # Already has a decimal in the current number segment
                else:
                    self.expression += char
        elif current_display == "0" and char != '.':
            # If display is "0" and a number is pressed, replace "0"
            # If an operator is pressed, and it's not '-', prevent it
            if is_operator and char != '-':
                logging.warning(f"Prevented starting expression with operator '{char}'.")
                return
            self.expression = char
        elif is_operator:
            # Prevent starting with an operator other than '-'
            if not self.expression and char != '-':
                logging.warning(f"Prevented starting expression with operator '{char}'.")
                return
            # If last char is an operator, replace it with the new one
            if last_char_is_operator:
                self.expression = self.expression[:-1] + char
            else:
                self.expression += char
        else:
            self.expression += char

        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        logging.info(f"Button '{char}' clicked. Expression: {self.expression}")

    def evaluate(self):
        """
        Evaluates the current expression using the controller and updates the display.
        Handles errors by showing a message box and resetting the expression.
        """
        try:
            result = self.controller.evaluate(self.expression)
            self.display.delete(0, tk.END)
            # Format result to avoid excessive decimal places for whole numbers
            if result == int(result):
                self.display.insert(0, str(int(result)))
                self.expression = str(int(result))
            else:
                self.display.insert(0, str(result))
                self.expression = str(result)
            logging.info(f"Expression '{self.expression}' evaluated to {result}")
        except ValueError as e:
            error_message = str(e)
            messagebox.showerror("Calculation Error", error_message)
            logging.error(f"Error during evaluation: {e}")
            self.expression = "" # Clear expression on error
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
        except Exception as e:
            messagebox.showerror("Unexpected Error", "An unexpected error occurred. Please try again.")
            logging.critical(f"An unexpected error occurred: {e}", exc_info=True)
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

def main():
    """
    Main function to initialize and run the calculator UI.
    """
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
