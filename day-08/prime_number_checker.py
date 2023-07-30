# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.
# Hint
# Remember the modulus:
# https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
#
# Make sure you name your function/parameters the same as when it's called on the last line of code.
#
# Use the same wording as the Example Outputs to make sure the tests pass.
#
# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.


# Write your code below this line 👇
def prime_checker(number):
    result = True
    for index in range(4, number):
        if number % index == 0:
            result = False

    if result:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
