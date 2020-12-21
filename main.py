from app.translator import Translator

if __name__ == '__main__':
    translator = Translator()
    while(True):
        phrase = input('Enter a phrase: ')
        print(translator.translate(phrase))
