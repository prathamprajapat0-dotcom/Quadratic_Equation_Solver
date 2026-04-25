This is a GUI-based Quadratic Equation Solver made using Python and Tkinter. The program helps users easily solve any quadratic equation of the form:

ax
2
+bx+c=0

The user only needs to enter the values of a, b, and c separated by commas (example: 1,5,6). After clicking the Solve button, the application calculates the discriminant and determines the nature of the roots.

🔹 Features:

✅ Full-screen interactive GUI using Tkinter
✅ Takes coefficient input in a simple comma-separated format
✅ Calculates the discriminant (b
2
−4ac)
✅ Detects the type of roots:

Real and Distinct Roots
Real and Equal Roots
No Real Roots

✅ Displays both roots if real roots exist
✅ Converts decimal roots into fraction form using Python’s Fraction module
✅ Shows error message if input is invalid

🔹 Working:

The program first checks the discriminant value:

If D>0: two real and different roots
If D=0: two real and equal roots
If D<0: no real roots

Then it calculates the roots using the quadratic formula:

x=
2a
−b±
D
	​

	​


If roots are real, they are displayed in fraction format.

🔹 Technologies Used:
Python
Tkinter (GUI Library)
fractions.Fraction module
