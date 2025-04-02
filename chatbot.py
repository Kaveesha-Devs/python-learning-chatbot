import time

# ========== Shared Helper Functions ==========
def print_answer_correct():
    print("\n🎉 Congratulations! You are correct.\n")
    print("➡️ Moving to the next question...\n")
    time.sleep(1)

def print_answer_incorrect(user_answer, correct_answer, explanation):
    print(f"\n❌ Incorrect! You chose: {user_answer}\n✅ The correct answer is: {correct_answer}\nℹ️ Explanation: {explanation}\n")

def ask_question(question, options, correct_option, explanation):
    print(question)
    for key, value in options.items():
        print(f"{key}) {value}")
    answer = input("\nYour Answer: ").lower()
    if answer == correct_option:
        print_answer_correct()
    else:
        print_answer_incorrect(answer, correct_option.upper() + ") " + options[correct_option], explanation)

# ========== Topic Modules ==========
# ---------- 01. Introduction ----------
def python_intro():
    print("\n📌 Concept: Introduction to Python\n")
    print("Python is a high-level, interpreted programming language, known for its simplicity and readability.")
    print("It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.")
    print("Python syntax is clean and easy to understand, making it an excellent choice for beginners.")
    print("Example:")
    print("""
# Simple Python program
print("Hello, World!")""")
    ask_question("What is the main reason Python is considered beginner-friendly?", 
                 {"a": "It is a compiled language", "b": "It has simple and readable syntax", "c": "It is hard to learn"}, 
                 "b", 
                 "Python's syntax is simple and easy to read, making it great for beginners.")

def python_data_types():
    print("\n📌 Concept: Python Data Types\n")
    print("Python has built-in data types that can hold different types of data. Common data types include:")
    print("- `int` for integers")
    print("- `float` for floating-point numbers")
    print("- `str` for strings")
    print("- `list` for ordered collections")
    print("Example:")
    print("""
x = 5  # integer
y = 3.14  # float
name = 'John'  # string
fruits = ['apple', 'banana', 'cherry']  # list""")
    ask_question("Which of the following is not a valid Python data type?", 
                 {"a": "int", "b": "string", "c": "decimal"}, 
                 "c", 
                 "Python doesn't have a `decimal` data type; it uses `float` for decimal numbers.")

def python_variables():
    print("\n📌 Concept: Python Variables\n")
    print("A variable is a name given to a value. It can be used to store different types of data.")
    print("You can create variables in Python without declaring their data type.")
    print("Example:")
    print("""
x = 10  # integer
name = 'Alice'  # string""")
    ask_question("Which of the following is a valid variable assignment in Python?", 
                 {"a": "10 = x", "b": "x = 10", "c": "int x = 10"}, 
                 "b", 
                 "In Python, you assign values to variables using the '=' operator.")

# ---------- 02. Variables ----------
def variable_concept():
    print("\n📌 Concept: Variables\n")
    print("A variable is a container for storing data values. It holds data that can be used and modified during program execution.")
    print("Example:")
    print("x = 5  # An integer value assigned to x")
    print("y = 'Hello'  # A string value assigned to y\n")
    ask_question("Which of the following is a valid variable declaration in Python?", 
                 {"a": "5 = x", "b": "x = 5", "c": "int x = 5"}, 
                 "b", 
                 "Variables in Python are assigned using '=', and there is no need to declare the type explicitly.")

def naming_rules():
    print("\n📌 Concept: Rules for Naming Variables\n")
    print("Variable names must start with a letter or underscore and cannot be Python keywords.")
    print("Example:")
    print("_name = 'Alice'  # Valid")
    print("age1 = 25  # Valid\n")
    ask_question("Which of the following is an invalid variable name?", 
                 {"a": "my_var", "b": "2ndVar", "c": "_privateVar"}, 
                 "b", 
                 "Variable names cannot start with a number in Python.")

def data_types():
    print("\n📌 Concept: Different Data Types in Variables\n")
    print("Python has several data types: int, float, str, list, tuple, dict, etc.")
    print("Example:")
    print("num = 10  # Integer")
    print("price = 99.99  # Float")
    print("name = 'Alice'  # String\n")
    ask_question("What is the type of the variable 'price' if price = 99.99?", 
                 {"a": "int", "b": "float", "c": "str"}, 
                 "b", 
                 "Decimals are represented as float data types in Python.")

