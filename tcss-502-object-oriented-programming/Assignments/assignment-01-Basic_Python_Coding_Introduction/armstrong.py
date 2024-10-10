## Armstrong Numbers
# Preston Harms

"""
An Armstrong number (also known as a perfect or narcissistic number) is a number whose sum of each of its
digits raised to the power of the count of digits in the number is the same as the number itself.  So if
the number were 123 (which has 3 digits), you would evaluate as follows (note that the ** is the
exponentiation operator in Python):

1**3 + 2**3 + 3**3

The result of the above operation would be 1 + 8 + 27, which is 36. This means 123 is not an Armstrong
number.Your job is to obtain a number n from the user that is greater than or equal to 10 and less than
or equal to 100,000,000 (10 <= n <= 100000000). You must ensure a number in this range is entered.
You must then determine all Armstrong numbers from 10 through n. Your program must then output those
numbers, one per line starting with the smallest Armstrong number found. Format your output so that it
is *identical* to what is shown below. Note that the x's and y's would have actual digits for the numbers
found. The ... (ellipses) just says there may be more numbers and should not be included in your output.
"""

def get_user_input():
    # Set response constants
    max_input = 100000000
    min_input = 10
    input_prompt = "Please enter an integer from 10 through 100,000,000 (without the commas):"
    invalid_input_message = "Please enter a valid input"

    # Prompt the user for input
    user_input = input(input_prompt)

    # Validate User Input
    while not user_input.isdigit():
        print(invalid_input_message)
        user_input = input(input_prompt)
    
    # Convert the user input to an integer
    user_input = int(user_input)

    # Check to see if the input is a number and repeat until the
    while user_input < min_input or user_input > max_input:
        print("Please enter a number between 10 and 100,000,000.")
        user_input = input(input_prompt)
        
    return user_input

def calculate_armstrong_numbers(user_input):
    # Set response constants
    min_input = 10

    # Initializing the variables being used
    count = 0
    output_prompt = f"The Armstrong numbers from 10 through {user_input} are:\n"

    # Opening the conversation
    print(output_prompt)

    # Loop through from the minimum input to the user input value
    for i in range(min_input + 1, user_input):
        # Check each number for armstrong value
        if is_armstrong_number(i):
            # Print the value if armstrong and increase the count
            print(i)
            count += 1

    # Ending the conversation
    print(f"\nThe total number of Armstrong numbers found was {count}")
    return

def is_armstrong_number(num):
    # Check the length of the number for power
    power = len(str(num))

    # Init the sum value
    sum: int = 0

    # Create a copy of the number
    remaining_val = num

    # Loops through each didget to get the armstrong value
    for i in range(power):
        sum += (remaining_val%10)**power
        remaining_val = int(remaining_val/10)

    return sum == num

def main():
    print("Welcome to the Armstrong number calculator.")
    user_input = get_user_input()
    calculate_armstrong_numbers(user_input)

main()