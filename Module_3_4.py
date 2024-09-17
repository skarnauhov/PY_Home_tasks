def single_root_words(root_word, *other_words):
    same_words = []
    s = 0
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
            s += 1
    if s == 0:
        for word in other_words:
            if word.lower() in root_word.lower():
                same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

result3 = single_root_words('r', 'richiest', 'orichalcum', 'cheers', 'richies', 'rrr', 'rr', 'r' )
print(result3)