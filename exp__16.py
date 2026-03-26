https://github.com/sidabdullah07 /Python-Programs
print("251A010")
import re
def validate_phone(phone):
pattern = r"^(\+91[\-\s]?)?[6 -9]\d{9}$"
return re.match(pattern, phone)
def validate_email(email):
pattern = r"^[a-zA-Z0-9._%+-] +@[a-zA-Z0-9.-]+\.[a-zA -Z]{2,}$"
return re.match(pattern, email)
number: ") 
phone input("Enter your phone
email = input("Enter your email ID: ")
if validate_phone(phone):
print("Valid Phone Number")
else:
print("Invalid Phone Number")
if validate_email(email):
print("Valid Email ID")
else:
print("Invalid Email ID")
