import os
import string
from collections import Counter

def create_sample_file():
    print("The file 'sample.txt' does not exist. Please type a paragraph to create it:")
    content = input("Enter your paragraph: ")
    with open("sample.txt", "w") as file:
        file.write(content)

def write_to_sample_file():
    content = input("Enter your paragraph: ")
    with open("sample.txt", "a") as file:
        file.write(content)

def read_file_content(filename):
    with open(filename, "r") as file:
        return file.read()

def count_word_frequency(text):
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()
    return Counter(words)

def save_report(filename, total_words, common_words, top_common):
    with open(filename, "w") as file:
        file.write("Word Count Report")
        file.write(f"Total words: {total_words}\n")
        file.write(f"Top {top_common} words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count}\n")

def main():
    if not os.path.exists("sample.txt"):
        create_sample_file()
    else:
        write_to_sample_file()

    content = read_file_content("sample.txt")
    word_counts = count_word_frequency(content)

    total_words = sum(word_counts.values())
    top_common = int(input("How many most common words would you like to see? "))
    common_words = word_counts.most_common(top_common)

    print(f"Total words: {total_words}")
    print(f"Top {top_common} most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")

    save_report("word_count_report.txt", total_words, common_words, top_common)

if __name__ == "__main__":
    main()