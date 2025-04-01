# Python-Course-by-Tutedude
# Assignments and Task during Course Work

# Task 1: Perform Basic Mathematical Operations
This Python script performs **basic mathematical operations** on two user-input integers: **addition, subtraction, multiplication, and division**.
Functionality:
1. User Input: 
   - The program prompts the user to enter two numbers (`a` and `b`).
   - `int(input(...))` ensures that the input is converted into an integer.

2. Operations Performed:
   - Addition (`a + b`): Computes the sum of the two numbers.
   - Subtraction (`a - b`): Computes the difference between the two numbers.
   - Multiplication (`a * b`): Computes the product of the two numbers.
   - Division (`a / b`): Computes the quotient of `a` divided by `b`.
          The try block attempts to perform the division. If b is 0, a ZeroDivisionError is raised.
          The except block catches the error and prints a user-friendly message instead of stopping execution.

3. Output Display:  
   - The results of all operations are printed to the console in a readable format.

Example Execution:
Enter the first number: 10
Enter the second number: 5
Addition = 15
Subtraction = 5
Multiplication = 50
Division = 2.0

# Task 2: Create a Personalized Greeting
This Python script is designed to generate a personalized greeting for the user by taking their first name and last name as input and then displaying a friendly welcome message.

Functionality:
1. User Input:
   - The program prompts the user to enter their first name (`First_Name`).
   - Then, it asks for their last name (`Last_Name`).

2. String Formatting and Output:
   - The program constructs a greeting message using f-string formatting (`f'...'`).
   - The message includes `"Hello,"`, the user's first name, last name, and a welcome message.
   - The final message is displayed using the `print()` function.

Example Execution:
User Input
Enter Your First Name: Tejas
Enter Your Last Name: Bele

Output
Hello, Tejas Bele! Welcome to Python Programming Course.
