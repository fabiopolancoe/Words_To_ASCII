def translate_word():
    word = input("Write a word to translate\t")
    word = word.lower()
    word_list = list(word)
    asciichar = 0
    for letters in word_list:
        asciichar = ord(letters) + asciichar
    print(asciichar)
    translate_word()
translate_word()