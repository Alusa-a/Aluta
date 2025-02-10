# Built-in functions/ Standard-Library

y = max(43, 87, 98, 76, 98, 78,)
print("The maximum value is", y)

x = min(54, 76, 45, 23)
print("The minimum value is", x)


# User defined functions
def school():
    print("eMobilis")


school()

def plus():
    print(x + y, "is the sum")

plus()


# Parameter(Variable) and argument(Value stored in argument)
def multiply(a , b):
     print(a * b)

multiply(6 , 5)
multiply(10 , 30)

def employee(name ,age, gender, salary, position):
    print(name ,age, gender, salary, position)

employee("Maureen", 25, "Female", 560000, "CEO")
employee("John", 52, "Male", 80000, "Managing Director")
employee("Mary", 28, "Female", 560000, "CEO")
employee("Mark", 32, "Female", 560000, "CEO")
employee("Harry", 27, "Female", 560000, "CEO")
employee("Sean", 43, "Male", 560000, "CEO")
employee("Elsie", 36, "Female", 230000, "CEO")
employee("Victoria", 56, "Female", 450000, "CEO")
employee("Charles", 47, "Male", 100000, "CEO")
employee("Walter", 29, "Male", 94000, "CEO")
employee("Caleb", 34, "Male", 760000, "CEO")



# Program to display details of 5 patients in a hospital
#Using a user defined function, implement a parameter and arguments
#Full name, gender, age, ailment


def patient(firstname , lastname, age, gender, ailment):
    print(firstname, lastname ,age, gender, ailment)


patient("Glen", "Kombo", 34, "Male", "Dysentric amoeba")
patient("Vanessa", "Wachira", 37, "Female", "Malaria")
patient("Stephen", "Wabomba", 29, "Male", "Chlamaydia")
patient("Rose", "Matolo", 41, "Female", "Tuberculosis")
patient("Lilian", "Wanyama", 24, "Male", "Scarlet fever")