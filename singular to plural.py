# Образовать от формы единственного числа русского (английского, немецкого, французского, испанского) имени
# существительного его форму множественного числа путем добавления соответствующего суффикса (окончания).

word = input('Enter your word ')       # ввод слова

one_letter = word[-1]                  # оставляем последнюю букву в слове
two_letter = word[-2:len(word)]        # оставляем еще две последние буквы (это все понадобится для проверки по правилу)

# список исключений номер 1
exception1 = ['roof', 'proof', 'belief', 'chef', 'chief', 'handkerchief']
# список исключений номер 2
exception2 = ['sheep', 'fish', 'deer', 'moose', 'swine', 'buffalo', 'shrimp', 'trout',
              'aircraft', 'offspring', 'species', 'salmon']
# список исключений номер 3
exception3 = {'child': 'children', 'die': 'dice', 'foot': 'feet', 'goose': 'geese', 'louse': 'lice', 'man': 'men',
              'mouse': 'mice', 'ox': 'oxen', 'person': 'people', 'tooth': 'teeth', 'woman': 'women'
              }
# список исключений номер 4
exception4 = ['photo', 'piano', 'halo']

if word in exception1:                 # ну и собсна все правила, что я нашла на сайте
    print(word + 's')                  # https://www.grammarly.com/blog/plural-nouns/
elif word in exception2:
    print(word)
elif word in exception3:
    print(exception3[word])
elif two_letter == 'ss' or two_letter == 'sh' or two_letter == 'ch' or two_letter == 'es':
    print(word[0:-2] + 'es')
elif two_letter == 'fe':
    print(word[0:-2] + 'ves')
elif one_letter == 'f':
    print(word[0:-1] + 'ves')
elif two_letter == 'us':
    print(word[0:-2] + 'i')
elif two_letter == 'is':
    print(word[0:-2] + 'es')
elif two_letter == 'on' or two_letter == 'um':
    print(word[0:-2] + 'a')
elif one_letter == 'y':
    if word[-2] in 'aoieu':
        print(word + 's')
    else:
        print(word[0:-1] + 'ies')
elif word in exception4:
    print(word + 's')
elif one_letter == 'o':
    print(word + 'es')
else:
    print(word + 's')
