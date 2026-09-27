# Experiment 13: Bigram-Based Next Word Prediction System
# Environment: Python 3.x

import string
import re
from collections import defaultdict, Counter

def clean_and_tokenize(text):
    """
    Cleans raw text by converting to lowercase and stripping punctuation,
    then tokenizes it into words.
    """
    text = text.lower()
    # Replace punctuation marks with spaces and extract word tokens
    tokens = re.findall(r'\b[a-z0-9]+\b', text)
    return tokens

def build_bigram_model(corpus):
    """
    Builds a bigram frequency mapping where:
    model[word] = Counter({next_word1: count1, next_word2: count2, ...})
    """
    tokens = clean_and_tokenize(corpus)
    bigram_model = defaultdict(Counter)

    # Construct bigrams (word_i, word_{i+1})
    for i in range(len(tokens) - 1):
        current_word = tokens[i]
        next_word = tokens[i + 1]
        bigram_model[current_word][next_word] += 1

    return bigram_model, tokens

def predict_next_word(bigram_model, input_word):
    """
    Predicts the most probable next word and lists alternative candidate frequencies.
    """
    cleaned_input = input_word.strip().lower()

    if cleaned_input not in bigram_model:
        return None, None

    # Frequency distribution of all words following cleaned_input
    candidates = bigram_model[cleaned_input]

    # Most common word (highest bigram count)
    predicted_word, highest_freq = candidates.most_common(1)[0]
    return predicted_word, candidates

def main():
    # Training Corpus
    corpus = """
    Artificial Intelligence is transforming industries.
    Artificial Intelligence is changing the world.
    Artificial Intelligence is a powerful technology.
    Artificial Intelligence will shape future automation.
    Machine learning and artificial intelligence drive modern computing.
    The world is evolving rapidly through technology.
    """

    print("==========================================================")
    print("      BIGRAM-BASED NEXT WORD PREDICTION SYSTEM           ")
    print("==========================================================")

    bigram_model, tokens = build_bigram_model(corpus)
    print(f"Total tokens processed: {len(tokens)}")
    print(f"Unique vocabulary words: {len(bigram_model)}\n")

    # Interactive test loop / demo inputs
    test_words = ["artificial", "intelligence", "is", "unknown"]
    for word in test_words:
        print(f"Input Word: '{word}'")
        predicted, candidates = predict_next_word(bigram_model, word)
        if predicted:
            print(f"  -> Predicted Next Word : '{predicted}'")
            print(f"  -> Candidate Bigram Frequencies:")
            for next_w, count in candidates.most_common():
                print(f"       ({word} -> {next_w}): count = {count}")
        else:
            print(f"  -> No prediction available (word not found in corpus vocabulary).")
        print("-" * 58)

if __name__ == "__main__":
    main()