def variable_reassignment():
    print("\n📌 Concept: Changing Variable Values (Reassignment)\n")
    print("A variable can be reassigned a new value anytime in the program.")
    print("Example:")
    print("x = 10  # Initially x is 10")
    print("x = 'changed'  # Now x holds a string value\n")
    ask_question("What will be the final value of x in this case: x = 5; x = 10?", 
                 {"a": "5", "b": "10", "c": "Error"}, 
                 "b", 
                 "The last assigned value (10) is the final value of x.")

def multiple_assignment():
    print("\n📌 Concept: Assigning Multiple Variables\n")
    print("Python allows multiple assignments in a single line.")
    print("Example:")
    print("a, b, c = 1, 2, 3  # Assigning values to multiple variables in one line\n")
    ask_question("What will be the value of b after this assignment: a, b, c = 1, 2, 3?", 
                 {"a": "1", "b": "2", "c": "3"}, 
                 "b", 
                 "The variables are assigned values in order: a=1, b=2, c=3.")

def variable_scope():
    print("\n📌 Concept: Variable Scope (Global vs Local)\n")
    print("Variables can be local (inside a function) or global (outside all functions).")
    print("Example:")
    print("global_var = 'I am global'  # This variable can be accessed anywhere")
    print("def my_function():")
    print("    local_var = 'I am local'  # This variable is only accessible inside this function\n")
    ask_question("Where can a local variable be accessed?", 
                 {"a": "Anywhere", "b": "Only inside the function where it's defined", "c": "Only outside functions"}, 
                 "b", 
                 "Local variables exist only within the function they are defined in.")

# ---------- 03. Input/Output ----------
def input_function():
    print("\n📌 Concept: Taking User Input\n")
    print("The input() function is used to take user input in Python.")
    print("Example:")
    print("name = input('Enter your name: ')  # Takes user input as a string\n")
    ask_question("What is the default data type of input() in Python?", 
                 {"a": "int", "b": "str", "c": "float"}, 
                 "b", 
                 "The input() function always returns a string. You must convert it if needed.")

def print_function():
    print("\n📌 Concept: Displaying Output\n")
    print("The print() function is used to display output in Python.")
    print("Example:")
    print("print('Hello, World!')  # Displays Hello, World!\n")
    ask_question("Which function is used to display output in Python?", 
                 {"a": "print()", "b": "output()", "c": "display()"}, 
                 "a", 
                 "The correct function for displaying output is print().")

def formatted_output():
    print("\n📌 Concept: Formatting Output\n")
    print("You can use f-strings or format() to format output in Python.")
    print("Example:")
    print("name = 'Alice'")
    print("print(f'Hello, {name}!')  # f-string formatting\n")
    ask_question("Which method is the most modern way to format strings in Python?", 
                 {"a": "Using + for concatenation", "b": "Using % formatting", "c": "Using f-strings"}, 
                 "c", 
                 "f-strings are the most modern and readable way to format strings in Python (introduced in Python 3.6).")

# ---------- 04. Operators ----------
def arithmetic_operators():
    print("\n📌 Concept: Arithmetic Operators\n")
    print("Arithmetic operators are used to perform basic mathematical operations.")
    print("Example:")
    print("a = 5")
    print("b = 3")
    print("sum = a + b  # Addition")
    print("diff = a - b  # Subtraction")
    print("prod = a * b  # Multiplication")
    print("div = a / b  # Division\n")
    ask_question("Which operator is used for division in Python?", 
                 {"a": "/", "b": "*", "c": "-"}, 
                 "a", 
                 "The '/' operator is used for division.")

def comparison_operators():
    print("\n📌 Concept: Comparison Operators\n")
    print("Comparison operators are used to compare two values.")
    print("Example:")
    print("a = 5")
    print("b = 3")
    print("print(a > b)  # True\n")
    ask_question("Which operator is used to check if a value is greater than another?", 
                 {"a": ">", "b": "<", "c": "=="}, 
                 "a", 
                 "The '>' operator checks if a value is greater than another.")

