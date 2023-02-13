import re
import collections

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)


s = "Bob hit a ball, the hit Ball flew far after it was hit."

b = ["hit"]

print(mostCommonWord(s,b))