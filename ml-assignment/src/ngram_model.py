# ngram_model.py
import random
from collections import defaultdict, Counter
from src.utils import clean_text, split_into_sentences, tokenize_sentences, replace_unk_words, add_padding

class TrigramModel:
    def __init__(self):
        self.trigram_counts = defaultdict(Counter)
        self.bigram_counts = Counter()
        self.vocab = set()

        self.start = "<s>"
        self.end = "</s>"
        self.unk = "<UNK>"

        self.trained = False

    def fit(self, text):
        """
        Trains the trigram model using the given text.
        """
        if not text or text.strip() == "":
            self.trained = True
            return

        cleaned = clean_text(text)
        sentences = split_into_sentences(cleaned)
        tokenized = tokenize_sentences(sentences)

        # Replace rare words with <UNK>
        tokenized, vocab = replace_unk_words(tokenized)
        self.vocab = vocab.union({self.start, self.end})

        # Add padding
        padded = add_padding(tokenized)

        # Count trigrams
        for sentence in padded:
            for i in range(len(sentence) - 2):
                w1, w2, w3 = sentence[i], sentence[i+1], sentence[i+2]
                self.trigram_counts[(w1, w2)][w3] += 1
                self.bigram_counts[(w1, w2)] += 1

        self.trained = True

    def _sample_next_word(self, w1, w2):
        """
        Samples the next word based on trigram probabilities.
        """
        context = (w1, w2)

        if context not in self.trigram_counts:
            choices = [word for word in self.vocab if word not in {self.start}]
            return random.choice(choices)

        counter = self.trigram_counts[context]
        total = self.bigram_counts[context]

        words = list(counter.keys())
        probabilities = [counter[w] / total for w in words]

        return random.choices(words, probabilities, k=1)[0]

    def generate(self, max_length=50):
        """
        Generates a sentence using the trigram model.
        """
        if not self.trained or len(self.trigram_counts) == 0:
            return ""

        w1, w2 = self.start, self.start
        result = []

        for _ in range(max_length):
            next_word = self._sample_next_word(w1, w2)

            if next_word == self.end:
                break

            result.append(next_word)
            w1, w2 = w2, next_word

        return " ".join(result)