def logical_operators():
    print("\n📌 Concept: Logical Operators\n")
    print("Logical operators are used to combine conditional statements.")
    print("Example:")
    print("x = True")
    print("y = False")
    print("print(x and y)  # False")
    print("print(x or y)   # True\n")
    ask_question("Which operator is used to combine conditions to check if both are True?", 
                 {"a": "or", "b": "and", "c": "not"}, 
                 "b", 
                 "The 'and' operator returns True if both conditions are True.")

def assignment_operators():
    print("\n📌 Concept: Assignment Operators\n")
    print("Assignment operators are used to assign values to variables.")
    print("Example:")
    print("x = 5  # Assigns 5 to x")
    print("x += 2  # Adds 2 to x\n")
    ask_question("What does 'x += 3' do?", 
                 {"a": "Assigns 3 to x", "b": "Adds 3 to x", "c": "Multiplies x by 3"}, 
                 "b", 
                 "'x += 3' adds 3 to the current value of x.")

# ---------- 05. Conditional Statements ----------
def if_statement():
    print("\n📌 Concept: if Statement\n")
    print("The 'if' statement is used to test a condition. If the condition is True, the code inside the if block will be executed.")
    print("Example:")
    print("x = 5")
    print("if x > 0:")
    print("    print('Positive number')  # This will print because x is positive\n")
    ask_question("Which statement is used to check if a condition is True?", 
                 {"a": "if", "b": "else", "c": "for"}, 
                 "a", 
                 "The 'if' statement is used to check conditions in Python.")

def elif_statement():
    print("\n📌 Concept: elif Statement\n")
    print("The 'elif' statement is used to check multiple conditions. It allows you to test multiple possibilities after the initial 'if'.")
    print("Example:")
    print("x = 0")
    print("if x > 0:")
    print("    print('Positive number')")
    print("elif x == 0:")
    print("    print('Zero')  # This will print because x is equal to 0\n")
    ask_question("What will the following code print if x = 0?\nif x > 0:\n    print('Positive number')\nelif x == 0:\n    print('Zero')", 
                 {"a": "Positive number", "b": "Zero", "c": "Error"}, 
                 "b", 
                 "The 'elif' block will execute when the 'if' condition is False, and the condition for 'elif' is True.")

def else_statement():
    print("\n📌 Concept: else Statement\n")
    print("The 'else' statement is used to execute code when all previous conditions (if/elif) are False.")
    print("Example:")
    print("x = -1")
    print("if x > 0:")
    print("    print('Positive number')")
    print("else:")
    print("    print('Negative number')  # This will print because x is negative\n")
    ask_question("What will the following code print if x = -1?\nif x > 0:\n    print('Positive number')\nelse:\n    print('Negative number')", 
                 {"a": "Positive number", "b": "Negative number", "c": "Zero"}, 
                 "b", 
                 "The 'else' block will execute when the 'if' condition is False.")

def nested_statements():
    print("\n📌 Concept: Nested if Statements\n")
    print("You can nest if statements inside other if statements to check multiple conditions.")
    print("Example:")
    print("x = 10")
    print("if x > 0:")
    print("    if x > 5:")
    print("        print('x is greater than 5')  # This will print because x is 10\n")
    ask_question("What will the following code print if x = 10?\nif x > 0:\n    if x > 5:\n        print('x is greater than 5')", 
                 {"a": "x is greater than 5", "b": "x is positive", "c": "No output"}, 
                 "a", 
                 "The nested 'if' checks if x is greater than 5, and since x is 10, it will print 'x is greater than 5'.")

# ---------- 06. Loops ----------
def for_loop():
    print("\n📌 Concept: for Loop\n")
    print("The 'for' loop is used to iterate over a sequence (like a list, tuple, dictionary, or string).")
    print("Example:")
    print("for i in range(5):")
    print("    print(i)  # This will print numbers 0 to 4\n")
    ask_question("Which keyword is used to create a 'for' loop?", 
                 {"a": "for", "b": "while", "c": "loop"}, 
                 "a", 
                 "The 'for' keyword is used to create a for loop in Python.")

def while_loop():
    print("\n📌 Concept: while Loop\n")
    print("The 'while' loop repeats a block of code as long as the given condition is True.")
    print("Example:")
    print("x = 0")
    print("while x < 5:")
    print("    print(x)")
    print("    x += 1  # This will print numbers 0 to 4\n")
    ask_question("What will be printed by the following code?\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1", 
                 {"a": "0 1 2", "b": "1 2 3", "c": "0 1 2 3"}, 
                 "a", 
                 "The while loop will print 0, 1, and 2 because the condition x < 3 is True for those values.")

