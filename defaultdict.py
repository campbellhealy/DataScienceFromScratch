# defaultdict.py

from collections import defaultdict
from rawData import document
# 3 ways to look at this

# 1
# word_counts = {}
# for word in document:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1

# 2
# word_counts = {}
# for word in document:
#     try:
#         word_counts[word] += 1
#     except KeyError:
#         word_counts[word] = 1

# 3
# word_counts = {}
# for word in document:
#     previous_count = word_counts.get(word, 0)
#     word_counts[word] = previous_count + 1

# defaultdict use
word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1


print(word_counts)