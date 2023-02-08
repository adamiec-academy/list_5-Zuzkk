def reversed_words():
    reversed_words = []
    words = set()
    for line in open("words.txt", encoding="utf-8"):
        words.add(line.strip())
    for word in words:
        rev_word = word[::-1]
        if rev_word in words and rev_word != word:
            reversed_words.append(tuple(sorted((word, rev_word))))
    reversed_words = list(set(reversed_words))
    reversed_words.sort()
    return reversed_words
