sentence = input("Write a sentence:\n")
s = sentence.replace(" ", "").lower()
if s == s[::-1]:
    print("That's a palindrome")
else:
    print("Not a palindrome.")