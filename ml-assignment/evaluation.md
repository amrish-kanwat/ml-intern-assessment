Evaluation Summary: Trigram Language Model

This project involved building a trigram (N=3) language model from scratch. The model learns patterns of word sequences from a text corpus and generates new text by sampling from trigram probabilities. Here’s a brief overview of the key design choices I made during the implementation.

1. N-Gram Count Storage

To store trigram counts effectively, I used:

A dictionary with bigram keys:  
(w1, w2) → Counter({w3: count})

A separate Counter for bigram totals:  
This keeps track of how often each (w1, w2) pair appears.

This structure simplifies the implementation, supports quick lookups, and works well with Python’s built-in defaultdict and Counter.

2. Text Cleaning & Preprocessing

The preprocessing pipeline includes:

- Lowercasing all text
- Removing unwanted characters using a regex (keeping only a–z, digits, and . ! ?)
- Splitting text into sentences based on punctuation
- Tokenizing each sentence using .split()

These steps ensure clean input for n-gram construction without adding unnecessary complexity.

3. Handling Unknown Words

To handle rare words, I:

Counted all words in the corpus.

Replaced words with a frequency of 1 or less with the token <UNK>.

This reduces sparsity and helps the model deal with new words smoothly during generation.

4. Padding Sentences

Since a trigram model needs two previous words for context, I padded each sentence as:

<s> <s> ... tokens ... </s>

<s>: start-of-sentence token  
</s>: end-of-sentence token  

Padding ensures consistent trigram windows and provides clear start and end points.

5. Probability Calculation & Sampling

I calculated the probability of the next word using:

P(w3 | w1, w2) = count(w1, w2, w3) / total_count(w1, w2)

For sampling, I used:

random.choices() with probability weights.  
This allows for variations in the generated text and avoids predictable outputs.

6. Generate Function

The generation process:

Begins with <s> <s> as the initial context

Samples the next word using trigram probabilities

Slides the context window forward

Stops when </s> is produced or the maximum length is reached

This creates sentences that reflect the structure and vocabulary of the training text.

7. Overall Design Decisions

I focused on clarity, readability, and simplicity:

- Simple data structures
- Clear preprocessing pipeline
- Direct probability computation
- Probabilistic text generation

The final model is easy to understand, extend, and debug while meeting all the assignment's functional requirements.