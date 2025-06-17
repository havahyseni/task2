# Task 2
Document Application

This is a simple Python console application designed to collect user data, validate inputs, and perform basic checks such as age verification and a CAPTCHA-like test to confirm the user is not a robot.

#Project Description
The application collects personal information from the user, including name, surname, birth year, place of origin, and occupation. It calculates the user’s age, checks if they are of legal age, and confirms data correctness before allowing the user to proceed. The program also uses a randomly generated math question as a CAPTCHA to prevent automated entries.

#Features
User input collection with validation
Age calculation based on birth year
Legal age verification (default 18 years)
Capitalization of first letters in name and surname
Input validation feedback
CAPTCHA test with a randomly generated addition question

#Code Structure
#bash
document-application/
└── document_application.py    


#Main Functions
age(birth_year, current_year=2025): Calculates current age from birth year
legal_age(age, legal=18): Checks if user is above legal age threshold
invalid(): Prints an invalid input warning
capitalize_name(name, surname): Capitalizes first letters of name and surname

#How to Run
Make sure Python 3 is installed on your system.
Save the script document_application.py.
Run the script from your terminal or command prompt:

#bash
python document_application.py

Follow the on-screen prompts to enter your data.
Confirm your details and complete the robot verification.

#Dependencies
Python Standard Library only 
Uses random module for CAPTCHA question generation

#Input Validation & Logic
Validates numerical input for birth year.
Validates user confirmation input for correctness.
Uses conditional logic (if/else) to direct program flow and validate data.