def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)
    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero.")
    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    
    
# TODO 2: Fix list index error
def safe_get_item(lst, index):
    """Get item at index or return 'Not found'"""
    # Add appropriate exception handling
    try:
        return lst[index]
    except IndexError:
        return "Not found"


my_list = [1, 2, 3]
print(f"Item at index 1: {safe_get_item(my_list, 1)}")
print(f"Item at index 10: {safe_get_item(my_list, 10)}")

# TODO 3: Handle multiple exceptions
def convert_to_number(value):
    """Convert string to int or float, return None if impossible"""
    # Try int first, then float, handle ValueError
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return None
# Test conversions
test_values = ["42", "3.14", "hello", None]
for val in test_values:
    result = convert_to_number(val)