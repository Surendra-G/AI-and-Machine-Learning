# -*- coding: utf-8 -*-
"""2357810_SurendraGiri_AI_&_ML_Worksheet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/186lNfnTs7m1Y-TBagbfJy_-foZvio48v

# Exercise on Functions
# Task 1: Unit Conversion Program

1. Prompt the user to choose the type of conversion (e.g., length, weight, volume).
2. Ask the user to input the value to be converted.
3. Perform the conversion and display the result.
4. Handle potential errors, such as invalid input or unsupported conversion types.


• Conversion Options:
1. Length:
– Convert meters (m) to feet (ft).
– Convert feet (ft) to meters (m).
2. Weight:
– Convert kilograms (kg) to pounds (lbs).
– Convert pounds (lbs) to kilograms (kg).
3. Volume:
– Convert liters (L) to gallons (gal).
– Convert gallons (gal) to liters (L).
"""

def convert_length(value, unit):
    """Converts length between meters and feet."""
    if unit == "m":
        return value * 3.28084  # meters to feet
    elif unit == "ft":
        return value / 3.28084  # feet to meters
    else:
        raise ValueError("Unsupported length unit")


def convert_weight(value, unit):
    """Converts weight between kilograms and pounds."""
    if unit == "kg":
        return value * 2.20462  # kg to lbs
    elif unit == "lbs":
        return value / 2.20462  # lbs to kg
    else:
        raise ValueError("Unsupported weight unit")


def convert_volume(value, unit):
    """Converts volume between liters and gallons."""
    if unit == "L":
        return value * 0.264172  # liters to gallons
    elif unit == "gal":
        return value / 0.264172  # gallons to liters
    else:
        raise ValueError("Unsupported volume unit")


def unit_converter():
    """Prompts user for conversion type, value, and unit, then performs the conversion."""
    try:
        conversion_type = input("Choose conversion type (length/weight/volume): ").lower()
        value = float(input("Enter the value to convert: "))
        unit = input("Enter the current unit (m/ft for length, kg/lbs for weight, L/gal for volume): ").strip()

        if conversion_type == "length":
            result = convert_length(value, unit)
        elif conversion_type == "weight":
            result = convert_weight(value, unit)
        elif conversion_type == "volume":
            result = convert_volume(value, unit)
        else:
            raise ValueError("Unsupported conversion type")

        print(f"Converted value: {result:.4f}")

    except ValueError as e:
        print(f"Error: {e}")


# Run the unit converter
unit_converter()

"""# Task2
# Mathematical operations on a list of numbers.


1. Prompt the user to choose an operation (e.g., find the sum, average, maximum, or minimum
of the numbers).
2. Ask the user to input a list of numbers (separated by spaces).
3. Perform the selected operation and display the result.
4. Handle potential errors, such as invalid input or empty lists.
"""

def math_operations():
    """Performs sum, average, max, or min on a list of numbers."""

    def _sum(nums): return sum(nums)
    def _avg(nums): return sum(nums) / len(nums)
    def _max(nums): return max(nums)
    def _min(nums): return min(nums)

    try:
        op = input("Choose operation (sum/avg/max/min): ").lower()
        nums_input = input("Enter numbers (space-separated): ").strip()

        if not nums_input:
            raise ValueError("No numbers provided.")

        nums = list(map(float, nums_input.split()))

        operations = {
            "sum": _sum(nums),
            "avg": _avg(nums),
            "max": _max(nums),
            "min": _min(nums)
        }

        if op not in operations:
            raise KeyError("Invalid operation selected.")

        print(f"Result: {operations[op]:.4f}")

    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")

# Run the function
math_operations()

"""# List Manipulation Solutions

## 1. Extract Every Other Element:

Write a Python function that extracts every other element from a list, starting from the first element.



## 2. Slice a Sublist:
Write a Python function that returns a sublist from a given list, starting from a specified index and
ending at another specified index.



## 3. Reverse a List Using Slicing:
Write a Python function that reverses a list using slicing.



## 4. Remove the First and Last Elements:
Write a Python function that removes the first and last elements of a list and returns the resulting sublist.


## 5. Get the First n Elements:
Write a Python function that extracts the first n elements from a list.


# 6. Extract Elements from the End:
Write a Python function that extracts the last n elements of a list using slicing.


## 7. Extract Elements in Reverse Order:
Write a Python function that extracts a list of elements in reverse order starting from the second-to-last
element and skipping one element in between.
"""

