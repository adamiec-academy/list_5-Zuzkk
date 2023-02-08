def longest_word():
    data = []
    for line in open("words.txt", encoding="utf-8"):
        data.append(line.strip())
    longest_word = ""
    for word in data:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
