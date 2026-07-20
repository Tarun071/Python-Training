# ● Read your age and print it.
def read_age():
    age=int(input("Enter your age : "))
    print(age)
read_age()

# ● Read two integers and print their sum.
def sum_of_integers():
    a=int(input("Enter 1 number : "))
    b=int(input("Enter 2 number :"))
    print(f"Sum of {a} and {b} is {a+b} ")
sum_of_integers()


# ● Read two numbers and print:
# Addition
# Subtraction
# Multiplication
# Division
def calc():
    n1=int(input("Enter 1 number : "))
    n2=int(input("Enter 2 number :"))
    print(f"Addition = {n1+n2}")
    print(f"Substraction = {n1-n2}")
    print(f"Multiplication = {n1*n2}")
    if n2>0:
        print(f"Devison = {n1/n2}")
calc()

# ● Read the radius of a circle and calculate its area.
def area_of_circle():
    r=int(input("Enter Radius of circle : "))
    res=3.141*(r*r)
    print(f"area Of Circle : {res}")
area_of_circle()

# ● Read the length and width of a rectangle and calculate its area.  
def area_of_rectangle():
    l=int(input("Enter length of rectangle : "))
    b=int(input("Enter breadth of rectangle : "))
    print(f"area of Reactangle : {l*b}")
area_of_rectangle()

# ● Read the side of a square and calculate its area.
def area_of_square():
    s=int(input("Enter side of the square : "))
    print(f"Area of square = {s*s}")
area_of_square()

# ● Read temperature in Celsius and convert it to Fahrenheit.
def cel_farhn():
    temp=float(input(" Enter celsius : "))
    print(f"farenheit = {(temp*1.8)/35}")
cel_farhn()

# ● Read your birth year and calculate your age.
from datetime import date 
def age_cal():
    year=int(input("Enter your birth year : "))
    cur=date.today().year
    print(f"your age is : {cur-year}")
age_cal()

# ● Read five numbers and print their average.
def multi_value_input():
    n1,n2,n3,n4,n5=input("Enter 5 numbers : ").split()
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    n4=int(n4)
    n5=int(n5)
    print(f"{n1},{n2},{n3},{n4},{n5}")
multi_value_input()

# ● Swap two numbers without using a temporary variable.
def swap():
    a=int(input())
    b=int(input())
    b=a+b
    a=b-a
    b=b-a
    print(f"A= {a}, B= {b}")
swap()

# ● Store the length and width of a rectangle and print both values.
def length_and_breadth():
    l=int(input())
    b=int(input())
    print("Length of rectangle = {l}")
    print(f"Breadth of rectangle ={b}")
length_and_breadth()

# ● Read five numbers and print their average.
def avg():
    n1=int(input())
    n2=int(input())
    n3=int(input())
    n4=int(input())
    n5=int(input())
    print(f"Average = {(n1+n2+n3+n4+n5)/5.0}")
avg()

# ● Convert kilometers to meters.
def km_to_m():
    km=int(input())
    m=km*1000
    print(f"{km} kms = {m} meters")
km_to_m()

# ● Convert meters to centimeters.
def m_to_cm():
    m=int(input())
    cm=m*100
    print(f"{m} meters = {m} centimeters")
m_to_cm()

# ● Convert hours into minutes.
def hours_to_mints():
    h=int(input())
    m=h*60
    print(f"{h} hours = {m} Minutes")
hours_to_mints()

# ● Program to calculate Simple intrest
def simple_intrest():
    p=int(input())
    t=int(input())
    r=int(input())
    si=(p*t*r)/100
    print(f"Simple Intrest = {si}")
simple_intrest()