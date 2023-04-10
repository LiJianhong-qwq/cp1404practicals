"""
Word Occurrences
Estimate: 20 minutes
Actual:  27 minutes
"""
COUNT_WORDS = {}

sentence = input("Text: ")
for i in sentence.split():
    if i not in COUNT_WORDS:
        COUNT_WORDS[i] = 1
    else:
        COUNT_WORDS[i] += 1

list = []
for word in COUNT_WORDS:
    list.append(word)

list.sort()
for i in list:
    print(f"{i:<10}: {COUNT_WORDS[i]}")

