from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """""
    Convert English Text to French Text.
    """""
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """""
    Convert French Text to English Text.
    """""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text

