#Write a program that takes an integer as input and returns an integer with reversed digit 
#ordering.


def reverse_integer(num):
  """
  This function reverses the digit order of an integer.

  Args:
      num: An integer

  Returns:
      An integer with the digits reversed.
  """
  reversed_num = 0
  sign = 1 if num >= 0 else -1
  num = abs(num)
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num * sign


num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(f"Reversed number: {reversed_num}")
