import tkinter as tk
from calculator.calculator import Hrishikesh_Calculator
from calculator.ui_controller import CalculatorUIController

class CalculatorUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hrishikesh's Calculator")
        
        self.calculator_controller = CalculatorUIController()
        
        self.create_widgets()
        self.root.mainloop()
        
    def create_widgets(self):
        """Create the UI elements for the calculator."""
        self.display = tk.Entry(self.root, width=25, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "+", "="
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                tk.Button(self.root, text=button, width=5, height=2, command=self.evaluate).grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(self.root, text=button, width=5, height=2, command=lambda x=button: self.add_to_display(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
    def add_to_display(self, value):
        """Add the clicked button value to the display."""
        self.display.insert(tk.END, value)
        
    def evaluate(self):
        """Evaluate the expression in the display and update the result."""
        try:
            expression = self.display.get()
            result = str(self.calculator_controller.evaluate(expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            logging.error(f"Error evaluating expression: {expression}, {e}")
