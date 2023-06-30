# Write a program to print the following number pattern using a loop.
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Write a program to display only those numbers from a list that satisfy the following conditions
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  # Stop the loop if the number is greater than 500
    if num % 5 == 0 and num <= 150:
        print(num)

# Problem 3: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
mid=len(s1)
s3 = s1[:mid] + s2 + s1[mid:]
print(s3)

# Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lower=""
upper=""
for chr in str1:
  if(chr.isupper()):
    upper+=chr
  else:
    lower+=chr

print(lower+upper)

# Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i in range(len(list1)):
  list1[i]+=list2[i]

print(list1)
