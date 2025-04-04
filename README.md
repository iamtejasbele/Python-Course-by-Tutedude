# Python-Course-by-Tutedude
# Assignments and Task during Course Work





# ASSIGNMENT 1:
# Module 2: Basic Python Concepts






# Task 1: Perform Basic Mathematical Operations
This Python script performs basic mathematical operations on two user-input integers: addition, subtraction, multiplication, and division.
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
This Python script determines whether a given number is even or odd, with added error handling to manage invalid user input.

Functionality:
1. User Input Handling:  
   - The program prompts the user to enter a test number (`n`).
   - It attempts to convert the input into an integer using `int(input(...))`.
   - If the input is not a valid integer (e.g., letters or symbols), an error message is displayed instead of crashing.

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
    - Input: `n = 5`
    - Factorial Calculation:
      \[
      5! = 5 × 4 × 3 × 2 × 1 = 120
      \]
    - Output: `Factorial of 5 = 120`
- The function uses recursion to repeatedly call itself until the base case (`n < 2`) is reached.

Example Runs:

Enter a number: 5
Factorial of 5 =  120


Enter a number: 0
Factorial of 0 =  1


Enter a number: 1
Factorial of 1 =  1




#   Task 2: Using the Math Module for Calculations

The given Python program takes a number as input from the user and checks if it is positive. If the number is positive, it calculates and prints:  
1. Square Root  
2. Natural Logarithm (ln)  
3. Sine Value 

If the number is zero or negative, it prints an error message asking the user to enter a positive value.  

Breakdown of the Code: 

1. User Input:
  
   n = float(input('Enter the number: '))
   - The program asks the user to enter a number.  
   - The input is converted to a floating-point number (`float`) and stored in variable `n`.

2. Checking if the Number is Positive:
  if n > 0:
    - The program checks if `n` is greater than 0 (i.e., positive).  
   - If true, the program proceeds to mathematical calculations.  

3. Importing the Math Module & Performing Calculations:
   import math
   print(f'Square root of {n} =', math.sqrt(n))
   print(f'Natural log of {n} =', math.log(n, math.e))
   print(f'Sine of {n} =', math.sin(n))
    - The `math` module is imported inside the `if` block to perform calculations.  
   - `math.sqrt(n)` calculates the square root of `n`.  
   - `math.log(n, math.e)` computes the natural logarithm (ln) of `n` (logarithm base `e`).  
   - `math.sin(n)` calculates the sine of `n` (assuming `n` is in radians).  

4. Handling Negative and Zero Inputs:
   else:
       print('Enter the positive value')
    - If `n` is zero or negative, the program prints `"Enter the positive value"` instead of performing calculations.  

Functionality of the Code: 
- This program ensures that mathematical calculations (square root, log, sine) are only performed on positive numbers.  
- If the input is negative or zero, it prevents errors and asks the user to enter a valid positive number.  


Example Runs:  

Example 1: Valid Input (Positive Number) 

Enter the number: 25
Square root of 25.0 = 5.0
Natural log of 25.0 = 3.2188758248682006
Sine of 25.0 = -0.13235175009777303


Example 2: Valid Input (Positive Decimal)  

Enter the number: 1.57
Square root of 1.57 = 1.2529964086141666
Natural log of 1.57 = 0.4519851237430572
Sine of 1.57 = 0.9999996829318346


Example 3: Invalid Input (Negative Number)  

Enter the number: -5
Enter the positive value

- The program does not attempt calculations and simply prompts the user to enter a positive number.

Example 4: Invalid Input (Zero)  

Enter the number: 0
Enter the positive value

- Logarithm (`log(0)`) is undefined or zero, so the program prevents calculations.




# ASSIGNMENT 4:
# Module 5: Files, Exceptions, and Errors in Python


# Task 1: Read a File and Handle Errors 
This Python script attempts to open and read a text file named `sample.txt`. It reads the file line by line and prints each line with a corresponding line number. If the file is not found, it handles the exception and displays an error message.

Breakdown of Code:
1. Try Block (`try:`)
   - The script attempts to open a file named `sample.txt` in read mode (`'r'`).  
   - If the file exists, it reads all the lines into a list called `reading_file` using `readlines()`.

2. Loop Through the File (`for i in reading_file:`)  
   - A counter variable `n` is initialized to 0.  
   - The loop iterates through each line in `reading_file`, increments `n` by 1, and prints the line number along with the content.

3. File Closing (`file1.close()`)  
   - After reading, the file is closed to free system resources.

4. Exception Handling (`except:`) 
   - If the file `sample.txt` is not found, the script catches the exception and prints an error message:  
     
     Error: The file sample.txt is not found
     

Example Output:
If `sample.txt` contains:
Hello, World!
This is a sample text file.
Python is fun.

The output would be:

Line 1: Hello, World!
Line 2: This is a sample text file.
Line 3: Python is fun.


If the file is not found, 

