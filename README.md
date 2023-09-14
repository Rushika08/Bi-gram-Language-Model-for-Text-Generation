# Bi-gram-Language-Model-for-Text-Generation
The Bi-gram model is based on the assumption that the probability of a word depends only on the previous word, thus simplifying the language modeling task.

Task 1: Data Preprocessing
You will be provided with the following corpus of text data. Perform basic data preprocessing steps to clean and tokenize the text. The preprocessing steps should include:
1. Removing punctuation and special characters.
2. Converting all text to lowercase.
3. Tokenizing the text into individual words.
Note: You can use your regular expression knowledge here. 

The Corpus:
"The quick brown fox jumps over the lazy dog. The lazy dog barked at the moon."


Task 2: Build Bi-gram Language Model
Once you have preprocessed the data, construct a Bi-gram language model. Calculate the probabilities of each word given its previous word.

Steps to build the Bi-gram model:
1. Count the occurrences of each word in the corpus.
2. Count the occurrences of each word pair (bi-gram) in the corpus.
3. Calculate the conditional probabilities of each word given its previous word (using maximum likelihood estimation).


Task 3: Generate Text using Bi-gram Model
After building the Bi-gram model, implement a text generation function. The function should take a seed word as the input and use the Bi-gram model to generate a random sequence of words based on the probabilities.

Steps to Generate Text
1. Given a seed word, find its most probable next word using the Bi-gram probabilities.
2. Append the next word to the generated text.
3. Repeat the above step to generate the desired length of text.
