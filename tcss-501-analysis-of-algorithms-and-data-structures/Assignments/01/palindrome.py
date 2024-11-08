"""
Name: Preston Harms
UWNetId: pharms
TimeComplexity = O(n)
"""

"""
Evaluates a given string and determines whether or not it is a palindrome.
:param the_string: The string to evaluate.
:returns: True when the string is a palindrome, False otherwise.
"""
def is_palindrome(the_string):
    # Base Cases
    if len(the_string) == 0: # TRIVIAL CASE WHERE THE STRING IS EMPTY
        return False
    
    # Convert the string to lowercase and get the end index of the string.
    lower_string = the_string.lower()
    end_index = len(lower_string) - 1
    
    # Iterate through the string and compare the characters from one end to the other.
    # Stop if any characters do not match, ir if we reached the middle of the string.
    # If we reach the middle of the string, then the string is a palindrome.
    # Otherwise, the string is not a palindrome.
    for i in range(0, len(the_string) // 2):
        if lower_string[i] != lower_string[end_index - i]:
            return False
    return True
