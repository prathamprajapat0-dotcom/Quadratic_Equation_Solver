import tkinter as tk    
from fractions import Fraction

# For making the GUI window
root = tk.Tk()
root.title("Quadtratic Equation Solver")
SWIDTH = root.winfo_screenwidth()
SHEIGHT = root.winfo_screenheight()
root.geometry(f"{SWIDTH}x{SHEIGHT}")

# For adding widgets
instruction = tk.Label(root, text="Enter the coefficients of the quadratic equation (a, b, c) separated by commas:", font="Arial 20")
instruction.pack(pady=20)

# For getting user Input
input_user = tk.Entry(root, width=50, font="Arial 20")
input_user.pack(pady=20)

solve_button = tk.Button(root, text="Solve", font="Arial 20", command=lambda: solve_quadratic(input_user.get()))
solve_button.pack(pady=20)

# Main working 
def solve_quadratic(user_input):
    try:
        for widget in root.winfo_children():
            if isinstance(widget, tk.Label) and widget != instruction and widget != solve_button and widget != input_user: # For destroying the last widget of no use
                widget.destroy()
        a,b,c = map(float, user_input.split(","))
        discriminant = b**2 - 4*a*c
        # For checking the condition
        if discriminant > 0:
            result =  tk.Label(root, text="The given Equation has real and distinct roots.", font="Arial 20")
            result.pack(pady=20)
        elif discriminant == 0:
            result = tk.Label(root, text="The given Equation has real and equal roots.", font="Arial 20")
            result.pack(pady=20)
        else:
            result = tk.Label(root, text="The given Equation has no real roots.", font="Arial 20")
            result.pack(pady=20)
        # For executing if the condition is True
        try:
            X1 = ((-b) + (discriminant**0.5))/(2*a)
            X2 = ((-b) - (discriminant**0.5))/(2*a)
            X1 = Fraction(X1)
            X2 = Fraction(X2)
            root_results = tk.Label(root, text=f"Roots: First Root = {X1}, \nSecond Root = {X2}", font="Arial 20")
            root_results.pack(pady=20)
        # If the condition goes false it direclty runs this line
        except ValueError:
            root_results = tk.Label(root, text="No real roots to display.", font="Arial 20")
            root_results.pack(pady=20)
# If the value is written in a wrong way this code runs 
    except ValueError:
        error_message = tk.Label(root, text="Invalid input. Please enter three numbers separated by commas.", font="Arial 20", fg="red")
        error_message.pack(pady=20)
root.mainloop() # For making the GUI on a loop

# Quadratic Equation Solver
# Author: Pratham.Deepak.Prajapt
# Email for paid projects:
# prathamprajapat0@gmail.com