# 1. Extract Every Other Element
def extract_every_other(lst): return lst[::2]
print("Output of task-1")
print(extract_every_other([1, 2, 3, 4, 5, 6]))
print(extract_every_other(["a", "b", "c", "d", "e"]))

# 2. Get Sublist
def get_sublist(lst, start, end): return lst[start:end+1]
print("\nOutput of task-2")
print(get_sublist([10, 20, 30, 40, 50], 1, 3))
print(get_sublist(["apple", "banana", "cherry", "date"], 0, 2))


# 3. Reverse List
def reverse_list(lst): return lst[::-1]
print("\nOutput of task-3")
print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["x", "y", "z"]))


# 4. Remove First/Last
def remove_first_last(lst): return lst[1:-1] if len(lst) > 2 else []
print("\nOutput of task-4")
print(remove_first_last([1, 2, 3, 4]))
print(remove_first_last(["a", "b", "c"]))
print(remove_first_last([10, 20]))


# 5. First N Elements
def get_first_n(lst, n): return lst[:n]
print("\nOutput of task-5")
print(get_first_n([10, 20, 30, 40, 50], 3))
print(get_first_n(["x", "y", "z"], 2))


# 6. Last N Elements
def get_last_n(lst, n): return lst[-n:]
print("\nOutput of task-6")
print(get_last_n([10, 20, 30, 40, 50], 2))
print(get_last_n(["a", "b", "c", "d"], 3))


# 7. Reverse Skip
def reverse_skip(lst): return lst[-2::-2]
print("\nOutput of task-7")
print(reverse_skip([1, 2, 3, 4, 5, 6]))
print(reverse_skip(["a", "b", "c", "d", "e", "f"]))

"""# Nested List Solutions


# 1. Flatten a Nested List:
Write a Python function that takes a nested list and flattens it into a single list, where all the elements
are in a single dimension.

# 2. Accessing Nested List Elements:
Write a Python function that extracts a specific element from a nested list given its indices.


# 3. Sum of All Elements in a Nested List:
Write a Python function that calculates the sum of all the numbers in a nested list (regardless of depth).

# 4. Remove Specific Element from a Nested List:
Write a Python function that removes all occurrences of a specific element from a nested list.

# 5. Find the Maximum Element in a Nested List:
Write a Python function that finds the maximum element in a nested list (regardless of depth).


# 6. Count Occurrences of an Element in a Nested List:
Write a Python function that counts how many times a specific element appears in a nested list

# 7. Flatten a List of Lists of Lists:
Write a Python function that flattens a list of lists of lists into a single list, regardless of the depth.


## 8. Nested List Average:
Write a Python function that calculates the average of all elements in a nested list.
"""

# 1. Flatten Nested List
def flatten(lst):
    return [item for sublist in lst for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])]
print("Output of Task-1:")
print(flatten([1, [2, [3, 4], 5], 6]))
print(flatten([[["a"]], "b", ["c", ["d"]]]))


# 2. Access Nested Element
def access_nested_element(lst, indices):
    for i in indices: lst = lst[i]
    return lst
print("\nOutput of Task-2:")
nested_list = [[1, 2], [3, [4, 5]]]
print(access_nested_element(nested_list, [1, 1, 0]))
print(access_nested_element(nested_list, [0, 1]))


# 3. Sum Nested List
def sum_nested(lst):
    return sum(sum_nested(item) if isinstance(item, list) else item for item in lst)

print("\nOutput of Task-3:")
print(sum_nested([1, [2, [3, 4], 5], 6]))
print(sum_nested([[10, [20, 30]], 40]))


# 4. Remove Element
def remove_element(lst, elem):
    return [remove_element(i, elem) if isinstance(i, list) else i for i in lst if i != elem]

print("\nOutput of Task-4:")
print(remove_element([1, [2, 3, [2, 4], 5], 2], 2))
print(remove_element(["a", ["b", "c", "a"], "a"], "a"))


