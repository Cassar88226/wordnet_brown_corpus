import re

phone_list = ['(0121) 123 4567', '(0121) 123 4567 ext. 890', '01211 234567', '(01 21) 12 34 567', '01211234567', '01211 234567', '01 211 23 45 67']

# run regular expression function
def run_re(re_ex, src_list):
    re_compile = re.compile(re_ex)
    passed = list(filter(re_compile.match, src_list))
    print(passed)


# Part-1 (Regular Expressions + Python)
# Task 1:

# a1 & a2
# a1
# regular expression : \(01[2-6]1\)\s\d{3}\s\d{4}
# In this case, phone number has the expression (01x1) nnn nnnn, so first 4 digits should be enclosed round bracket
# and in round bracket part, 01 should be appeard, then only one digit in range from 2 to 6([2-6]), next 1
# then, space character(\s), three digits(\d{3}), space character(\s), four digits(\d{4})
# a2
re_ex = "\(01[2-6]1\)\s\d{3}\s\d{4}"
run_re(re_ex, phone_list)

# b1 & b2
# regular expression : \(01[2-6]1\)\s\d{3}\s\d{4}\sext\.\s\d{1,4}
# prefix part is the same as a1, but phone number should have space character(\s), 'ext' string, '.' punctation(\.), up to 4 digits(\d{1,4})
re_ex = "\(01[2-6]1\)\s\d{3}\s\d{4}\sext\.\s\d{1,4}"
run_re(re_ex, phone_list)

# c1 & c2
# regular expression : ^\(?01\s?[2-6]\s?1\)?\s?([0-9]|\s){3,5}([0-9]|\s){4,7}
# round bracket may or not appear(^\(?), 
# space character may or not (\s?) may or not appear in 3 digits(([0-9]|\s){3,5}) and 4 digits(([0-9]|\s){4,7})
re_ex = "^\(?01\s?[2-6]\s?1\)?\s?([0-9]|\s){3,5}([0-9]|\s){4,7}"
run_re(re_ex, phone_list)

