# Python-Course-by-Tutedude
# Assignments and Task during Course Work





# ASSIGNMENT 1:
# Module 2: Basic Python Concepts






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





# ASSIGNMENT 2:
# Module 3: Control Structures in Python

# Task 1: Check if a Number is Even or Odd
This Python script determines whether a given number is **even or odd**, with added error handling to manage invalid user input.

Functionality:
1. User Input Handling:  
   - The program prompts the user to enter a test number (`n`).
   - It attempts to convert the input into an integer using `int(input(...))`.
   - If the input is not a valid integer (e.g., letters or symbols), an **error message is displayed** instead of crashing.

2. Even-Odd Check using Modulus Operator (`%`): 
   - If `n % 2 == 0`, the number is even.
   - Otherwise, the number is odd.

3. Error Handling:  
   - The `try-except` block prevents the program from crashing if the user enters non-numeric input.
   - If an error occurs (e.g., the user enters `"abc"` instead of a number), the `except` block prints:  
     `"Error: Enter the valid input"`

4. Formatted Output using f-strings: 
   - The output message is dynamically formatted using f-strings, making it more readable.

Example Execution:
#1 Valid Even Number Input:
Enter the Test Number: 8
8 is an Even number

#2 Valid Odd Number Input:
Enter the Test Number: 7
7 is an Odd number

#3 Invalid Input (Non-Numeric):
Enter the Test Number: hello
Error: Enter the valid input






# Task 2: Sum of Integers from 1 to 50 Using a Loop
This Python script calculates the sum of integers from 1 to 50 using a loop.

Functionality:
1. Creating a List of Numbers (Range Function):  
   - `list(range(1, 51, 1))` generates a list of numbers from `1` to `50`.
   - The `range(1, 51, 1)` function produces numbers starting from `1` up to `50`, with a step of `1`.

2. Initializing the Sum Variable: 
   - `sum = 0` initializes the sum to zero before starting the loop.

3. Looping Through the List to Calculate the Sum: 
   - A `for` loop iterates through the list of numbers (`c`).
   - Inside the loop, each number (`i`) is added to `sum`.
   - `sum = sum + i` (or `sum += i`) updates the cumulative total.

4. Displaying the Final Sum:  
   - After the loop completes, the total sum is printed using an f-string.

Example Execution Output:
Sum of numbers from 1 to 50 is: 1275






# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python 




# Task 1: Calculate Factorial Using a Function 
The given Python program calculates the factorial of a given number using a recursive function. The user inputs a number, and the program computes its factorial using the `factorial()` function.

Breakdown of the Code:
1. User Input:
   n = int(input('Enter a number:'))
   - The program prompts the user to enter a number.
   - The input is converted into an integer and stored in the variable `n`.

2. Factorial Function Definition:
   def factorial(n):
   - A function named `factorial()` is defined, which takes one parameter, `n`.

3. Base Case (Stopping Condition):
   if n < 2:
       return 1
   - If `n` is less than 2 (i.e., `n = 0` or `n = 1`), the function returns `1` as the factorial of `0` and `1` is `1`.

4. Recursive Case:
   else:
       return n * (factorial(n-1))
   - If `n` is greater than 1, the function calls itself recursively with `n-1`, multiplying the current value of `n` by the factorial of `n-1`.

5. Function Call and Output:
   ans = factorial(n)
   print(f'Factorial of {n} = ', ans)
   - The function `factorial(n)` is called, and the result is stored in the variable `ans`.
   - The calculated factorial is displayed using `print()`.

Functionality of the Code:
- The code calculates the factorial of a number using recursion.
- Factorial is defined as:
  \[
  n! = n \times (n-1) \times (n-2) \times ... \times 1
  \]
  - Example:
    - **Input:** `n = 5`
    - **Factorial Calculation:**
      \[
      5! = 5 × 4 × 3 × 2 × 1 = 120
      \]
    - Output: `Factorial of 5 = 120`
- The function uses **recursion** to repeatedly call itself until the base case (`n < 2`) is reached.

Example Runs:

Enter a number: 5
Factorial of 5 =  120


Enter a number: 0
Factorial of 0 =  1


Enter a number: 1
Factorial of 1 =  1
