#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.



#This function checks if a given number is a power of two
#Returns:True if n is a power of two, False otherwise
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n - 1)) == 0


# Get integer input from the user
while True:
  try:
    num = int(input("Enter an integer: "))
    break
  except ValueError:
    print("Invalid input. Please enter an integer.")

# Check if the number is a power of two
if is_power_of_two(num):
  print(f"{num} is a power of two.")
else:
  print(f"{num} is not a power of two.")
