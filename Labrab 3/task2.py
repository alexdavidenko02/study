word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

unique_letters = set(word1).symmetric_difference(set(word2))

print("Літери, які зустрічаються тільки в одному слові:")
for letter in unique_letters:
    print(letter, end=' ')
