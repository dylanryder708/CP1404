"""
Word Occurrences
Estimate: 15 minutes
Actual: 18 minutes
"""

word_to_count = {}
random_text = input("Text: ")
words = random_text.split()
for word in words:
    word_frequency = word_to_count.get(word, 0)
    word_to_count[word] = word_frequency + 1
words = list(word_to_count.keys())
words.sort()
max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
