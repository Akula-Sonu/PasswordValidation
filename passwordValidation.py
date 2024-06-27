import re
pattern = re.compile( r"""
    (?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$%#@&])(?!.*\s) (?!.*(.)\1{2,})(?!.*(?:012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))[A-Za-z0-9$%#@&]{8,} """, re.VERBOSE)
common_passwords = {"password", "123456", "123456789", "12345678", "12345", "1234567", "123123"}
password = input("enter a password: ")
while(True):
    if password in common_passwords:
        print("The password is common. Choose a different password.")
    elif any(seq in password for seq in consecutive):
        print("The password should not contain sequences of three or more consecutive characters (e.g., 'abc' or '123').")
    elif (len(password) < 8):
        print("the password should be more than 8 characters")
    elif not re.search('[A-Z]',password):
        print("at least one character should be capitalize")
    elif not re.search('[a-z]',password):
        print("must contain at least one character")
    elif not re.search('[0-9]',password):
        print('must contain at least one number')
    elif not re.search('[$%#@&]',password):
        print("should contain at least one of the following (@,#,$,%,&)")
    else:
        print("password is valid")
        break
    password = input("enter a password: ")