# 5. Find Max
def find_max(lst):
    return max(find_max(i) if isinstance(i, list) else i for i in lst)

print("\nOutput of Task-5:")
print(find_max([1, [5, [3, 9], 4], 8]))
print(find_max([[-10, [-50, -3]], -1]))


# 6. Count Occurrences
def count_occurrences(lst, elem):
    return sum(count_occurrences(i, elem) if isinstance(i, list) else 1 for i in lst if i == elem)

print("\nOutput of Task-6:")
print(count_occurrences([1, [2, 3, [2, 4], 2], 2], 2))
print(count_occurrences(["a", ["b", "a", ["a", "c"]]], "a"))



# 7. Deep Flatten
def deep_flatten(lst):
    return [item for sublist in lst for item in (deep_flatten(sublist) if isinstance(sublist, list) else [sublist])]

print("\nOutput of Task-7:")
print(deep_flatten([[[1, 2], 3], [4, [5, [6]]]]))
print(deep_flatten([["x", [["y"]], "z"]]))


# 8. Nested Average
def average_nested(lst):
    flat = deep_flatten(lst)
    return sum(flat)/len(flat) if flat else 0

print("\nOutput of Task-8:")
print(average_nested([1, [2, 3], [4, [5, 6]]]))
print(average_nested([[10, 20], [30, [40]]]))
print(average_nested([]))

"""# To - Do - NumPy

# NumPy Solutions

# Basic Vector and Matrix Operation with Numpy.
Problem - 1: Array Creation:
Complete the following Tasks:
1. Initialize an empty array with size 2X2.
2. Initialize an all one array with size 4X2.
3. Return a new array of given shape and type, filled with fill value.{Hint: np.full}
4. Return a new array of zeros with same shape and type as a given array.{Hint: np.zeros like}
5. Return a new array of ones with same shape and type as a given array.{Hint: np.ones like}
6. For an existing list new_list = [1,2,3,4] convert to an numpy array.{Hint: np.array()}
"""

import numpy as np

# 1. Create an empty 2x2 array
empty = np.empty((2,2))
print("Empty 2x2 Array:\n", empty)

# 2. Create a 4x2 array filled with ones
ones = np.ones((4,2))
print("\n4x2 Ones Array:\n", ones)

# 3. Create a 3x3 array filled with the number 5
full = np.full((3,3), 5)
print("\n3x3 Full Array (Filled with 5s):\n", full)

# 4. Create an array of zeros with the same shape as 'full'
zeros_like = np.zeros_like(full)
print("\nZeros Like 'full' (Same Shape as 'full'):\n", zeros_like)

# 5. Create an array of ones with the same shape as 'full'
ones_like = np.ones_like(full)
print("\nOnes Like 'full' (Same Shape as 'full'):\n", ones_like)

# 6. Convert a Python list to a NumPy array
np_array = np.array([1,2,3,4])
print("\nNumPy Array from List:\n", np_array)

"""# Problem - 2: Array Manipulation: Numerical Ranges and Array indexing:
Complete the following tasks:
1. Create an array with values ranging from 10 to 49. {Hint:np.arrange()}.
2. Create a 3X3 matrix with values ranging from 0 to 8.
{Hint:look for np.reshape()}
3. Create a 3X3 identity matrix.{Hint:np.eye()}
4. Create a random array of size 30 and find the mean of the array.
{Hint:check for np.random.random() and array.mean() function}
5. Create a 10X10 array with random values and find the minimum and maximum values.
6. Create a zero array of size 10 and replace 5th element with 1.
7. Reverse an array arr = [1,2,0,0,4,0].
8. Create a 2d array with 1 on border and 0 inside.
9. Create a 8X8 matrix and fill it with a checkerboard pattern.
"""

import numpy as np

# 1. Create an array from 10 to 49
arr_10_49 = np.arange(10, 50)
print("Array from 10 to 49:\n", arr_10_49)

# 2. Create a 3×3 matrix with values from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix:\n", matrix_3x3)

# 3. Create a 3×3 identity matrix
identity = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity)

