# endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# FUNCTION custom_endswith(main_string, suffix):
# suffix_length = LENGTH(suffix)
# main_length = LENGTH(main_string)
# IF suffix_length > main_length:
# RETURN False
# RETURN substring(main_string, main_length - suffix_length, main_length) == suffix
# END FUNCTION

def ends(main, suffix):
    return len(main) >= len(suffix) and main[-len(suffix):] == suffix
    
main = input("Main string: ")
suffix = input("check if ends with: ")
print("Ends with!" if ends(main, suffix) else "Doesn't end with")