def break_statement():
    print("\n📌 Concept: break Statement\n")
    print("The 'break' statement is used to exit the loop prematurely.")
    print("Example:")
    print("for i in range(10):")
    print("    if i == 5:")
    print("        break  # The loop will stop when i equals 5\n")
    ask_question("What will be the value of i when the loop breaks?\nfor i in range(10):\n    if i == 5:\n        break", 
                 {"a": "5", "b": "10", "c": "0"}, 
                 "a", 
                 "The loop will break when i equals 5, so it will stop and print 5.")

def continue_statement():
    print("\n📌 Concept: continue Statement\n")
    print("The 'continue' statement skips the rest of the code inside the loop for the current iteration and goes to the next iteration.")
    print("Example:")
    print("for i in range(5):")
    print("    if i == 3:")
    print("        continue  # The loop will skip printing 3\n")
    ask_question("What will the following code print?\nfor i in range(5):\n    if i == 3:\n        continue\n    print(i)", 
                 {"a": "0 1 2 3 4", "b": "0 1 2 4", "c": "1 2 3 4"}, 
                 "b", 
                 "The continue statement will skip printing 3, so the output will be 0 1 2 4.")
    
# ---------- 07. Functions ----------
def function_definition():
    print("\n📌 Concept: Function Definition\n")
    print("A function is a block of code that only runs when it is called.")
    print("Example:")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')  # This function greets the user\n")
    ask_question("Which keyword is used to define a function?", 
                 {"a": "def", "b": "function", "c": "define"}, 
                 "a", 
                 "In Python, we use the keyword 'def' to define a function.")

def function_parameters():
    print("\n📌 Concept: Function Parameters\n")
    print("Parameters are variables that are passed to a function.")
    print("Example:")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')  # 'name' is the parameter\n")
    ask_question("What is the purpose of a parameter in a function?", 
                 {"a": "To define the function", "b": "To pass values to the function", "c": "To store return values"}, 
                 "b", 
                 "Parameters are used to pass values to the function so that it can operate on those values.")

def function_return_value():
    print("\n📌 Concept: Function Return Value\n")
    print("Functions can return values using the 'return' statement.")
    print("Example:")
    print("def add(a, b):")
    print("    return a + b  # The function returns the sum of a and b\n")
    ask_question("What will be the result of this function call: add(3, 4)?", 
                 {"a": "7", "b": "34", "c": "None"}, 
                 "a", 
                 "The function adds 3 and 4 and returns 7.")

def function_scope():
    print("\n📌 Concept: Function Scope\n")
    print("A variable inside a function is local to that function and cannot be accessed outside.")
    print("Example:")
    print("def my_function():")
    print("    x = 10  # x is local to my_function\n")
    print("print(x)  # This will raise an error because x is local to the function\n")
    ask_question("What will happen if you try to access a variable outside its function scope?", 
                 {"a": "It will work", "b": "It will raise an error", "c": "It will return None"}, 
                 "b", 
                 "Variables defined inside a function are local to that function and cannot be accessed outside.")

# ---------- 08. Lists & Tuples ----------
def lists_concept():
    print("\n📌 Concept: Lists\n")
    print("A list is a collection of ordered, changeable, and indexed items. It can hold items of different data types.")
    print("Example:")
    print("fruits = ['apple', 'banana', 'cherry']  # List of strings")
    print("numbers = [1, 2, 3, 4]  # List of integers\n")
    ask_question("Which of the following is a valid list declaration in Python?", 
                 {"a": "fruits = (1, 2, 3)", "b": "fruits = [1, 2, 3]", "c": "fruits = {1, 2, 3}"}, 
                 "b", 
                 "Lists in Python are defined using square brackets '[]'.")

def accessing_list_elements():
    print("\n📌 Concept: Accessing List Elements\n")
    print("You can access elements in a list by their index (starting from 0).")
    print("Example:")
    print("fruits = ['apple', 'banana', 'cherry']")
    print("print(fruits[1])  # This will print 'banana'\n")
    ask_question("What will be the output of fruits[2] if fruits = ['apple', 'banana', 'cherry']?", 
                 {"a": "'apple'", "b": "'banana'", "c": "'cherry'"}, 
                 "c", 
                 "Index 2 corresponds to the third item in the list, which is 'cherry'.")