# 4. Compute the mean of a random array with 30 elements
mean_rand = np.random.random(30).mean()
print("\nMean of random 30-element array:", mean_rand)

# 5. Find the min and max of a 10×10 random matrix
random_matrix = np.random.rand(10, 10)
min_max = (random_matrix.min(), random_matrix.max())
print("\nMin and Max of 10x10 random matrix:", min_max)

# 6. Create a zero array of size 10 and set the fifth value to 1
zero_arr = np.zeros(10)
zero_arr[4] = 1
print("\nZero array with fifth element as 1:\n", zero_arr)

# 7. Reverse an array
reversed_arr = np.array([1, 2, 0, 0, 4, 0])[::-1]
print("\nReversed array:\n", reversed_arr)

# 8. Create a 5×5 array with a 1s border and 0s inside
border = np.ones((5, 5))
border[1:-1, 1:-1] = 0
print("\n5x5 Matrix with a border of 1s and 0s inside:\n", border)

# 9. Create an 8×8 checkerboard pattern
checker = np.zeros((8, 8))
checker[::2, ::2] = 1
checker[1::2, 1::2] = 1
print("\n8x8 Checkerboard Pattern:\n", checker)

"""# Problem - 3: Array Operations:
## For the following arrays:

x = np.array([[1,2],[3,5]])
y = np.array([[5,6],[7,8]]);
v = np.array([9,10])
w = np.array([11,12]);

Complete all the task using numpy:
1. Add the two array.
2. Subtract the two array.
3. Multiply the array with any integers of your choice.
4. Find the square of each element of the array.
5. Find the dot product between: v(and)w ; x(and)v ; x(and)y.
6. Concatenate x(and)y along row and Concatenate v(and)w along column.
{Hint:try np.concatenate() or np.vstack() functions.
7. Concatenate x(and)v; if you get an error, observe and explain why did you get the error?

"""

import numpy as np

# Define matrices and vectors
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

# 1. Element-wise addition
add = x + y
print("Addition of x and y:\n", add)

# 2. Element-wise subtraction
subtract = x - y
print("\nSubtraction of x and y:\n", subtract)

# 3. Element-wise multiplication by 3
multiply = x * 3
print("\nMultiplication of x by 3:\n", multiply)

# 4. Element-wise square
square = x ** 2
print("\nSquare of x:\n", square)

# 5. Dot product of v and w
dot_vw = np.dot(v, w)
print("\nDot Product of v and w:", dot_vw)

# 6. Dot product of matrix x and vector v
dot_xv = np.dot(x, v)
print("\nDot Product of x and v:\n", dot_xv)

# 7. Dot product of matrices x and y
dot_xy = np.dot(x, y)
print("\nDot Product of x and y:\n", dot_xy)

# 8. Concatenation of x and y along rows (vertical stack)
concat_row = np.vstack((x, y))
print("\nConcatenation of x and y along rows:\n", concat_row)

# 9. Concatenation of v and w along columns
concat_col = np.column_stack((v, w))
print("\nConcatenation of v and w along columns:\n", concat_col)

"""# Problem - 4: Matrix Operations:
## • For the following arrays:

A = np.array([[3,4],[7,8]])

B = np.array([[5,3],[2,1]])

## Prove following with Numpy:
1. Prove A.A−1 = I.
2. Prove AB ̸= BA.
3. Prove (AB)
T = BTAT


## • Solve the following system of Linear equation using Inverse Methods.
2x − 3y + z = −1
x − y + 2z = −3
3x + y − z = 9

{Hint: First use Numpy array to represent the equation in Matrix form. Then Solve for: AX = B}

• Now: solve the above equation using np.linalg.inv function.{Explore more about ”linalg” function of Numpy}

"""

import numpy as np

# Define matrices A and B
A = np.array([[3, 4], [7, 8]])
B = np.array([[5, 3], [2, 1]])

# 1. A * A_inv should give the identity matrix (A * A_inv ≈ I)
AA_inv = np.dot(A, np.linalg.inv(A))
print("A * A_inv (Should be Identity Matrix):\n", AA_inv)

