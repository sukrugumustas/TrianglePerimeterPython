# Triangle Perimeter Calculator (Python)

This project provides a simple graphical user interface (GUI) for calculating the perimeter of a triangle using Python and Tkinter.

## Features

*   User-friendly GUI for entering triangle side lengths.
*   Input validation to ensure valid positive numeric values are entered.
*   Checks for the triangle inequality to ensure the entered sides can form a valid triangle.
*   Clear message boxes for displaying results and error messages.
*   Option to continue with new calculations or exit the application.

## Getting Started

### Prerequisites

You need to have Python installed on your system. This project uses the built-in `tkinter` library, so no additional installations are required for basic functionality.

### Running the Application

1.  Clone or download this repository.
2.  Navigate to the project directory in your terminal or command prompt.
3.  Run the application using:

    ```bash
    python triangle_app.py
    ```

## Usage

1.  Enter the length of each side in the corresponding text entry boxes.
2.  Click the "Add" button to add the side to the calculation.
3.  The prompt will update to ask for the next side length.
4.  Once all three sides are entered, the "Calculate Perimeter" button becomes active.
5.  Click "Calculate Perimeter" to display the result.
6.  A message box will show the calculated perimeter or an error message if the input is invalid.
7.  A confirmation dialog will appear, asking if you want to continue.

## Code Structure

*   `triangle_app.py`: Contains the main application logic, GUI setup using Tkinter, and event handling.
*   `triangle.py`: Defines the `Triangle` class, which handles triangle validation and perimeter calculation.

## Example

Here's a simple example of how to use the `Triangle` class directly (without the GUI):

```python
from triangle import Triangle

try:
    triangle = Triangle(*[3.0, 4.0, 5.0])
    perimeter = triangle.calculate_perimeter()
    print(f"The perimeter is: {perimeter}")  # Output: The perimeter is: 12.0

    triangle = Triangle(*[1.0, 2.0, 5.0])  # Invalid triangle
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: The edges do not form a valid triangle.
except TypeError as e:
    print(f"Error: {e}") # Output if there is a wrong type of input.
except ArithmeticError as e:
    print(f"Error: {e}")
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or bug fixes.
