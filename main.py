"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

def isPalindrom(word):
    import string
    word = word.lower()
    for punctuation in string.punctuation:
    word = word.replace(punctuation, '')
    word = word.replace(' ', '')
    return word == word[::-1]
    a = list(['hello', 'Искать Такси', 'list', 'level'])

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

def isPalidromList(words):
    Palindroms = []
    for word in words:
        if isPalindrom(word):
            Palindroms.append(word)
    return Palindroms
print (a)
print(isPalidromList(a))

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

def isPalindromString(text):
    import string
    text = text.lower()
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    text = text.replace(' ', '')

    palindromes = {text for text in cleaned_text if isPalindrom(text) and text}
    
    return list(palindromes)

print(isPalindromString("Madam, Anna went to the civic center"))

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""
