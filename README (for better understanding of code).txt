Password Validation 

-> regular expression is used for the password validation
-> and the password is only valid when it satisfies all the condition

-> the conditions:
Minimum length of 8 characters with allowed set
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character from the set $%#@&
No spaces allowed
No more than two consecutive identical characters
No sequences of three or more consecutive characters







don't worry you can generate the pattern from the [REGEX website]
    (?=.*[A-Z])                                                  # At least one uppercase letter

    (?=.*[a-z])                                                  # At least one lowercase letter

    (?=.*[0-9])                                                  # At least one digit

    (?=.*[$%#@&])                                                # At least one special character from the set $%#@&

    (?!.*\s)                                                     # No spaces allowed

    (?!.*(.)\1{2,})                                              # No more than two consecutive identical characters

    (?!.*(?:012|123|234|345|456|
    567|678|789|890|abc|bcd|cde|def|
    efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop
    |opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))                    # No sequences of three or more consecutive characters

    [A-Za-z0-9$%#@&]{8,}                                          # Minimum length of 8 characters with allowed set
    """, re.VERBOSE




