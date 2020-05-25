from datetime import date

year = date.today().year

name = str.title(input("Please type your name: "))
age = int(input("Enter with your age: "))
r_number = int(input("Please type any number: "))

while (age is not True):
    if type(age) is int:
        birth_year = year - age
        century = birth_year + 100
        for i in range(r_number):
            print("Dear {0} you will be a centenary in {1}".format(name, century))
        break
    else:
        print("You need to try again, with a valid number")