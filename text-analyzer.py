text = input("Enter your text here: ")
text = text.lower()

letters = [] # This variable makes our list 

# Now we can add elements to our list using method '.append' 
letters.append(input("Enter the first letter here: ").lower())
letters.append(input("Enter the second letter here: ").lower())
letters.append(input("Enter the third letter here: ").lower())

print("\n")
print("LETTERS REPETITION")

letter_repetition1 = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print(f"The repetition of letter {letters[0]} is {letter_repetition1}")
print(f"The repetition of letter {letters[1]} is {letter_repetition2}")
print(f"The repetition of letter {letters[2]} is {letter_repetition3}")

print("\n")
print("NUMBERS OF WORDS")

text2 = text.split()
print(f"We have found {len(text2)} words")

print("\n")
print("THE FIRST AND THE LAST LETTER")
print(f"The first letter of text is {text[0]}")
print(f"The last letter of text is {text[-1]}")

print("\n")
print("INVERTED ORDER OF TEXT")

text2.reverse()
joined_text = " ".join(text2)
print(joined_text)

print("\n")
print("IS THERE 'PYTHON' IN TEXT?")

is_python = 'python' in text
dic = {True: "was", False: "was not"}

print(f"There {dic[is_python]} 'python' in text")