def modifying_lists():
    print("\n📌 Concept: Modifying Lists\n")
    print("Lists are mutable, meaning you can change the values of items after creation.")
    print("Example:")
    print("fruits = ['apple', 'banana', 'cherry']")
    print("fruits[1] = 'blueberry'  # Modify the second item\n")
    ask_question("What will the list 'fruits' contain after this modification: fruits = ['apple', 'banana', 'cherry']; fruits[1] = 'blueberry'?", 
                 {"a": "['apple', 'banana', 'cherry']", "b": "['apple', 'blueberry', 'cherry']", "c": "['blueberry', 'banana', 'cherry']"}, 
                 "b", 
                 "The second item in the list is modified to 'blueberry'.")

def tuples_concept():
    print("\n📌 Concept: Tuples\n")
    print("A tuple is similar to a list, but it is immutable (cannot be modified). It is defined using parentheses '()'.")
    print("Example:")
    print("coordinates = (1, 2, 3)  # A tuple containing 3 integers\n")
    ask_question("Which of the following is the correct syntax to define a tuple?", 
                 {"a": "coordinates = [1, 2, 3]", "b": "coordinates = {1, 2, 3}", "c": "coordinates = (1, 2, 3)"}, 
                 "c", 
                 "Tuples are defined using parentheses '()'.")

def tuple_accessing_elements():
    print("\n📌 Concept: Accessing Tuple Elements\n")
    print("You can access elements in a tuple in the same way as in a list (by index). However, tuples are immutable, so you can't modify them.")
    print("Example:")
    print("coordinates = (1, 2, 3)")
    print("print(coordinates[1])  # This will print 2\n")
    ask_question("What will be the output of coordinates[0] if coordinates = (1, 2, 3)?", 
                 {"a": "1", "b": "2", "c": "3"}, 
                 "a", 
                 "The element at index 0 in the tuple is 1.")

# ---------- 09. Dictionaries ----------
def dictionaries_concept():
    print("\n📌 Concept: Dictionaries\n")
    print("A dictionary is an unordered collection of items. It stores key-value pairs, where each key is unique.")
    print("Example:")
    print("person = {'name': 'Alice', 'age': 25, 'city': 'New York'}  # A dictionary with keys and values\n")
    ask_question("Which of the following is the correct way to define a dictionary in Python?", 
                 {"a": "person = {'name': 'Alice', 'age': 25}", "b": "person = ['name': 'Alice', 'age': 25]", "c": "person = ('name', 'Alice', 'age', 25)"}, 
                 "a", 
                 "Dictionaries are defined using curly braces '{}' and consist of key-value pairs.")

def accessing_dict_elements():
    print("\n📌 Concept: Accessing Dictionary Elements\n")
    print("You can access dictionary values using their keys.")
    print("Example:")
    print("person = {'name': 'Alice', 'age': 25}")
    print("print(person['name'])  # This will print 'Alice'\n")
    ask_question("What will be the output of person['age'] if person = {'name': 'Alice', 'age': 25}?", 
                 {"a": "Alice", "b": "25", "c": "Error"}, 
                 "b", 
                 "The value of the key 'age' is 25.")

def modifying_dict_elements():
    print("\n📌 Concept: Modifying Dictionary Elements\n")
    print("You can modify dictionary values by accessing the key and assigning a new value.")
    print("Example:")
    print("person = {'name': 'Alice', 'age': 25}")
    print("person['age'] = 26  # Modifying the value of 'age'\n")
    ask_question("What will be the value of person['age'] after this modification: person = {'name': 'Alice', 'age': 25}; person['age'] = 26?", 
                 {"a": "25", "b": "26", "c": "Error"}, 
                 "b", 
                 "The value of 'age' is updated to 26.")

