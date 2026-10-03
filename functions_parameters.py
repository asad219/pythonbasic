# Function with parameters
# The function greet takes one parameter, name, and prints a greeting message.
def greet(name):
    print(f"Hello, {name}!")

greet("Asad")

# Function with multiple parameters
def greet_full_name(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full_name("Asad", "Khan")

# Function with default parameter
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Asad")

# Function with variable-length arguments
def greet_multiple(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_multiple("Asad", "Ali", "Sara")

# Function with keyword arguments
def greet_with_keywords(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_with_keywords(first_name="Asad", last_name="Khan", age=25)

# Function with both positional and keyword arguments
def greet_positional_and_keywords(greeting, *names, **kwargs):
    for name in names:
        print(f"{greeting}, {name}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_positional_and_keywords("Hello", "Asad", "Ali", first_name="Asad", last_name="Khan", age=25, location="UAE")

# Function with type hints and return type
def add_numbers(first: int, second: int) -> int:
    return first + second

print(add_numbers(5, 5))
print(add_numbers(first=3, second=5))

# Function with type hints and default parameter
def multiply_numbers(first: int, second: int = 2) -> int:
    return first * second

print(multiply_numbers(5))
print(multiply_numbers(5, 3))

# Lambda function with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12
print(multiply(5, 6))  # 30

# Lambda function with a single argument
double = lambda number: number * 2
print(double(5))  # 10
print(double(8))  # 16