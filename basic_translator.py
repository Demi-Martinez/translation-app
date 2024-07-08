from googletrans import Translator

def translate_text():
    translator = Translator()
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language (e.g., 'en', 'es', 'fr'): ")

    try:
        translation = translator.translate(text, dest=target_lang)
        print("Translation:", translation.text)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    while True:
        translate_text()
        continue_translating = input("Translate another text? (y/n): ")
        if continue_translating.lower() != "y":
            break
