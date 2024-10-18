def palindrome(string):
    return string == string[::-1]
Given_string = input("Enter a string: ")
if palindrome(Given_string):
    print(f"{Given_string} is a palindrome.")
else:
    print(f"{Given_string} is not a palindrome.")