def adding_dict_elements():
    print("\n📌 Concept: Adding New Elements to Dictionaries\n")
    print("You can add new key-value pairs to a dictionary by assigning a value to a new key.")
    print("Example:")
    print("person = {'name': 'Alice', 'age': 25}")
    print("person['city'] = 'New York'  # Adding a new key-value pair\n")
    ask_question("What will the dictionary 'person' contain after this addition: person = {'name': 'Alice', 'age': 25}; person['city'] = 'New York'?", 
                 {"a": "{'name': 'Alice', 'age': 25, 'city': 'New York'}", "b": "{'name': 'Alice', 'age': 25}", "c": "{'name': 'Alice', 'age': 25, 'city': '25'}"}, 
                 "a", 
                 "A new key-value pair ('city': 'New York') is added to the dictionary.")

def removing_dict_elements():
    print("\n📌 Concept: Removing Elements from Dictionaries\n")
    print("You can remove key-value pairs using the 'del' keyword or the 'pop()' method.")
    print("Example:")
    print("person = {'name': 'Alice', 'age': 25}")
    print("del person['age']  # This will remove the key-value pair with key 'age'\n")
    ask_question("What will be the dictionary 'person' after removing the 'age' key: person = {'name': 'Alice', 'age': 25}; del person['age']?", 
                 {"a": "{'name': 'Alice'}", "b": "{'name': 'Alice', 'age': 25}", "c": "{'age': 25, 'name': 'Alice'}"}, 
                 "a", 
                 "The key-value pair with key 'age' is removed.")
    
