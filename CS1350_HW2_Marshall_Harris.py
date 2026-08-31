# CS1350_HW2_Marshall_Harris.py
# CS1350 Homework 2
# Dictionary Fundamentals and Dictionary Keys & Methods
#
# Based on:
# Week 1 Lecture 1: Units 1.1, 1.2, 1.3
# Week 1 Lecture 2: Units 2.1, 2.2, 2.3

print("=" * 60)
print("CS1350 Homework 2 - Dictionary Practice Exercises")
print("=" * 60)


# ============================================================
# UNIT 1.1 - WHAT ARE DICTIONARIES?
# ============================================================

print("\nUNIT 1.1 - WHAT ARE DICTIONARIES?")

# Beginner (5 points)
# Create a dictionary called my_info with name, age, and major.
my_info = {
    "name": "Marshall",
    "age": 19,
    "major": "Computer Science"
}
print("\n1.1 Beginner - My Information:")
print(my_info)


# Intermediate (10 points)
# 1. Create a menu with at least 4 food items and prices.
menu = {
    "burger": 8.99,
    "fries": 3.49,
    "pizza": 10.99,
    "soda": 1.99
}

# 2. Create a dictionary mapping course names to credit hours.
course_credits = {
    "CS1350": 3,
    "MATH": 3,
    "ENGLISH": 3,
    "SCIENCE": 4
}

print("\n1.1 Intermediate - Menu:")
print(menu)
print("1.1 Intermediate - Course Credits:")
print(course_credits)


# Advanced (15 points)
# Create weekly_temps using dict(), not curly braces.
weekly_temps = dict(
    Monday=72,
    Tuesday=75,
    Wednesday=68,
    Thursday=70,
    Friday=73,
    Saturday=78,
    Sunday=76
)
print("\n1.1 Advanced - Weekly Temperatures:")
print(weekly_temps)


# ============================================================
# UNIT 1.2 - ACCESSING DICTIONARY ELEMENTS
# ============================================================

print("\n" + "=" * 60)
print("UNIT 1.2 - ACCESSING DICTIONARY ELEMENTS")

pet = {
    "name": "Buddy",
    "type": "dog",
    "age": 3
}

# Beginner (5 points)
print("\n1.2 Beginner:")
print("Pet name:", pet["name"])
print("Pet age:", pet["age"])


# Intermediate (10 points)
# 1. Safely access the missing color key with get().
color = pet.get("color", "unknown")
print("\n1.2 Intermediate - Pet color:", color)

# 2. Check if a student passed a course using get().
grades = {
    "CS1350": 85,
    "MATH": 68,
    "ENGLISH": 92
}

course = "CS1350"
grade = grades.get(course, None)

if grade is not None:
    if grade >= 70:
        print(f"{course}: Passed with a grade of {grade}.")
    else:
        print(f"{course}: Did not pass with a grade of {grade}.")
else:
    print(f"{course}: Grade not found.")


# Advanced (15 points)
# Take a product dictionary and product name. Print the price if
# found, or "Product not available" if not found.
products = {
    "laptop": 999.99,
    "mouse": 29.99,
    "keyboard": 79.99
}

def find_product_price(product_name):
    price = products.get(product_name)
    if price is not None:
        print(f"{product_name}: ${price:.2f}")
    else:
        print("Product not available")

print("\n1.2 Advanced:")
find_product_price("laptop")
find_product_price("headphones")


# ============================================================
# UNIT 1.3 - MODIFYING DICTIONARIES
# ============================================================

print("\n" + "=" * 60)
print("UNIT 1.3 - MODIFYING DICTIONARIES")

# Beginner (5 points)
# Start with an empty dictionary and add three items.
inventory = {}
inventory["apples"] = 10
inventory["bananas"] = 6
inventory["oranges"] = 8

print("\n1.3 Beginner - Inventory:")
print(inventory)


# Intermediate (10 points)
scores = {
    "Team A": 45,
    "Team B": 38
}

# Update Team B and add Team C.
scores["Team B"] = 52
scores["Team C"] = 41

