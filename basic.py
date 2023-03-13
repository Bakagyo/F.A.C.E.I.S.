# List comprehension: use loops to create lists in succint code

# example: using a typical for loop
x = [1, 2, 3, 4, 5]
y = []
for item in x:
    if item > 2:
        y.append(item)
print(f"y (for loop) = {y}")

# using list comprehension
y = [item for item in x if item > 2]
print(f"y (l. comprehension) = {y}")