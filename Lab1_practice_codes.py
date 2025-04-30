# Program number 1
a = 36
b = 12
add = a + b
print("Addition of the numbers is:", add)

# Program number 2
a = 23
b = 45
sub = a - b
print("Subtraction of the numbers is:", sub)

# Program number 3
a = 23
b = 45
multi = a * b
print("Multiplication of the numbers is:", multi)

# Program number 4
a = 23
b = 45
div = a / b
print("Division of the numbers is:", div)

# Program number 5
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

add = x + y
sub = x - y
mul = x * y
div = x / y

print("Addition of the two user-defined numbers is:", add)
print("Subtraction of the two user-defined numbers is:", sub)
print("Multiplication of the two user-defined numbers is:", mul)
print("Division of the two user-defined numbers is:", div)

# Program number 6
hrs = int(input("Enter number of hours: "))
minutes = hrs * 60
print("Minutes in", hrs, "hours is:", minutes)

# Program number 7
minutes = int(input("Enter number of minutes: "))
hrs = minutes // 60
print("Hours in", minutes, "minutes is:", hrs)

# Program number 8
dollar = int(input("Enter number of dollars: "))
rupee = dollar * 48
print("Rupees in", dollar, "Dollars are:", rupee)

# Program number 9
rupee = int(input("Enter number of Rupees: "))
dollar = rupee // 48
print("Dollars in", rupee, "Rupees are:", dollar)

# Program number 10
dollar = int(input("Enter number of dollars: "))
pound = dollar * 70
print("Pounds in", dollar, "Dollars are:", pound)

# Program number 11
pound = int(input("Enter number of Pounds: "))
dollar = pound // 70
print("Dollars in", pound, "Pounds are:", dollar)

# Program number 12
gm = int(input("Enter the number of grams: "))
kgm = gm // 1000
print(gm, "grams contain", kgm, "kilograms")

# Program number 13
kgm = int(input("Enter the number of kilograms: "))
gm = kgm * 1000
print(kgm, "kilograms contain", gm, "grams")

# Program number 14
cel = int(input("Enter Celsius: "))
F = (9 / 5 * cel) + 32
print("Fahrenheit in", cel, "Celsius is:", F)

# Program number 15
F = int(input("Enter Fahrenheit: "))
C = 5 / 9 * (F - 32)
print("Celsius in", F, "Fahrenheit is:", C)

# Program number 16
principal = int(input("Enter Principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time: "))

interest = (principal * rate * time) // 100
print("The interest on the given figures is:", interest)

# Program number 17
l = int(input("Enter the side length of the square: "))
a = l * l
p = 4 * l
print("Area of the square is:", a)
print("Perimeter of the square is:", p)

# Program number 18
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
a = l * b
p = 2 * (l + b)
print("Area of the rectangle is:", a)
print("Perimeter of the rectangle is:", p)

# Program number 19
r = int(input("Enter the radius of the circle: "))
a = 3.14 * r * r
print("Area of the circle is:", a)

# Program number 20
l = int(input("Enter the base length of the triangle: "))
h = int(input("Enter the height of the triangle: "))
a = h * l / 2
print("Area of the triangle is:", a)

# Program number 21
gross_salary = float(input("Enter the gross salary: "))
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print("Net Salary:", net_salary)

# Program number 22
gross_sales = float(input("Enter the gross sales: "))
discount = 0.10 * gross_sales
net_sales = gross_sales - discount
print("Net Sales:", net_sales)

# Program number 23
sub1 = int(input("Enter the marks of Maths: "))
sub2 = int(input("Enter the marks of English: "))
sub3 = int(input("Enter the marks of Science: "))

total_marks = sub1 + sub2 + sub3
avg_marks = total_marks / 3

print("Total marks obtained by the student:", total_marks)
print("Average marks obtained by the student:", avg_marks)

# Program number 24
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

temp = x
x = y
y = temp

print("After swapping:")
print("x =", x)
print("y =", y)
