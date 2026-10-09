# for loop
# A for loop iterates over a sequence (like a list) and executes a block of code for each item.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop
# A while loop repeats as long as a condition is True.
count = 0
while count < 5:
    print(count)
    count += 1

# break statement
# The break statement exits the nearest enclosing loop immediately.
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# continue statement
# The continue statement skips the rest of the current loop iteration and moves to the next iteration.
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# # else clause with for loop
# # The else clause executes after the for loop completes normally (without a break).
for fruit in fruits:
    print(fruit)
else:
    print("Finished iterating over fruits.")


# else clause with while loop
# The else clause executes after the while loop completes normally (without a break).
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Finished counting.")


# Nested loops
# A nested loop is a loop inside another loop.
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

    