# Remove Team A with pop() and print its old score.
team_a_score = scores.pop("Team A")

print("\n1.3 Intermediate:")
print("Team A's removed score:", team_a_score)
print("Updated scores:", scores)


# Advanced (15 points)
# Simple shopping cart system.
cart = {}

# Add 3 items with prices.
cart["shirt"] = 24.99
cart["shoes"] = 59.99
cart["hat"] = 19.99

# Update one item's price.
cart["shirt"] = 29.99

# Remove one item and print what was removed.
removed_item_price = cart.pop("hat")
print("\n1.3 Advanced - Removed hat:", f"${removed_item_price:.2f}")

# Print final cart.
print("Final cart:", cart)

# Bonus: calculate total price of remaining items.
total_price = sum(cart.values())
print(f"Total price of remaining items: ${total_price:.2f}")


# ============================================================
# UNIT 2.1 - HOW DICTIONARIES WORK
# ============================================================

print("\n" + "=" * 60)
print("UNIT 2.1 - HOW DICTIONARIES WORK")

# Beginner (5 points)
# Identify valid and invalid dictionary keys.
key_examples = {
    '"student_name"': "valid",
    "[1, 2, 3]": "invalid",
    "100": "valid",
    '("x", "y")': "valid",
    '{"a": 1}': "invalid",
    "frozenset({1,2})": "valid"
}

print("\n2.1 Beginner - Dictionary Keys:")
for key, result in key_examples.items():
    reason = (
        "immutable and hashable"
        if result == "valid"
        else "mutable and unhashable"
    )
    print(f"{key}: {result} ({reason})")


# Intermediate (10 points)
# 1. Fix the original code by using tuples as keys.
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}

# 2. Duplicate keys: the last value wins.
data = {
    "a": 1,
    "b": 2,
    "a": 3,
    "b": 4
}

# 3. Investigate hash values.
print("\n2.1 Intermediate:")
print("Locations:", locations)
print("Duplicate-key dictionary:", data)
print("Length:", len(data))
print("Hash of Marshall:", hash("Marshall"))
print("Hash of 100:", hash(100))


# Advanced (15 points)
# 1. Game high scores using tuples as keys.
high_scores = {
    ("Alice", "Chess"): 950,
    ("Bob", "Tetris"): 1250,
    ("Carol", "Pac-Man"): 2100
}

print("\n2.1 Advanced - High Scores:")
print(high_scores)
print("Bob's Tetris score:", high_scores[("Bob", "Tetris")])

# 2. Compare membership checking in a list and dictionary.
import time

big_list = list(range(100000))
big_dict = {i: i for i in range(100000)}
search_value = 99999

start = time.perf_counter()
search_value in big_list
list_time = time.perf_counter() - start

start = time.perf_counter()
search_value in big_dict
dict_time = time.perf_counter() - start

print(f"List search time: {list_time:.8f} seconds")
print(f"Dictionary search time: {dict_time:.8f} seconds")

if dict_time > 0:
    print(f"Dictionary was approximately {list_time / dict_time:.2f}x faster.")
else:
    print("Dictionary search was too fast to calculate a ratio.")


# ============================================================
# UNIT 2.2 - keys() AND values()
# ============================================================

print("\n" + "=" * 60)
print("UNIT 2.2 - keys() AND values()")

temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}

# Beginner (5 points)
print("\n2.2 Beginner - Day names:")
print(list(temps.keys()))

print("2.2 Beginner - Temperatures:")
print(list(temps.values()))

print("2.2 Beginner - Number of days:", len(temps))


# Intermediate (10 points)
# 1. Highest and lowest temperatures.
highest_temp = max(temps.values())
lowest_temp = min(temps.values())

print("\n2.2 Intermediate:")
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)

# 2. Check if Friday exists.
if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")

# 3. Add Thursday only if it does not already exist.
temps.setdefault("Thursday", 70)
print("After setdefault:", temps)

