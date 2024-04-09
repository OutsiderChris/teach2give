#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
  """
  This function counts the number of vowels (a, e, i, o, u) in a sentence.

  Args:
      sentence: A string containing the sentence.

  Returns:
      The number of vowels in the sentence.
  """
  vowels = "aeiouAEIOU"
  vowel_count = 0
  for char in sentence:
    if char in vowels:
      vowel_count += 1
  return vowel_count

sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print(f"Number of vowels in '{sentence}': {vowel_count}")