# ========== Main Menu Handlers ==========
def handle_introduction(score):
    while True:
        print("\nChoose a topic to learn about Python:")
        print("1) Introduction to Python")
        print("2) Python Data Types")
        print("3) Python Variables")
        print("4) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            python_intro()
            score += 1
        elif choice == '2':
            python_data_types()
            score += 1
        elif choice == '3':
            python_variables()
            score += 1
        elif choice == '4':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_variables(score):
    while True:
        print("\nChoose a topic to learn about Variables:")
        print("1) What is a Variable?")
        print("2) Rules for Naming Variables")
        print("3) Different Data Types in Variables")
        print("4) Changing Variable Values (Reassignment)")
        print("5) Assigning Multiple Variables")
        print("6) Variable Scope (Global vs Local)")
        print("7) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            variable_concept()
            score += 1
        elif choice == '2':
            naming_rules()
            score += 1
        elif choice == '3':
            data_types()
            score += 1
        elif choice == '4':
            variable_reassignment()
            score += 1
        elif choice == '5':
            multiple_assignment()
            score += 1
        elif choice == '6':
            variable_scope()
            score += 1
        elif choice == '7':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_input_output(score):
    while True:
        print("\nChoose a topic to learn about Input & Output:")
        print("1) Taking User Input")
        print("2) Displaying Output")
        print("3) Formatting Output")
        print("4) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            input_function()
            score += 1
        elif choice == '2':
            print_function()
            score += 1
        elif choice == '3':
            formatted_output()
            score += 1
        elif choice == '4':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_operators(score):
    while True:
        print("\nChoose a topic to learn about Operators:")
        print("1) Arithmetic Operators")
        print("2) Comparison Operators")
        print("3) Logical Operators")
        print("4) Assignment Operators")
        print("5) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            arithmetic_operators()
            score += 1
        elif choice == '2':
            comparison_operators()
            score += 1
        elif choice == '3':
            logical_operators()
            score += 1
        elif choice == '4':
            assignment_operators()
            score += 1
        elif choice == '5':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_conditionals(score):
    while True:
        print("\nChoose a topic to learn about Conditional Statements:")
        print("1) if Statement")
        print("2) elif Statement")
        print("3) else Statement")
        print("4) Nested if Statements")
        print("5) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            if_statement()
            score += 1
        elif choice == '2':
            elif_statement()
            score += 1
        elif choice == '3':
            else_statement()
            score += 1
        elif choice == '4':
            nested_statements()
            score += 1
        elif choice == '5':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_loops(score):
    while True:
        print("\nChoose a topic to learn about Loops:")
        print("1) for Loop")
        print("2) while Loop")
        print("3) break Statement")
        print("4) continue Statement")
        print("5) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            for_loop()
            score += 1
        elif choice == '2':
            while_loop()
            score += 1
        elif choice == '3':
            break_statement()
            score += 1
        elif choice == '4':
            continue_statement()
            score += 1
        elif choice == '5':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_functions(score):
    while True:
        print("\nChoose a topic to learn about Functions:")
        print("1) Function Definition")
        print("2) Function Parameters")
        print("3) Function Return Value")
        print("4) Function Scope")
        print("5) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            function_definition()
            score += 1
        elif choice == '2':
            function_parameters()
            score += 1
        elif choice == '3':
            function_return_value()
            score += 1
        elif choice == '4':
            function_scope()
            score += 1
        elif choice == '5':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_lists_tuples(score):
    while True:
        print("\nChoose a topic to learn about Lists and Tuples:")
        print("1) Lists in Python")
        print("2) Accessing List Elements")
        print("3) Modifying Lists")
        print("4) Tuples in Python")
        print("5) Accessing Tuple Elements")
        print("6) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            lists_concept()
            score += 1
        elif choice == '2':
            accessing_list_elements()
            score += 1
        elif choice == '3':
            modifying_lists()
            score += 1
        elif choice == '4':
            tuples_concept()
            score += 1
        elif choice == '5':
            tuple_accessing_elements()
            score += 1
        elif choice == '6':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_dictionaries(score):
    while True:
        print("\nChoose a topic to learn about Dictionaries:")
        print("1) Dictionaries in Python")
        print("2) Accessing Dictionary Elements")
        print("3) Modifying Dictionary Elements")
        print("4) Adding New Elements to Dictionaries")
        print("5) Removing Elements from Dictionaries")
        print("6) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            dictionaries_concept()
            score += 1
        elif choice == '2':
            accessing_dict_elements()
            score += 1
        elif choice == '3':
            modifying_dict_elements()
            score += 1
        elif choice == '4':
            adding_dict_elements()
            score += 1
        elif choice == '5':
            removing_dict_elements()
            score += 1
        elif choice == '6':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_exceptions(score):
    while True:
        print("\nChoose a topic to learn about Exception Handling:")
        print("1) Exception Handling in Python")
        print("2) Handling Multiple Exceptions")
        print("3) Using 'else' Clause in Exception Handling")
        print("4) Using 'finally' Clause in Exception Handling")
        print("5) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            exception_handling_concept()
            score += 1
        elif choice == '2':
            multiple_exceptions()
            score += 1
        elif choice == '3':
            else_clause_in_exception_handling()
            score += 1
        elif choice == '4':
            finally_clause_in_exception_handling()
            score += 1
        elif choice == '5':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")

def handle_file_handling(score):
    while True:
        print("\nChoose a topic to learn about File Handling:")
        print("1) Reading from Files")
        print("2) Writing to Files")
        print("3) Appending to Files")
        print("4) Reading Lines from Files")
        print("5) Closing a File")
        print("6) Return to Main Menu\n")
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            file_reading_concept()
            score += 1
        elif choice == '2':
            file_writing_concept()
            score += 1
        elif choice == '3':
            file_append_concept()
            score += 1
        elif choice == '4':
            file_read_lines()
            score += 1
        elif choice == '5':
            file_closing()
            score += 1
        elif choice == '6':
            return score
        else:
            print("❌ Invalid choice. Please choose again.\n")            
# ========== Main Function ==========
def main():
    score = 0
    while True:
        print("\n🤖 Welcome to the Python Learning Chatbot!")
        print(f"\n📚 Current Score: {score} points")
        print("\nMain Menu - Choose a Topic:")
        print("1. Introduction to Python")
        print("2. Variables")
        print("3. Input and Output")
        print("4. Operators")
        print("5. Conditional Statements")
        print("6. Loops")
        print("7. Functions")
        print("8. Lists & Tuples")
        print("9. Dictionaries")
        print("10. Exception Handling")
        print("11. File Handling")
        print("12. Exit\n")
        
        choice = input("Enter the number of your choice: ")
        
        handlers = {
            '1': handle_introduction,
            '2': handle_variables,
            '3': handle_input_output,
            '4': handle_operators,
            '5': handle_conditionals,
            '6': handle_loops,
            '7': handle_functions,
            '8': handle_lists_tuples,
            '9': handle_dictionaries,
            '10': handle_exceptions,
            '11': handle_file_handling
        }
        
        if choice == '12':
            print(f"\n🏆 Your final score: {score} points!")
            print("Goodbye! Keep learning Python!\n")
            break
        elif choice in handlers:
            score = handlers[choice](score)
        else:
            print("❌ Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    main()