# 4. Demonstrate dynamic keys view.
keys_view = temps.keys()
print("Keys before adding Friday:", keys_view)

temps["Friday"] = 73
print("Keys after adding Friday:", keys_view)


# Advanced (15 points)
prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

# 1. Total value and average price.
total_value = sum(prices.values())
average_price = total_value / len(prices)

# 2. Most and least expensive items.
most_expensive = max(prices.items(), key=lambda item: item[1])
least_expensive = min(prices.items(), key=lambda item: item[1])

# 3. Compare memory usage of keys() and list(keys()).
import sys

keys_view = prices.keys()
keys_list = list(prices.keys())

print("\n2.2 Advanced:")
print(f"Total value: ${total_value}")
print(f"Average price: ${average_price:.2f}")
print(
    f"Most expensive: {most_expensive[0]} (${most_expensive[1]})"
)
print(
    f"Least expensive: {least_expensive[0]} (${least_expensive[1]})"
)
print("Memory used by keys() view:", sys.getsizeof(keys_view), "bytes")
print("Memory used by list(keys()):", sys.getsizeof(keys_list), "bytes")

# 4. Add 3 new products with update().
prices.update({
    "monitor": 249,
    "keyboard": 79,
    "mouse": 29
})

print("Products after update():")
print(list(prices.keys()))


# ============================================================
# UNIT 2.3 - items() METHOD
# ============================================================

print("\n" + "=" * 60)
print("UNIT 2.3 - items() METHOD")

colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Beginner (5 points)
print("\n2.3 Beginner - Fruit colors:")
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")

print("list(colors.items()) would return:")
print(list(colors.items()))


# Intermediate (10 points)
prices_with_tax = {
    "coffee": 4.50,
    "tea": 3.00,
    "juice": 5.25
}

print("\n2.3 Intermediate - Prices with 10% tax:")
for item, price in prices_with_tax.items():
    tax = price * 0.10
    total = price + tax
    print(f"{item}: ${price:.2f} + tax = ${total:.2f}")

# Count items costing more than $4.00.
count_over_four = 0
for item, price in prices_with_tax.items():
    if price > 4.00:
        count_over_four += 1

print("Items costing more than $4.00:", count_over_four)

# Tuple unpacking to swap x and y.
x = 10
y = 20
x, y = y, x
print("After swapping: x =", x, "y =", y)

# Extended unpacking.
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)


# Advanced (15 points)
scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

# 1. Find highest score using items() and max() with lambda.
best_name, best_score = max(
    scores.items(),
    key=lambda item: item[1]
)

# 2. Create passed and failed dictionaries.
passed = {}
failed = {}

for name, score in scores.items():
    if score >= 70:
        passed[name] = score
    else:
        failed[name] = score

# 3. Calculate class average and each student's deviation.
class_average = sum(scores.values()) / len(scores)

deviations = {}
for name, score in scores.items():
    deviations[name] = score - class_average

print("\n2.3 Advanced:")
print(f"Highest score: {best_name} with {best_score}")
print("Passed:", passed)
print("Failed:", failed)
print(f"Class average: {class_average:.2f}")
print("Deviation from average:")
for name, deviation in deviations.items():
    print(f"  {name}: {deviation:+.2f}")

# 4. Performance test: items() vs keys() + lookup for 50,000 entries.
performance_dict = {
    i: i * 2 for i in range(50000)
}

start = time.perf_counter()
for key, value in performance_dict.items():
    _ = key + value
items_time = time.perf_counter() - start

start = time.perf_counter()
for key in performance_dict.keys():
    value = performance_dict[key]
    _ = key + value
keys_lookup_time = time.perf_counter() - start

print(f"items() iteration: {items_time:.6f} seconds")
print(f"keys() + lookup: {keys_lookup_time:.6f} seconds")

if items_time > 0:
    print(
        f"keys() + lookup / items() ratio: "
        f"{keys_lookup_time / items_time:.2f}x"
    )


print("\n" + "=" * 60)
print("Homework 2 practice exercises complete.")
print("=" * 60)
