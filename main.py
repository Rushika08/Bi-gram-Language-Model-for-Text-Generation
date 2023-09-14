# 20_ENG_061 - NLP Assignment 1

import re
import time

from nltk.tokenize import word_tokenize



# Task 1: Data Preprocessing

user_corpus = input("Enter the corpus (or press Enter to go with default corpus): ")
default_corpus = "The quick brown fox jumps over the lazy dog. The lazy dog barked at the moon."

if user_corpus == "":       # if user corpus is empty
    user_corpus = default_corpus

# Removing punctuation and special characters.
user_corpus = re.sub(r'[^\w\s]', '', user_corpus)

# Converting all text to lowercase.
user_corpus = user_corpus.lower()

# Tokenizing the text into individual words.
tokens = word_tokenize(user_corpus)

#Printing the preprocessed text.
print("\n","Task 01","\n\n","Preprocessed text: ", " ".join(tokens), "\n")

time.sleep(2)       #delay of 2 seconds




# Task 2: Build Bi-gram Language Model

# Count the occurrences of each word in the corpus.
word_count = {}                 # initializing an empty dictionary to store word count
for word in tokens:
    if word in word_count:      # if word is already present in the dictionary
        word_count[word] += 1
    else:                       # if word is not present in the dictionary
        word_count[word] = 1

# Count the occurrences of each word pair (bi-gram) in the corpus.
bi_gram_count = {}              # initializing an empty dictionary to store bi-gram count
for i in range(len(tokens)-1):
    bi_gram = tokens[i] + "|" + tokens[i+1]     # creating bi-gram by combining the current word and the next word
    if bi_gram in bi_gram_count:    # if bi-gram is already present in the dictionary
        bi_gram_count[bi_gram] += 1
    else:                           # if bi-gram is not present in the dictionary
        bi_gram_count[bi_gram] = 1

# Calculate the conditional probabilities of each word given its previous word (using maximum likelihood estimation).

#Assumption: The probability of a word depends only on the previous word (Markov assumption)

# initializing an empty dictionary to store conditional probabilities
conditional_probabilities = {}

for word in word_count:
    for bi_gram in bi_gram_count:
        if word in bi_gram.split("|")[0]:
            conditional_probabilities[bi_gram] = bi_gram_count[bi_gram] / word_count[word]

#Printing conditional probabilities line by line in the format: (previous word, next word): probability
print("\n","Task 02","\n\n","Conditional Probabilities: ")
print(" Format: (previous word | next word): probability","\n")

for bi_gram in conditional_probabilities:
    print(bi_gram, ":", conditional_probabilities[bi_gram])

time.sleep(2)       #delay of 2 seconds




# Task 3: Generate Text using Bi-gram Model
print("\n","Task 03","\n")

# Given a seed word, find its most probable next word using the Bi-gram probabilities.
def find_next_word(current_word1, probability_dict):
    next_word = "<unk>"    # initializing next word to <unk>
    max_prob = 0           # initializing maximum probability to 0
    for key in probability_dict.keys():
        if current_word1 in key.split("|")[0]:
            if probability_dict[key] > max_prob:        # check if probability of current word is greater than maximum probability
                max_prob = probability_dict[key]        # if yes, update maximum probability
                next_word = key.split("|")[1]

    return next_word

# Append the next word to the generated text.
def generate_text(seed_word, length, probability_dict):
    if seed_word == "":         # if seed word is empty
        return ""

    if length == 1:             # if length of text to be generated is 1
        return seed_word

    current_word2 = seed_word   # initializing current word to seed word
    generated_text = seed_word  # initializing generated text to seed word

    for i in range(length-1):
        next_word = find_next_word(current_word2, probability_dict)
        generated_text += " " + next_word
        current_word2 = next_word
    return generated_text


#Generating text using Bi-gram model
seed_word = input("Enter the seed word: ")
length = int(input("Enter the length of text to be generated: "))
generated_text = generate_text(seed_word, length, conditional_probabilities)

#Printing the generated text
print("\n","Generated text: ", "\n", generated_text, "\n")

time.sleep(2)       #delay of 2 seconds




#Enhancement

#Steps to implement add-1 smoothing:
#1 Add 1 to the count of each word pair (bi-gram) in the corpus.
#2. Add the vocabulary size to the count of each word in the corpus.
#3. Calculate the conditional probabilities of each word given its previous word
#4. Generate text using the add-1 smoothed Bi-gram model.

# Add the vocabulary size to the count of each word in the corpus.
enhanced_word_count = word_count.copy()
for word in enhanced_word_count:
    enhanced_word_count[word] += len(word_count)

# Add 1 to the count of each word pair (bi-gram) in the corpus.
enhanced_bi_gram_count = bi_gram_count.copy()
for bi_gram in enhanced_bi_gram_count:
    enhanced_bi_gram_count[bi_gram] += 1

# Calculate the conditional probabilities of each word given its previous word (using maximum likelihood estimation).
enhanced_conditional_probabilities = {}

for word in enhanced_word_count:
    for bi_gram in enhanced_bi_gram_count:
        if word in bi_gram.split("|")[0]:
            enhanced_conditional_probabilities[bi_gram] = round(enhanced_bi_gram_count[bi_gram] / enhanced_word_count[word], 4)
            #rounded upto 4 decimal places

#Printing smoothed conditional probabilities line by line in the format: (previous word, next word): probability
print("\n\n","Implementing add-1 smoothing technique","\n\n","Enhanced Conditional Probabilities: ")
print(" Format: (previous word | next word): probability","\n")

for bi_gram in enhanced_conditional_probabilities:
    print(bi_gram, ":", enhanced_conditional_probabilities[bi_gram])

print("\n")

#Generating text using add-1 smoothed Bi-gram model
seed_word = input("Enter the seed word: ")
length = int(input("Enter the length of text to be generated: "))
generated_text = generate_text(seed_word, length, enhanced_conditional_probabilities)

#Printing the generated text
print("\n\n","Generated text after smoothing: ", "\n", generated_text, "\n")




