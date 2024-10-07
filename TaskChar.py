word = 'testing'

word_length = len(word)

if word_length % 2 == 0:

    middle = word[word_length // 2 - 1:word_length // 2 + 1]
else:

    middle = word[word_length // 2]

print(middle)
