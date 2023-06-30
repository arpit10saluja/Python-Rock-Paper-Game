
# Hello, World!: Write a Python program that prints "Hello, World!" to the console.
print("Hello, World!")

# Data Type Play: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
integer_var = 10
float_var = 3.14
string_var = "Hello"
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dictionary_var = {"name": "John", "age": 25}
set_var = {7, 8, 9}

variables = [integer_var, float_var, string_var, boolean_var, list_var, tuple_var, dictionary_var, set_var]

for var in variables:
    print(f"Type of {var}: {type(var)}, value: {var}")

# List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
numbers = list(range(1, 11))
print(numbers)

numbers.append(20)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.sort()
print(numbers)

# Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
def calculate_sum_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return total_sum, average

numbers = [10, 20, 30, 40]
sum_result, average_result = calculate_sum_average(numbers)
print(f"Sum: {sum_result}, Average: {average_result}")


# String Reversal: Write a Python function that takes a string and returns the string in reverse order
def reverse_string(input_str):
    return input_str[::-1]

string = "Python"
reversed_string = reverse_string(string)
print(reversed_string)


# Count Vowels: Write a Python program that counts the number of vowels in a given string.
def count_vowels(input_str):
    vowels = "aeiou"
    count = 0
    for char in input_str.lower():
        if char in vowels:
            count += 1
    return count

string = "Hello"
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")


# Prime Number: Write a Python function that checks whether a given number is a prime number.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = 13
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# Factorial Calculation: Write a Python function that calculates the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}.")

# Fibonacci Sequence: Write a Python function that generates the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence[:n]

number = 5
fibonacci_sequence = fibonacci(number)
print(fibonacci_sequence)


# List Comprehension: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
squared_numbers = [num ** 2 for num in range(1, 11)]
print(squared_numbers)
