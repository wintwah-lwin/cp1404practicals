"""Word occurences
Estimate: 20 minutes
Time taken: 16 minutes"""

text = input("Enter text: ")
words = text.split()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
sorted_words = sorted(word_to_count.keys())
max_width = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{max_width}} : {word_to_count[word]}")
