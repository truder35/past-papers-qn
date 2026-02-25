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
    
# 2. (i). Given the following students details and marks: Enter these details from the keyboard
# ( Student name=Gloria Arinda, Student Number= SEP23/BCS/088U/F, Programming=90, Data
# Science= 87,Computer applications=77). Calculate the average mark and print the answer in 3
# decimal places. Display full details of the student ( 10 marks)
# 2. (ii) A car's miles per gallon can be calculated with the following formula. Write a program
# that asks the user for the number of miles driven and gallons used. It should calculate the car's
# miles-per-gallons-used and display the result MPG = milesDriven / gallonsOfGasUsed (10
# marks)
# 2. (iii) Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
# ( 5 marks)

# 
def student_details():
    name = input("Enter student name: ")
    student_number = input("Enter student number: ")
    programming_mark = float(input("Enter programming mark: "))
    data_science_mark = float(input("Enter data science mark: "))
    computer_applications_mark = float(input("Enter computer applications mark: "))
    
    average_mark = (programming_mark + data_science_mark + computer_applications_mark) / 3
    print(f"Student Name: {name}")
    print(f"Student Number: {student_number}")
    print(f"Programming Mark: {programming_mark}")
    print(f"Data Science Mark: {data_science_mark}")
    print(f"Computer Applications Mark: {computer_applications_mark}")
    print(f"Average Mark: {average_mark:.3f}") 
student_details() 
#  

def car_mpg():
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons used: "))
    
    mpg = miles_driven / gallons_used
    print(f"The car's miles-per-gallon is: {mpg:.2f}")
car_mpg()

def numbers_not_divisible_by_2():
    for num in range(1, 101):
        if num % 2 != 0:
            print(num)
numbers_not_divisible_by_2()

# 3 (i) Write a Python code snippet that asks the user for their age and prints "You are eligible" if
# the age is greater than or equal to 18, otherwise prints "You are not eligible."
# (5 marks)
# 3(ii) Write a Python function named "grade_students" that takes a student's mark as input
# and returns their corresponding grade based on the following criteria:
# 90 or above: 'A'
# 80-89: 'B'
# 70-79: 'C'
# 60-69: 'D'
# Below 60: 'F'
# 3(iii) Test the function with a mark of 85. (10 marks)
# 3 (iv) Modify the "grade_students" function to handle the case where the input mark is not a
# valid number. If the input is not a number, the function should return 'Invalid Input'. Test the
# function with both a valid mark and an invalid input (5 marks).
# 3(v) Enhance the "grade_students" function to also provide a message along with the grade:
# 'Excellent' for grades 'A' and 'B'
# 'Good' for grade 'C'
# 'Satisfactory' for grade 'D'
# 'Needs Improvement' for grade 'F'
# (vi) The function should now return both the grade and the corresponding message. Test the
# function with a mark of 78. (5 marks)

def age_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible")
    else:
        print("You are not eligible.")
age_eligibility()

# GRADE STUDENTS FUNCTION
def grade_students(mark):
    mark = input("Enter the student's mark: ")
    try:
        mark = float(mark)
    except ValueError: 
        return 'Invalid Input'
    
    
    if mark >= 90:
        grade = 'A'
        message = 'Excellent'
    elif 80 <= mark < 90:
        grade = 'B'
        message = 'Excellent'
    elif 70 <= mark < 80:
        grade = 'C'
        message = 'Good'
    elif 60 <= mark < 70:
        grade = 'D'
        message = 'Satisfactory'
    else:
        grade = 'F'
        message = 'Needs Improvement'
    
    return grade, message
print(grade_students(70))

grade_students(85)
print(grade_students(85))

# 3 (iv) Modify the "grade_students" function to handle the case where the input mark is not a valid number. If the input is not a number, 
# the function should return 'Invalid Input'. Test  the function with both a valid mark and an invalid input (5 marks).

def grade_students(mark):
    mark = input("Enter the student's mark: ")
    try:
        mark = float(mark)
    except ValueError: 
        return 'Invalid Input'
    if mark >= 90:
        grade = 'A'
        message = 'Excellent'

    elif 80 <= mark < 90:
        grade = 'B'
        message = 'Excellent'
    elif 70 <= mark < 80:
        grade = 'C'
        message = 'Good'    
    elif 60 <= mark < 70:
        grade = 'D'
        message = 'Satisfactory'
    elif mark < 60:
        grade = 'F'
        message = 'Needs Improvement'
    else:
        grade = 'Invalid Input'
        message = 'Invalid Input'    
    return grade, message
print(grade_students(78))

# 3(v) Enhance the "grade_students" function to also provide a message along with the grade:
# 'Excellent' for grades 'A' and 'B'
# 'Good' for grade 'C'
# 'Satisfactory' for grade 'D'
# 'Needs Improvement' for grade 'F'

def grade_students(mark):
    mark = input("Enter the student's mark: ")
    try:
        mark = float(mark)
    except ValueError: 
        return 'Invalid Input'
    if mark >= 90 and mark >= 80:
        grade  = 'A'
        message = 'Excellent'
    elif 70 <= mark < 80:
        grade = 'C'
        message = 'Good'
    elif 60 <= mark < 70:
        grade = 'D'
        message = 'Satisfactory'    
    elif mark < 60:
        grade = 'F'
        message = 'Needs Improvement'
    else:
        grade = 'Invalid Input'
        message = 'Invalid Input'   
    return grade, message
grade_students(89)

# 1.(ii) Given a list of integers [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum
# of all odd numbers and print the result. (5 marks)
# 1.(iii) Write a Python function that takes two numbers as input and returns their sum, difference,
# product, and quotient.(5 marks)
# 1.(v) Given the dictionary below, update the value of 'age' to 26 and add a new key-value pair
# ('city', 'Kampala’'). student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}(5 marks)
def sum_of_odd_numbers(numbers):
    odd_sum = 0
    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
numbers = [4, 7, 2, 9, 12, 15]
result = sum_of_odd_numbers(numbers)
print("Sum of odd numbers:", result)

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

def update_student_info(student_info):
    student_info['age'] = 26
    student_info['city'] = 'Kampala'
    return student_info
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
updated_info = update_student_info(student_info)
print(updated_info)


    
    
    
  









