from palindrome import is_palindrome

def main():
    # Test cases
    print(is_palindrome("racecar")) # True
    print(is_palindrome("raceCar")) # True
    print(is_palindrome("hello")) # False
    print(is_palindrome("a")) # True
    print(is_palindrome("")) # False
    
main()