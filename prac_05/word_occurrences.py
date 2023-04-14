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

sorted_list = []
for word in COUNT_WORDS:
    sorted_list.append(word)

sorted_list.sort()
for i in sorted_list:
    print(f"{i:<10}: {COUNT_WORDS[i]}")

