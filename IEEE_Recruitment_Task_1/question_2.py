# Prompt the user to enter a paragraph
para = input("Enter paragraph: ")

# Import the string module to access punctuation characters
import string

# Create a translation table to remove punctuation from the text
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation from the input paragraph
clean_text = para.translate(translator)

# Convert the cleaned text to lowercase
ftext = clean_text.lower()

# Split the text into a list of words
w = ftext.split()

# Count the number of words
l = len(w)

# Check if the word count exceeds 100
if l > 100:
    print("Length exceeded 100 words")
else:
    n = 0  # Counter for palindrome words
    for i in w:
        # Check if the word is a palindrome
        if i == i[::-1]:
            print("Palindrom word: ", i)
            n += 1
    # If no palindrome words were found, print 0
    if n == 0:
        print(0)
        

        
        

 
