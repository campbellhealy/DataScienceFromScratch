# splitCountList.py

from rawData import interests
from collections import Counter

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split()) 
                           
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
