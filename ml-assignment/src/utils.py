# This file is optional.
# You can add any utility functions you need for your implementation here.
# utils.py
import re
from collections import Counter

def clean_text(text):
    """
    Cleans the raw text by keeping only letters, numbers, and sentence punctuation.
    Converts text to lowercase and removes extra spaces.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\.\!\? ]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def split_into_sentences(text):
    """
    Splits the cleaned text into sentences based on ., !, ?
    """
    sentences = re.split(r"[\.!\?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def tokenize_sentences(sentences):
    """
    Tokenizes each sentence into a list of words.
    """
    tokenized = [s.split() for s in sentences]
    return tokenized

def replace_unk_words(tokenized, min_freq=2, unk_token="<UNK>"):
    """
    Replaces rare words (frequency <= min_freq) with <UNK>
    """
    freq = Counter()

    for sentence in tokenized:
        freq.update(sentence)

    vocab = set()
    for word, count in freq.items():
        if count >= min_freq:
            vocab.add(word)

    new_tokenized = []
    for sentence in tokenized:
        new_sentence = []
        for word in sentence:
            if word in vocab:
                new_sentence.append(word)
            else:
                new_sentence.append(unk_token)
        new_tokenized.append(new_sentence)

    vocab.add(unk_token)
    return new_tokenized, vocab

def add_padding(tokenized, start="<s>", end="</s>"):
    """
    Adds two <s> tokens at the start and one </s> at the end of each sentence.
    """
    padded = []
    for sentence in tokenized:
        padded_sentence = [start, start] + sentence + [end]
        padded.append(padded_sentence)
    return padded
