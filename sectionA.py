# 1.(i) Write a Python function named "circle_area" that takes the radius of a circle as a 
# parameter and returns the area of the circle. Use the formula: area = π * r^2. (Assume π ≈ 3.14)
# . Test the function with a radius of 4. (5 marks) 
# from unittest import result


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


# 5i) Define a python class named "book" with attributes: title, author, and pages.
# provide a method to display information about the book.Create an instance of the class and display the inforation.(10marks)
# A class is a blueprint or template for creating objects. It defines the attributes and behaviors that the objects created from 
# the class will have.
# a book is a class that represents a book objects with attributes such as title, author and pages, while books in the library are objects.
# An object is a real thing built using that blueprint.
# A blueprint is like a plan or template that tells the computer how to make objects
# self refers to the curent object being created.

# Creating a class named book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

book1 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book1.display_info()


# ii)Create a derived class named "EBook" that inherits from the "Book" class.
# Add an additional attribute "format" to the EBook class. Display information for an instance of the EBook class. (8marks)

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")

# # ebook object

ebook1 = EBook("The Great Gatsby", "Scott Fitzgerald", 180, "PDF")
ebook1.display_info()
# super is a function that gives access to the parent class. It is used to call the parent class's methods and access its attributes from the child class.
# Ebook is a digital version of a book that can be read on electronic devices.


# iii) Create a function on the "Book" class that returns only the book title and its author.(3marks)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"

    

# Define the following terms
# a) Class 2marks  b object (2marks)
    #  A class is a blueprint or template for creating objects
    # An object is an instance of a class that has its own unique identity and state. It is created based on the structure 
    # defined by the class and can have its own values for the attributes defined in the class.
    




