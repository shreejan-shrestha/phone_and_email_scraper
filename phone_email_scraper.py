#! python3

import re, pyperclip

# Create a regex object for the phone numbers

phone_num_regex = re.compile(r'(?:\+977[- ])?\d{2}-?\d{7,8}')

# Create a regex object for the email addresses

email_regex = re.compile(r'''
[a-zA-Z0-9\._-]+ # name part
@ # @ sign
[a-zA-Z0-9\._-]+  # domain name
.[a-zA-Z]+ # .com part
[.[a-zA-Z]]? # .np (country level domain)
''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email/phone from the text

extracted_phone_num = phone_num_regex.findall(text)
extracted_email = email_regex.findall(text)

# Copy the extracted email/phone to the clipboard

results = '\n'.join(extracted_phone_num) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)