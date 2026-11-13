def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    Example: power(2, 5) = 32
    Example: power(3, 0) = 1
    """
    # TODO:
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 5))
print(power(3, 0))
print(power(5, 3))




def generate_binary_strings(n):

    results = []

    def build_string(current):

        if len(current) == n:
            results.append(current)
            return

        build_string(current + '0')
        build_string(current + '1')

    build_string("")

    return results


print(generate_binary_strings(2))
print(generate_binary_strings(1))




def subset_sum(nums, target):

    def check(index, remaining):

        if remaining == 0:
            return True

        if index == len(nums):
            return False

        # Include the current number
        include = check(index + 1, remaining - nums[index])

        # Skip the current number
        exclude = check(index + 1, remaining)

        return include or exclude

    return check(0, target)


print(subset_sum([3, 34, 4, 12, 5, 2], 9))
print(subset_sum([1, 2, 3, 4], 10))
print(subset_sum([1, 2, 3], 7))



def is_palindrome(s):

    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))