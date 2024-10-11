string = input("Введіть слова, розділені пробілами:")
word = string.split()
long_word = max(word, key=len)

print(long_word)
print(len(long_word))