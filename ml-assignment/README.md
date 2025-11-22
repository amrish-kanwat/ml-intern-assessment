This project is a basic Trigram Language Model that I built from scratch for an ML internship assignment. The goal was to train a simple language model on a real text dataset and generate new sentences based on trigram probabilities. I used the book “Alice in Wonderland” (public domain) as the training data.

The idea is simple: the model looks at two previous words and predicts the next one. By repeating this process, it can generate new text that roughly follows the writing style of the original book.


Project Structure

ml-assignment/

│
├── data/
│   └── alice_in_wonderland.txt
│
├── src/
│   ├── ngram_model.py
│   ├── utils.py
│   └── generate.py
│
├── tests/
│   └── test_ngram.py
│
├── evaluation.md
└── README.md


ngram_model.py – main trigram model

utils.py – preprocessing functions

generate.py – trains the model + prints generated text

test_ngram.py – basic tests using pytest

How to Run

Make sure Python 3 is installed.

Install requirements:

pip install -r requirements.txt


Train the model and generate text:

python -m src.generate


Example output:

Generated Text:
but i m glad they ve begun asking riddles


The sentence changes every time because generation is probabilistic.


Preprocessing Steps

Before training, the text goes through the following steps:

convert to lowercase

remove unwanted characters

split into sentences

tokenize using .split()

replace rare words with UNK

add s s at the start and /s at the end

This keeps the input clean and easier for the trigram model to learn from.


How the Model Works

The model stores trigram counts in a dictionary where each key is a pair of words (w1, w2) and the value is a Counter of possible next words.

Text generation works like this:

Start with s s

Look up possible next words

Sample one using probability weights

Shift the context window forward

Stop at /s or when max length is reached

This creates short, slightly unpredictable sentences that resemble the training text.


Tests
Run the tests with:

pytest


The tests check basic training and ensure the generate function returns a valid string.
