# vuln_sample.py

import os

def delete_user_data(username):
    os.system(f"rm -rf /home/{username}")  # Command injection risk

password = input("Enter your password: ")  # Sensitive data collection

eval("print('Eval used')")  # Dangerous function

print("Done")
