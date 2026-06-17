from deep_translator import GoogleTranslator

text = input("Enter text: ")

translated = GoogleTranslator(source='en', target='fr').translate(text)

print("Translated Text:", translated)