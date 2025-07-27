# File I/O Errors
    # Can also use specific file errors

from translate import Translator
try:
    with open("text.txt", mode = "r") as my_file:
        text = my_file.read()
        language = Translator(to_lang="ja") # Code for Japanese
        transalte_text = language.translate(text)
        print(transalte_text)
except FileNotFoundError as err:
    print("check file path")
    raise(err)