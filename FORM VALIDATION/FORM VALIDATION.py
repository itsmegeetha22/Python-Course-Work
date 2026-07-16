Try AI directly in your favourite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for ₹1,950 ₹489 for 3 months
1
100%
import re

'''
fullname = input("Enter the full name: ")
pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'

res = re.fullmatch(pattern,fullname)
print("Valid name" if res else "Invalid name")

phone = input("Enter the phone number: ")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'

res = re.fullmatch(pattern,phone)
print("Valid phone number" if res else "Invalid phone number")
'''


email = input("Enter the email: ")
pattern = r'^[a-zA-Z0-9._]+@+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

res = re.fullmatch(pattern,email)
print("Valid Email" if res else "Invalid Email")





'''

def validate_name(name):
    pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
    return bool(re.fullmatch(pattern, name))

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))

def validate_phone(phone):
    pattern = 
    return bool(re.fullmatch(pattern, phone))

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.fullmatch(pattern, password))


def validate_username(username):
    pattern = r'^[a-zA-Z0-9]{5,15}$'
    return bool(re.fullmatch(pattern, username))

'''