the output would be:
Error: The file sample.txt is not found



# Task 2: Write and Append Data to a File

This Python script performs the following tasks:  

1. Takes user input and writes it to a file named `output.txt` (overwriting any existing content).  
2. Appends additional user input to the same file without overwriting the existing content.  
3. Reads and displays the final content of the file.  

Code Breakdown:

1. Writing to the File (`'w'` mode)

file1 = open('output.txt','w')
file1.write(input('Enter text to write to the file:')+'\n')
print('Data successfully written to output.txt')
file1.close()

- Opens `output.txt` in write mode (`'w'`), which overwrites any existing content.  
- Takes user input via `input()`, appends a newline (`'\n'`), and writes it to the file.  
- Prints a confirmation message and closes the file to save the data properly.  

2. Appending to the File (`'a'` mode)

file1 = open('output.txt','a')
file1.write(input('Enter additional text to append:'))
print('Data successfully appended')
file1.close()

- Opens `output.txt` in append mode (`'a'`), which adds new content to the existing file without erasing it.  
- Takes additional user input and writes it to the file.  
- Prints a confirmation message and closes the file.  


3. Reading from the File (`'r'` mode)

file1 = open('output.txt','r')
reading_file = file1.read()
print('Final content of output.txt')
print(reading_file)
file1.close()

- Opens `output.txt` in read mode (`'r'`) to read its entire content.  
- Reads the content and stores it in the variable `reading_file`.  
- Prints the final content of the file.  
- Closes the file after reading.  

 Example Run:

Enter text to write to the file: Hello, this is the first line.
Data successfully written to output.txt


Enter additional text to append: This is the second line.
Data successfully appended

Final content of output.txt:
Hello, this is the first line.
This is the second line.




# ASSIGNMENT 5:

# Module 6: Data Structures and Strings in Python
 


# Task 1: Create a Dictionary of Student Marks

Description

- `marks_entry`: A dictionary storing student names as keys and their corresponding marks as values.
  
- `marks_entry.keys()`: Retrieves and displays all the keys (student names) from the dictionary.

- `input()`: Prompts the user to input a student name.

- `.capitalize()`: This method ensures that the first letter of the entered name is uppercase and the rest are lowercase, improving matching accuracy (e.g., "alice", "ALICE", "Alice" → "Alice").

- `try` block: Attempts to find and print the marks of the student entered.

- `except KeyError`: Executes when the name is not found in the dictionary, printing an error message and reminding the user to refer to the given list.


Functionality

1. Displays Available Students:
   - Shows the list of student names in the dictionary using `marks_entry.keys()`.

2. Takes User Input:
   - The user is asked to input a student's name.

3. Handles Case Sensitivity:
   - Uses `.capitalize()` to reduce errors due to incorrect casing in input.

4. Checks and Prints Marks:
   - If the name exists (after capitalization), prints the marks.
   - If not, catches the `KeyError` and prints an error message.

5. Improved User Guidance:
   - On failure, reminds the user to refer to the displayed list.

Example Outputs

Case 1: Correct Name, Wrong Case

Student's Name Present in Data: dict_keys(['Alice', 'Mike', 'Kelly', 'Steve', 'Dino'])
Enter the student's Name: mike
mike's marks is: 50


Case 2: Invalid Name

Student's Name Present in Data: dict_keys(['Alice', 'Mike', 'Kelly', 'Steve', 'Dino'])
Enter the student's Name: John
Student not found
Enter the student's name from the List of Names given above





# Task 2: Demonstrate List Slicing 

Explanation

`list_original = list(range(1,11))`
- Creates a list of integers from 1 to 10.
- `range(1, 11)` generates numbers from 1 (inclusive) to 11 (exclusive).
- The `list()` function converts the range into a list.

- Result:  

  list_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


`print('Original List:', list_original)`
- Prints the original list:

  Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


`first5 = list_original[0:5]`
- Uses list slicing to extract the first 5 elements.
- `0:5` means start at index 0 and go up to (but not including) index 5.
- Result:

  first5 = [1, 2, 3, 4, 5]


`print('Extracted first 5 elements:', first5)`
- Prints the extracted sublist:

  Extracted first 5 elements: [1, 2, 3, 4, 5]


`rev = first5[::-1]`
- Uses slicing with step `-1` to reverse the list.
- `[::-1]` starts from the end of the list and moves backward.
- This does not modify the original list; it creates a new reversed list.
- Result:

  rev = [5, 4, 3, 2, 1]


`print('Reverse extracted elements:', rev)`

- Prints the reversed list:

  Reverse extracted elements: [5, 4, 3, 2, 1]



Program Output


Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first 5 elements: [1, 2, 3, 4, 5]
Reverse extracted elements: [5, 4, 3, 2, 1]

Functionality Summary

- Demonstrates list creation, slicing, and reversing using slicing (`[::-1]`).
- Does not modify the original list.
- `rev` is a new list containing the reversed values of `first5`.




