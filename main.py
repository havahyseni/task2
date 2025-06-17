import random  

print("Document application!")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
birth_year = int(input("Enter your birthyear: "))
place = input("Where are you from: ")
status = input("Whats your occupation: ")


#function for current age:
def age(birth_year, current_year=2025):
    return current_year - birth_year


#function to check if user is of legal age
def legal_age(age, legal=18):
    if age >= legal:
        print("You are of legal age.")
        return True
    else:
        print("You are not of legal age.")
        return False  


#function for invalid input of user
def invalid():
    print("Invalid input! Please enter a valid option.")

#function to make first letters of the name capital
def capitalize_name(name, surname):
    return f"{name.capitalize()} {surname.capitalize()}"

# inputs = [name, surname, birth_year, place, status] #list
# inputs.insert(3, age(birth_year)) #adding age to the list (in position between birthyear and place)
#changed the above list to dict
user_data = {
    "name": name,
    "surname": surname,
    "birth year": birth_year,
    "age": age(birth_year),
    "place": place,
    "occupation": status
}


print("These are your registered data:")
print("Name:", user_data["name"])
print("Surname:", user_data["surname"])
print("Birth year:", user_data["birth year"])
print("Age:", user_data["age"])
print("Place:", user_data["place"])
print("Occupation:", user_data["occupation"])
valid_data= input("Are all data correct? (Press Y for Yes and N for No)")
if valid_data == "Y" or valid_data == "y":
    print("Go to the next steps.")
elif valid_data.upper() == "N":
    print("Fill again!")
else: 
    invalid()


print("Are you a robot? Please answer the question below:")

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
answer = int(input(f"What is {num1} + {num2}? "))
if answer == num1 + num2:
    print("Correct! You can continue.")

else: invalid()