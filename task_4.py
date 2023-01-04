def reversed_words():
    reversed_words = []
    words = set()
    for line in open("words.txt", encoding="utf-8"):
        words.add(line.strip())
    for word in words:
       if word[::-1] in words:
           pair = word, word[::-1]
           reversed_words.append(pair)
    reversed_words.sort()
    return reversed_words
