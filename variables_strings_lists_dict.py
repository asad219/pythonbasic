# Variables
# Variables are names that store values. The = sign assigns a value to a name.
# Python figures out the type of each value; you do not declare it first.

# A string is text surrounded by quotes.
name = "Asad"

# An integer is a whole number (no decimal point).
age = 25

# A Boolean is either True or False. These words do not need quotes.
is_student = True

# A list holds multiple values in order, inside square brackets.
hobbies = ["reading", "coding", "hiking"]

# A dictionary stores labeled values as key: value pairs, inside curly braces.
address = {"city": "New York", "country": "USA"}

# print() displays values in the terminal. The labels make the output easier to read.
print("Name:", name)
print("Age:", age)
print("Is student:", is_student)
print("Hobbies:", hobbies)
print("Address:", address)

# Strings
# An f-string starts with f and inserts values where you write {variable}.
greeting = "Hello"
print(f"{greeting}, {name}!")
print(f"I am {age} years old.")
# join() combines the hobby strings, placing a comma and space between them.
print(f"My hobbies are: {', '.join(hobbies)}")
# Use a dictionary key in square brackets to get its value.
print(f"I live in {address['city']}, {address['country']}.")


# Lists
# Lists keep their order and can be changed after they are created.
topics = ["Python", "Machine Learning", "Data Science"]
print("Topics:", topics)

# List positions start at 0; -1 means the last item.
print("First topic:", topics[0])
print("Last topic:", topics[-1])

# append() adds one item at the end of the existing list.
topics.append("Artificial Intelligence")
print("Appended topics:", topics)

# Assigning to position 0 replaces the first item.
topics[0] = "Deep Learning"
print("Modified topics:", topics)

# remove() finds and removes an item by its value.
topics.remove("Data Science")
print("After removal:", topics)

# del removes an item by its position; positions shift after a deletion.
del topics[0]
print("After deletion:", topics)

# Dictionaries
# Dictionaries use keys (labels) to find values, not numbered positions.
person = {"name": "Asad", "age": 45, "is_student": False}
print("Person:", person)

# Use a key in square brackets to read its value.
print("Name:", person["name"])
print("Age:", person["age"])
print("Is student:", person["is_student"])

# Assigning to an existing key replaces its old value.
person["age"] = 46
print("Modified person:", person)

# Assigning to a new key adds it. A dictionary value can also be a list.
person["hobbies"] = ["reading", "coding", "hiking"]
print("After adding hobbies:", person)

# del removes the key and its value together.
del person["is_student"]
print("After removing is_student:", person)

# in checks for a key and returns True or False; it does not change the dictionary.
print("Does 'name' exist in person?", "name" in person)
print("Does 'is_student' exist in person?", "is_student" in person)
print("Does 'hobbies' exist in person?", "hobbies" in person)
print("Does 'address' exist in person?", "address" in person)

# Sets
# Sets hold unique items. The second "apple" is ignored as a duplicate.
# Sets do not have numbered positions; their printed order may vary.
fruits = {"apple", "banana", "cherry", "apple"}
print("Fruits:", fruits)

# add() puts an item in the set if it is not there already.
fruits.add("orange")
print("After adding orange:", fruits)

# remove() deletes an item by value. It raises an error if the item is absent.
fruits.remove("banana")
print("After removing banana:", fruits)

# in checks for an item and returns True or False.
print("Is apple in fruits?", "apple" in fruits)
print("Is banana in fruits?", "banana" in fruits)