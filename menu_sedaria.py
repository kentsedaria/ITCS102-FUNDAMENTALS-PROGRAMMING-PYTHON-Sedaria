# Python Fundamentals Interactive Menu

def print_statements():
    print("\n--- Print Statements ---")
    print("In Python, the print() function is used to display output.")
    print("Example:")
    print("print('Hello, World!') -> Hello, World!")
    print("Try it yourself below!")
    user_input = input("Enter something to print: ")
    print("Output:", user_input)


def variables():
    print("\n--- Variables ---")
    print("Variables are used to store data values.")
    print("Example:")
    print("x = 10")
    print("y = 'Python'")
    print("print(x, y) -> 10 Python")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old!")


def operators():
    print("\n--- Operators ---")
    print("Operators are used to perform operations on variables and values.")
    print("Examples:")
    print("Arithmetic: +, -, *, /, %")
    print("Comparison: ==, !=, >, <, >=, <=")
    print("Logical: and, or, not")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"{a} + {b} = {a+b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} > {b} ? {a > b}")


def conditionals():
    print("\n--- Conditionals ---")
    print("Conditionals allow you to execute code based on conditions.")
    print("Example:")
    print("if x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')")
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")


def loops():
    print("\n--- Loops ---")
    print("Loops allow you to repeat code multiple times.")
    print("Examples:")
    print("for i in range(5):\n    print(i)")
    print("while condition:\n    do something")
    n = int(input("Enter a number to loop up to: "))
    print("Using for loop:")
    for i in range(1, n+1):
        print(i, end=" ")
    print("\nUsing while loop:")
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1
    print()


def lists():
    print("\n--- Lists ---")
    print("Lists are used to store multiple items in a single variable.")
    print("Example:")
    print("fruits = ['apple', 'banana', 'cherry']")
    print("print(fruits[0]) -> apple")
    fruits = []
    count = int(input("How many fruits do you want to add? "))
    for _ in range(count):
        fruit = input("Enter a fruit: ")
        fruits.append(fruit)
    print("Your fruit list:", fruits)
    print("First fruit:", fruits[0] if fruits else "No fruits added")


def functions():
    print("\n--- Functions ---")
    print("Functions are blocks of code that run when called.")
    print("Example:")
    print("def greet(name):\n    return 'Hello ' + name")
    def greet(name):
        return "Hello " + name
    name = input("Enter your name: ")
    print(greet(name))


def menu():
    while True:
        print("\n=== Python Fundamentals Interactive Menu ===")
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        print("0. Exit")

        choice = input("Select a topic (0-7): ")

        if choice == "1":
            print_statements()
        elif choice == "2":
            variables()
        elif choice == "3":
            operators()
        elif choice == "4":
            conditionals()
        elif choice == "5":
            loops()
        elif choice == "6":
            lists()
        elif choice == "7":
            functions()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    menu()
