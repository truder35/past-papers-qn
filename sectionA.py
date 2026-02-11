# 1.(i) Write a Python function named "circle_area" that takes the radius of a circle as a 
# parameter and returns the area of the circle. Use the formula: area = π * r^2. (Assume π ≈ 3.14)
# . Test the function with a radius of 4. (5 marks) 
from unittest import result


def circle_area(radius):
    x = 3.14 * (radius ** 2)
    return x

print(f"The area of a circle with radius 4 is: {circle_area(4)}")
# calling the function 


#a) create a function that calculates the area of a triangle, the function must take in two parameters,(base and height)

def triangle_area(base, height):
    area = 0.5 * base * height
    return area
result = triangle_area(5, 10)         
print(f"The area of a triangle is {result:.0f}")
# calling the function


# b) create a function that calculates the perimeter of a rectangle
def rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    print(f"The perimeter of a rectangle of length {length} and width {width} is {perimeter}")
# calling the function     
rectangle_perimeter(5, 3) 

# 1.(ii) Given a list of integers [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of 
# all odd numbers and print the result. (5 marks) 
numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for num in numbers:
    if num % 2 != 0:
        odd_sum += num
print(f"The sum of all odd numbers in the list is: {odd_sum}")






# .(iii) Write a Python function that takes two numbers as input and returns their sum, difference, product, 
# and quotient.(5 marks)
def arithmetic_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 
    print(f"the sum is {sum_result}, the difference is {difference_result}, the product is {product_result} and the quotient is {quotient_result}")

print(arithmetic_operations(10, 5))

# Another approach
def arithmetic_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 
    return sum_result, difference_result, product_result, quotient_result
num1 = 4
num2 = 2
result2 = arithmetic_operations(num1, num2)
print(f"The sum is {num1 + num2}, the difference is {num1 - num2}, the product is {num1 * num2} and the quotient is {num1 / num2}")
sum_output, difference_output, product_output, quotient_output = arithmetic_operations(4, 2) 
print(f"The sum of {num1} and {num2} is: {sum_output}")
print(f"The difference of {num1} and {num2} is: {difference_output}")
print(f"The product of {num1} and {num2} is: {product_output}")
print(f"The quotient of {num1} and {num2} is: {quotient_output}")










