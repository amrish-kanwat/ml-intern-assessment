This project involved creating a trigram (N=3) language model from scratch. The goal was to learn word-sequence patterns from a text corpus and generate new text based on trigram probabilities. Below is a summary of the main design decisions I made.

1. N-Gram Count Storage
 
I stored trigram counts using:

A dictionary where each key is a pair of words (w1, w2).

Each key maps to a Counter that stores possible next words and their frequencies.

A separate Counter stores the total number of times each (w1, w2) pair appears.

This structure keeps the implementation simple and allows for fast lookups when generating text.

2. Text Cleaning and Preprocessing

The text was cleaned using the following steps:

Converting everything to lowercase.

Removing characters that aren’t letters, digits, or basic punctuation.

Splitting the text into sentences using punctuation marks.

Tokenizing each sentence using Python’s .split().

This keeps the text consistent and easier for the model to learn from.

3. Handling Unknown Words

To reduce sparsity, I handled rare words using the following approach:

Counted all words in the dataset.

Any word that appeared once or less was replaced with a special token called UNK.

This ensures that unusual words do not affect the model’s ability to calculate probabilities.

4. Padding Sentences

Since a trigram model needs two previous words for context, I added padding around every sentence. The padding looks like:

START START ...words... END.

START = beginning-of-sentence marker.

END = sentence-ending marker.

Padding gives the model a consistent starting point and helps it know where a sentence ends.

5. Probability Calculation and Sampling

I calculated trigram probabilities with:

P(next | w1, w2) = count(w1, w2, next) / total_count(w1, w2).

To generate text, I used weighted sampling with random.choices(). This creates more natural and varied sentences instead of always picking the most frequent next word.

6. Generate Function

The text generation process works as follows:

Start with the two START tokens.

Sample the next word based on trigram probabilities.

Shift the context window forward.

Stop when the END token appears or when the maximum length is reached.

This results in sentences that resemble the structure and vocabulary of the training text.

7. Overall Design Choices

I kept the design simple and easy to follow:

Clear preprocessing steps.

Straightforward data structures.

Direct probability calculations.

Probabilistic text generation.
