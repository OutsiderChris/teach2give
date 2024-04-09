#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#string, and then returns the result string.
#Examples: 
#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming

def capitalize_words(s):
    # Split the string into words
    words = s.split()
    
    # Capitalize the first letter of each word and join them back into a string
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words with space
    return ' '.join(capitalized_words)

# Accept input from the user
input_string = input("Enter a string: ")
result = capitalize_words(input_string)
print("Result:", result)
