sentence = input("Введіть речення: ")

words = sentence.split()  # Розділити речення на слова
matched_words = []

for word in words:
    if len(word) >= 2 and word[0].lower() == word[-1].lower():
        matched_words.append(word)

if matched_words:
    print("Слова, що починаються і закінчуються на одну і ту ж літеру:")
    for matched_word in matched_words:
        print(matched_word)
else:
    print("У введеному реченні немає слів, які починаються і закінчуються на одну і ту ж літеру.")