# 2. Check if AB is not equal to BA (Matrix multiplication is not commutative)
AB_BA = np.dot(A, B) != np.dot(B, A)
print("\nIs A * B not equal to B * A?:\n", AB_BA)

# 3. Check if (A * B)^T == B^T * A^T (Transpose of product)
AB_T = np.dot(A, B).T == np.dot(B.T, A.T)
print("\nIs (A * B)^T equal to B^T * A^T?:\n", AB_T)

# 4. Solve the linear system of equations Ax = b
coefficients = np.array([[2, -3, 1], [1, -1, 2], [3, 1, -1]])
constants = np.array([-1, -3, 9])

# Solve for x using numpy's linear algebra solver
solution = np.linalg.inv(coefficients).dot(constants)
print("\nSolution to the linear system Ax = b:\n", solution)

"""# Speed Comparison

# 10.2 Experiment: How Fast is Numpy?
In this exercise, you will compare the performance and implementation of operations using plain Python
lists (arrays) and NumPy arrays. Follow the instructions:

## 1. Element-wise Addition:
• Using Python Lists, perform element-wise addition of two lists of size 1, 000, 000. Measure and Print the time taken for this operation.

• Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this operation.



"""

import numpy as np
import time

# 1. Element-wise Addition
size = 1_000_000
list1 = list(range(size))
list2 = list(range(size))

# Using Python Lists
start_time = time.time()
list_sum = [a + b for a, b in zip(list1, list2)]
end_time = time.time()
print(f"Python Lists Addition Time: {end_time - start_time:.6f} seconds")

# Using NumPy Arrays
arr1 = np.array(list1)
arr2 = np.array(list2)
start_time = time.time()
numpy_sum = arr1 + arr2
end_time = time.time()
print(f"NumPy Addition Time: {end_time - start_time:.6f} seconds")

"""
## 2. Element-wise Multiplication
• Using Python Lists, perform element-wise multiplication of two lists of size 1, 000, 000. Measure and Print the time taken for this operation.

• Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this operation."""

# 2. Element-wise Multiplication
# Using Python Lists
start_time = time.time()
list_product = [a * b for a, b in zip(list1, list2)]
end_time = time.time()
print(f"Python Lists Multiplication Time: {end_time - start_time:.6f} seconds")

# Using NumPy Arrays
start_time = time.time()
numpy_product = arr1 * arr2
end_time = time.time()
print(f"NumPy Multiplication Time: {end_time - start_time:.6f} seconds")

"""## 3. Dot Product
• Using Python Lists, compute the dot product of two lists of size 1, 000, 000. Measure and Print the time taken for this operation.

• Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this operation.

"""

# 3. Dot Product
# Using Python Lists
start_time = time.time()
dot_product = sum(a * b for a, b in zip(list1, list2))
end_time = time.time()
print(f"Python Lists Dot Product Time: {end_time - start_time:.6f} seconds")

# Using NumPy Arrays
start_time = time.time()
numpy_dot_product = np.dot(arr1, arr2)
end_time = time.time()
print(f"NumPy Dot Product Time: {end_time - start_time:.6f} seconds")

"""## 4. Matrix Multiplication
• Using Python lists, perform matrix multiplication of two matrices of size 1000x1000. Measure and print the time taken for this operation.

• Using NumPy arrays, perform matrix multiplication of two matrices of size 1000x1000. Measure and print the time taken for this operation.
"""

# 4. Matrix Multiplication
matrix_size = 1000
list_matrix1 = [[i for i in range(matrix_size)] for _ in range(matrix_size)]
list_matrix2 = [[i for i in range(matrix_size)] for _ in range(matrix_size)]

# Using Python Lists
start_time = time.time()
result_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*list_matrix2)] for row in list_matrix1]
end_time = time.time()
print(f"Python Lists Matrix Multiplication Time: {end_time - start_time:.6f} seconds")

# Using NumPy Arrays
numpy_matrix1 = np.array(list_matrix1)
numpy_matrix2 = np.array(list_matrix2)
start_time = time.time()
numpy_result_matrix = np.dot(numpy_matrix1, numpy_matrix2)
end_time = time.time()
print(f"NumPy Matrix Multiplication Time: {end_time - start_time:.6f} seconds")