import tkinter as tk
from tkinter import messagebox as msg

from triangle import Triangle


class TriangleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Triangle Perimeter Calculator")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

        self.edges = []
        self.__create_widgets()

    def __create_widgets(self):
        self.input_label = tk.Label(self.root, text="Please enter the edge (1/3):")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(self.root, width=40)
        self.input_entry.pack(pady=5)

        self.add_edge_button = tk.Button(self.root, text="Add", command=self.__add_edge)
        self.add_edge_button.pack(pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate Perimeter", command=self.__calculate)
        self.calculate_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=5)

    def __add_edge(self):
        try:
            edge_str = self.input_entry.get().strip()
            if not edge_str:
                msg.showerror("Error", "Please enter a value.")
                return

            edge = float(edge_str)
            self.edges.append(edge)
            self.input_entry.delete(0, tk.END)

            if len(self.edges) < 3:
                self.input_label.config(text=f"Please enter the edge ({len(self.edges) + 1}/3):")
            else:
                self.input_label.config(text="Press 'Calculate Perimeter' to proceed!")
                self.input_entry.config(state="disabled")
                self.add_edge_button.config(state="disabled")
        except ValueError:
            msg.showerror("Error", "Invalid input. Please enter a valid number.")

    def __calculate(self):
        if len(self.edges) != 3:
            msg.showerror("Error", "Please enter all 3 edges.")
            return

        try:
            triangle = Triangle(*self.edges)
            perimeter = triangle.calculate_perimeter()
            msg.showinfo("Perimeter", f"Perimeter of the triangle is: {perimeter}")
            self.__continue()
        except ValueError as e:
            msg.showerror("Error", str(e), command=self.__continue)

    def __continue(self, event=None):
        result = msg.askyesno("Continue?", "Do you want to continue?")
        if result:
            self.edges.clear()
            self.input_entry.delete(0, tk.END)
            self.input_label.config(text="Please enter the edge (1/3):")
            self.input_entry.config(state="normal")
            self.add_edge_button.config(state="normal")
        else:
            self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    triangle_app = TriangleApp()
    triangle_app.run()
