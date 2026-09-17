# Unit 3.1 Beginner

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

# 1. Print each product name
for product in inventory:
    print(product)

# 2. Calculate total items
total = sum(inventory.values())
print("Total items:", total)

# 3. Print each product with quantity
for product, quantity in inventory.items():
    print(product, ":", quantity)
    
    
# Unit 3.1 Intermediate

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

# 1. Print products sorted alphabetically
print("Products alphabetically:")

for product in sorted(prices):
    print(product, ":", prices[product])


# 2. Print products sorted by price, cheapest first
print("\nProducts by price:")

for product in sorted(prices, key=prices.get):
    print(product, ":", prices[product])


# 3. Find and print the most expensive item
most_expensive = max(prices.items(), key=lambda item: item[1])

print("\nMost expensive:")
print(most_expensive[0], ":", most_expensive[1])


# Unit 3.1 Advanced

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75,
    "Thu": 80,
    "Fri": 65
}

# 1. Calculate average temperature
average = sum(temps.values()) / len(temps)

print("Average temperature:", average)


# 2. Find hottest and coldest days in a single loop

hottest_day = None
hottest_temp = float("-inf")

coldest_day = None
coldest_temp = float("inf")

for day, temperature in temps.items():

    if temperature > hottest_temp:
        hottest_temp = temperature
        hottest_day = day

    if temperature < coldest_temp:
        coldest_temp = temperature
        coldest_day = day


print("Hottest day:", hottest_day, hottest_temp)
print("Coldest day:", coldest_day, coldest_temp)


# 3. Count days above average

above_average = 0

for temperature in temps.values():
    if temperature > average:
        above_average += 1

print("Days above average:", above_average)


# Unit 3.2 Beginner

products = {
    "laptop": {
        "price": 999,
        "stock": 15
    },
    "phone": {
        "price": 699,
        "stock": 50
    }
}

# 1. Print laptop's price
print("Laptop price:", products["laptop"]["price"])


# 2. Print each product with its stock level

for product, info in products.items():
    print(product, "stock:", info["stock"])
    
    
# Unit 3.2 Intermediate

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

# 1. Create dictionary using zip()
country_capitals = dict(zip(countries, capitals))

print("Country Capitals:")
print(country_capitals)


# 2. Add tablet product

products = {
    "laptop": {
        "price": 999,
        "stock": 15
    },
    "phone": {
        "price": 699,
        "stock": 50
    }
}

products["tablet"] = {
    "price": 449,
    "stock": 30
}

print("\nProducts:")
print(products)


# 3. Safely remove products with stock < 20

for product, info in list(products.items()):

    if info["stock"] < 20:
        del products[product]

print("\nProducts after removing low stock:")
print(products)

# Unit 3.2 Advanced

company = {
    "Engineering": {
        "Alice": 95000,
        "Bob": 85000
    },
    "Marketing": {
        "Carol": 75000,
        "Dave": 70000
    }
}


# 1. Print all employees with salaries

for department, employees in company.items():

    print("\n" + department)

    for employee, salary in employees.items():
        print(employee, ":", salary)


# 2. Calculate average salary per department

print("\nAverage salaries:")

for department, employees in company.items():

    average_salary = sum(employees.values()) / len(employees)

    print(department, ":", average_salary)


# 3. Find highest-paid employee

highest_employee = None
highest_salary = 0

for department, employees in company.items():

    for employee, salary in employees.items():

        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee

print("\nHighest-paid employee:")
print(highest_employee, ":", highest_salary)

# Unit 3.3 Beginner

# 1. Map numbers 1-5 to their cubes

cubes = {
    x: x ** 3
    for x in range(1, 6)
}

print("Cubes:", cubes)


# 2. Convert Fahrenheit temperatures to Celsius

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75
}

celsius = {
    day: (temperature - 32) * 5 / 9
    for day, temperature in temps.items()
}

print("Celsius:", celsius)

# Unit 3.3 Intermediate

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}


# 1. Create passing dictionary

passing = {
    name: score
    for name, score in scores.items()
    if score >= 70
}

print("Passing:", passing)


# 2. Create letter grades

def to_letter(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


letter_grades = {
    name: to_letter(score)
    for name, score in scores.items()
}

print("Letter grades:", letter_grades)


# 3. Invert student IDs

student_ids = {
    "Alice": 101,
    "Bob": 102
}

inverted = {
    student_id: name
    for name, student_id in student_ids.items()
}

print("Inverted:", inverted)

# Unit 3.3 Advanced

sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]


# 1. Total sales by region

region_totals = {}

for region, person, amount in sales:

    region_totals[region] = region_totals.get(region, 0) + amount

print("Sales by region:")
print(region_totals)


# 2. Total sales by salesperson

person_totals = {}

for region, person, amount in sales:

    person_totals[person] = person_totals.get(person, 0) + amount

print("\nSales by salesperson:")
print(person_totals)


# 3. Nested dictionary: {region: {person: total}}

nested_sales = {}

for region, person, amount in sales:

    if region not in nested_sales:
        nested_sales[region] = {}

    nested_sales[region][person] = (
        nested_sales[region].get(person, 0) + amount
    )

print("\nNested sales:")
print(nested_sales)

# Unit 1 Beginner

# 1. Create a vowels set

vowels = {"a", "e", "i", "o", "u"}

print("Vowels:", vowels)


# 2. Create set from list

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

number_set = set(numbers)

print("Set:", number_set)
print("Number of elements:", len(number_set))


