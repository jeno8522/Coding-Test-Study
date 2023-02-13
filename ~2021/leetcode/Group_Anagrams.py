import collections

def groupAnagrams(strs):

    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

s = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(s))

