#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.


# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the first two Fibonacci numbers
print(a)
print(b)

# Generate and print the remaining Fibonacci numbers up to 100
while b < 100:
    a, b = b, a + b
    print(b)
    
