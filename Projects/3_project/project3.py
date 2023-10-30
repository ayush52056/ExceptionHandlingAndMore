import os
import re
from collections import Counter

def read_text_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                for line in file:
                    yield line


def preprocess_text(data):
    for text in data:
        # Tokenization, lowercasing, and punctuation removal (simplified)
        tokens = re.findall(r'\w+', text.lower())
        yield tokens


def calculate_word_frequencies(data):
    word_counter = Counter()
    for tokens in data:
        word_counter.update(tokens)
    return word_counter


def filter_and_sort_words(word_counter, min_frequency=5):
    for word, count in word_counter.items():
        if count >= min_frequency:
            yield (word, count)


if __name__ == "__main__":
    # Example: Process text data using the generator pipeline
    data_directory = "data"
    text_data = read_text_files(data_directory)
    preprocessed_data = preprocess_text(text_data)
    word_counter = calculate_word_frequencies(preprocessed_data)
    filtered_words = filter_and_sort_words(word_counter)

    # Print the top 10 words by frequency
    for word, count in sorted(filtered_words, key=lambda x: x[1], reverse=True)[:10]:
        print(f"{word}: {count}")
