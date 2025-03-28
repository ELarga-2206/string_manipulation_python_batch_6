# endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# FUNCTION custom_endswith(main_string, suffix):
# suffix_length = LENGTH(suffix)
# main_length = LENGTH(main_string)
# IF suffix_length > main_length:
# RETURN False
# RETURN substring(main_string, main_length - suffix_length, main_length) == suffix
# END FUNCTION

def custom_endswith(main_string, suffix):
    suffix_len = len(suffix)
    main_len = len(main_string)
    
    if suffix_len > main_len:
        return False
    
    return main_string[main_len - suffix_len:] == suffix