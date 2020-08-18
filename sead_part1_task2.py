import re

def check_email(regex, email):
    if(re.search(regex,email)):  
        print("Valid Email")
    else:  
        print("Invalid Email")  
regex = '^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
# email addres has to start with character within a-z, A-Z, 0-9 and may include ., english character, digit
# and should have one @ symbol, and include '.' punctation, end with domain name(english character, digit)
check_email(regex, 'ankitrai326@gmail.com')
check_email(regex, 'AnkItrai326@gmail.com')