#Question 2: String Manipulation and Loops
#Write a function letter_histogram(word) that takes in a string word and returns a dictionary where the keys are the letters in the word, and the values are the number of times each letter appears.

#For example:
#python
#Copy code
#word = "banana"
#result = letter_histogram(word)
#print(result)  # Output: {'b': 1, 'a': 3, 'n': 2}

def letter_histogram(word):
    out = {}
    for letter in word:
        if letter in out:
            out[letter]+=1
        else:
            out[letter] = 1
    return out

word = "banana"
print(f"The Result of letter histogram  for a given word is {letter_histogram(word)}")