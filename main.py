import random

print("Document application!")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
birth_year = int(input("Enter your birthyear: "))
place = input("Where are you from: ")
status = input("Whats your occupation: ")

#Version 1 of function for current age:
# age = 2025 - birth_year

#Version 2 of function for current age:
def age(birth_year, current_year=2025):
    return current_year - birth_year


inputs = [name, surname, birth_year, place, status]
inputs.insert(3, age(birth_year))

print("These are your registered data:")
print("Name:", inputs[0])
print("Surname:", inputs[1])
print("Birth year:", inputs[2])
print("Age:", inputs[3])
print("Place:", inputs[4])
print("Occupation:", inputs[5])
valid_data= input("Are all data correct? (Press Y for Yes and N for No)")
if valid_data == "Y" or valid_data == "y":
    print("Go to the next steps.")
elif valid_data.upper() == "N":
    print("Fill again!")
else: print("Please press Y or N")

print("Are you a robot? Please answer the question below:")

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
answer = int(input(f"What is {num1} + {num2}? "))
if answer == num1 + num2:
    print("Correct! You can continue.")
else: print("Wrong!Please verify again.")