# 3. What's wrong with empty = {}?

empty = {}

print(type(empty))

# {} creates an empty dictionary.
# Use set() to create an empty set.

empty_set = set()

print(type(empty_set))

# Unit 1 Intermediate

# 1. Unique characters in "mississippi"

text = "mississippi"

unique_letters = set(text)

print("Unique letters:", unique_letters)
print("Number of unique letters:", len(unique_letters))


# 2. Remove duplicates from email list

emails = [
    "a@b.com",
    "c@d.com",
    "a@b.com",
    "e@f.com",
    "c@d.com"
]

unique_emails = list(set(emails))

print("Unique emails:", unique_emails)


# 3. Why does this fail?

# s = {[1, 2], [3, 4]}

# It fails because lists cannot be elements of a set.
# Lists are not hashable.

# Unit 1 Advanced

import time


# 1. Compare set vs list membership

big_set = set(range(1000000))
big_list = list(range(1000000))

start = time.perf_counter()
999999 in big_set
set_time = time.perf_counter() - start


start = time.perf_counter()
999999 in big_list
list_time = time.perf_counter() - start


print("Set lookup time:", set_time)
print("List lookup time:", list_time)


# 2. Create frozenset and use it as dictionary key

my_frozenset = frozenset(["Python", "SQL"])

my_dictionary = {
    my_frozenset: "Programming Skills"
}

print("\nDictionary:")
print(my_dictionary)


# 3. Find unique nodes in graph edges

edges = [
    (1, 2),
    (2, 3),
    (1, 3),
    (3, 4)
]

nodes = set()

for edge in edges:

    nodes.add(edge[0])
    nodes.add(edge[1])

print("\nUnique nodes:", nodes)

# Unit 2 Beginner

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# 1. Union
all_numbers = a | b
print("Union:", all_numbers)


# 2. Intersection
both = a & b
print("Intersection:", both)


# 3. Difference
a_only = a - b
print("Only in a:", a_only)

# Unit 2 Intermediate

morning_shift = {
    "Alice",
    "Bob",
    "Carol"
}

evening_shift = {
    "Carol",
    "Dave",
    "Eve"
}

weekend_shift = {
    "Alice",
    "Eve",
    "Frank"
}


# 1. Employees who work ALL shifts

all_shifts = (
    morning_shift
    & evening_shift
    & weekend_shift
)

print("All shifts:", all_shifts)


# 2. Employees who work at least one shift

any_shift = (
    morning_shift
    | evening_shift
    | weekend_shift
)

print("At least one shift:", any_shift)


# 3. Employees who ONLY work morning

morning_only = (
    morning_shift
    - evening_shift
    - weekend_shift
)

print("Morning only:", morning_only)


# 4. Employees who work exactly one shift

exactly_one = (
    morning_shift
    ^ evening_shift
    ^ weekend_shift
)

print("Exactly one shift:", exactly_one)

# Unit 2 Intermediate

morning_shift = {
    "Alice",
    "Bob",
    "Carol"
}

evening_shift = {
    "Carol",
    "Dave",
    "Eve"
}

weekend_shift = {
    "Alice",
    "Eve",
    "Frank"
}


# 1. Employees who work ALL shifts

all_shifts = (
    morning_shift
    & evening_shift
    & weekend_shift
)

print("All shifts:", all_shifts)


# 2. Employees who work at least one shift

any_shift = (
    morning_shift
    | evening_shift
    | weekend_shift
)

print("At least one shift:", any_shift)


# 3. Employees who ONLY work morning

morning_only = (
    morning_shift
    - evening_shift
    - weekend_shift
)

print("Morning only:", morning_only)


# 4. Employees who work exactly one shift

exactly_one = (
    morning_shift
    ^ evening_shift
    ^ weekend_shift
)

print("Exactly one shift:", exactly_one)

# Unit 3 Beginner

# 1. Create set, add 4, remove 1

numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(1)

print("Numbers:", numbers)


# 2. Set comprehension for even numbers 0-20

evens = {
    number
    for number in range(21)
    if number % 2 == 0
}

print("Even numbers:", evens)


# 3. discard() vs remove()

numbers = {1, 2, 3}

# discard() does NOT cause an error
numbers.discard(10)

print("After discard:", numbers)


# remove() WOULD cause a KeyError if 10 isn't present
# numbers.remove(10)

# Unit 3 Intermediate

# 1. Remove duplicates while preserving order

numbers = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

seen = set()
unique = []

for number in numbers:

    if number not in seen:
        seen.add(number)
        unique.append(number)

print("Unique numbers:", unique)


# 2. Unique words from sentence

sentence = "To be or not to be that is the question"

words = {
    word.lower()
    for word in sentence.split()
}

print("Unique words:", words)


# 3. Find missing numbers

expected = set(range(1, 11))

actual = {
    1, 2, 4, 5, 7, 8, 10
}

missing = expected - actual

print("Missing numbers:", missing)

# Unit 3 Intermediate

# 1. Remove duplicates while preserving order

numbers = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

seen = set()
unique = []

for number in numbers:

    if number not in seen:
        seen.add(number)
        unique.append(number)

print("Unique numbers:", unique)


# 2. Unique words from sentence

sentence = "To be or not to be that is the question"

words = {
    word.lower()
    for word in sentence.split()
}

print("Unique words:", words)


# 3. Find missing numbers

expected = set(range(1, 11))

actual = {
    1, 2, 4, 5, 7, 8, 10
}

missing = expected - actual

print("Missing numbers:", missing)

