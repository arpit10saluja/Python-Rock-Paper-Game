                # # Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
# data = [("John", 25), ("Jane", 30)]

# for name, age in data:
#     print(f"{name} is {age} years old.")




                # #  **Dictionary Manipulation**
# def add(dictionary, name, age):
#     dictionary[name] = age

# def update(dictionary, name, age):
#     if name in dictionary:
#         dictionary[name] = age

# def delete(dictionary, name):
#     if name in dictionary:
#         del dictionary[name]

# my_dict={}

# add(my_dict, "Jone", 22)
# print(my_dict)
# update(my_dict, "Jone", 55)
# print(my_dict)
# delete(my_dict, "Jone")
# print(my_dict)




            # # Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
# def two_sum(nums, target):
#     complements = {}  # Dictionary to store complements of numbers

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in complements:
#             return [complements[complement], i]

#         complements[num] = i

#     return None  # Return None if no solution is found


# # Input
# nums = [2, 7, 11, 15]
# target = 9

# # Find two integers that sum to the target
# result = two_sum(nums, target)

# print(result) 






                    # Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.
# str="madaim"
# res=str[::-1]   #reserse the string
# if(res==str):
#     print(f"The word {str} is a palindrome")
# else:
#     print(f"The word {str} is not a palindrome")



                    # Selection Sort: Implement the selection sort algorithm in Python.

# arr = [64, 25, 12, 22, 11]
# arr.sort()
# print(arr)


                    # # Implement Stack using Queue: Use Python's queue data structure to implement a stack.
# stk=[]

# stk.append(2)
# stk.append(3)
# stk.insert(0, 1)
# print(stk)
# stk.pop()
# stk.remove(1)
# print(stk)


                    # FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, 
                    # print "Buzz", and for multiples of both three and five, print "FizzBuzz".
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)



                    # File I/O: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
# def count_words(input_file, output_file):
#     with open(input_file, 'r') as file:
#         content = file.read()
#         word_count = len(content.split())

#     with open(output_file, 'w') as file:
#         file.write(f"Number of words: {word_count}")


# # Input file name
# input_file = "input.txt"

# # Output file name
# output_file = "output.txt"

# # Call the function to count words and write to the output file
# count_words(input_file, output_file)


            # Exception Handling: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).

# def divion(num, div):
#     if(div==0):
#         return "Cannot divide by Zero"
#     else:
#         return num/div
    
# print(divion(5,0))
# print(divion(15,3))
