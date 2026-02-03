# Task 11 – Regular Expressions for Data Validation

## Description
This project demonstrates how to use Python regular expressions to validate
user input such as email addresses, Indian mobile numbers, and passwords.

## Tools Used
- Python
- re module (built-in)
- VS Code / Jupyter Notebook

## Features
- Email validation using regex
- Indian mobile number validation
- Password strength validation
- Reusable functions
- User-friendly success/error messages
- Handles invalid and empty inputs

## Validation Rules

### Email
- Must follow standard email format
- Example: user@example.com

### Mobile Number
- Must be a valid Indian number
- Starts with 6–9
- Exactly 10 digits

### Password
- Minimum 8 characters
- At least one letter
- At least one digit
- At least one special character (@$!%*#?&)

## How to Run
```bash
python regex_validation.py
