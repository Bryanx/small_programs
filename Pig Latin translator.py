pyg = 'ay'

original = input('Enter a word:')
word = original.lower()  # makes the word lowercase
first = word[0]  # takes the first letter from the word

new_word = word + first + pyg  # sum of the word, first letter and, "ay"
new_word = new_word[1:len(new_word)]

# isalpha is to test wether letters are entered
if len(original) > 0 and original.isalpha():
    print(new_word)
else:
    print('empty')