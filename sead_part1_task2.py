import re

def check_email(regex, email):
    if(re.search(regex,email)):  
        print("Valid Email")
    else:  
        print("Invalid Email")

regex = "^[a-zA-Z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)+((.com)|(.co.uk)|(.net)|(.ac.uk))$"

regex1 = "^[a-zA-Z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_‘{|}~-]+)*@[a-z0-9]+((\.[a-z]{3})|((\.[a-z]{2})(\.[a-z]{2})))$"
# email addres has to start with character within a-z, A-Z, 0-9, printable punctations an include a-z, A-Z, 0-9, printable punctations
# and should have one @ symbol, and last doman part should be .com, .co.uk, .net, .ac.uk
check_email(regex, 'ankitrai326@gmail.com')
check_email(regex, 'An.kItr._ai326@gmail.com')

check_email(regex1, 'ankitrai326@gmail.com')
check_email(regex1, 'An.kItr._ai326@gmail.com')
