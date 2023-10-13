from googletrans import Translator

def translate_to_hinglish(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    # Replace specific words with English words in the translation
    hinglish_translation = translation.text.replace('टिप्पणी अनुभाग', 'comment section').replace('प्रतिक्रिया', 'feedback')
    return hinglish_translation

# Example usage
english_text = "Definitely share your feedback in the comment section."
hinglish_text = translate_to_hinglish(english_text)
print("Input (English):", english_text)
print("Output (Hinglish):", hinglish_text)
