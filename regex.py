import re

text = """
Hello, my email is mridulchavhan@gmail.com.
You can contact mitadt@gmaail.com.
My college email is mridulchavhan567@gmail.com.
For support, contact support@mitadtu.org.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)