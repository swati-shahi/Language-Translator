import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("500x500")
        self.root.config(bg="#f0f0f0")

        # Initialize the translator object
        self.translator = Translator()

        # Label for title
        self.title_label = tk.Label(root, text="Language Translator", font=("Arial", 20), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Input Textbox for text to be translated
        self.input_text_label = tk.Label(root, text="Enter text to translate:", font=("Arial", 12), bg="#f0f0f0")
        self.input_text_label.pack(pady=5)

        self.input_textbox = tk.Text(root, height=4, width=40, font=("Arial", 12))
        self.input_textbox.pack(pady=10)

        # Dropdown for source language selection
        self.source_lang_label = tk.Label(root, text="Select source language:", font=("Arial", 12), bg="#f0f0f0")
        self.source_lang_label.pack(pady=5)

        self.source_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly", width=30, font=("Arial", 12))
        self.source_lang_combobox.set("english")
        self.source_lang_combobox.pack(pady=5)

        # Dropdown for target language selection
        self.target_lang_label = tk.Label(root, text="Select target language:", font=("Arial", 12), bg="#f0f0f0")
        self.target_lang_label.pack(pady=5)

        self.target_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly", width=30, font=("Arial", 12))
        self.target_lang_combobox.set("spanish")
        self.target_lang_combobox.pack(pady=5)

        # Button to trigger translation
        self.translate_button = tk.Button(root, text="Translate", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.translate_text)
        self.translate_button.pack(pady=20)

        # Label to show translated text
        self.translated_text_label = tk.Label(root, text="Translated text will appear here", font=("Arial", 12), bg="#f0f0f0", wraplength=400)
        self.translated_text_label.pack(pady=10)

    def translate_text(self):
        # Get input text and selected languages
        text = self.input_textbox.get("1.0", "end-1c")
        source_lang = self.source_lang_combobox.get().lower()
        target_lang = self.target_lang_combobox.get().lower()

        # Map human-readable languages to their ISO codes for gTTS
        lang_code_map = {
            "urdu": "ur",
            "zulu": "zu",
            "russian": "ru",
            "japanese": "ja",
            "kannada": "kn",
            "french": "fr",
            "spanish": "es",
            "german": "de",
            "chinese": "zh",
            "english": "en",
            "gujarati": "gu",
            "spanish":"es",
            "german": "de",
            "italian": "it",
            "portuguese" :"pt",
            "dutch" : "nl",
            "russian" : "ru",
            "chinese (Simplified)" :"zh",
            "chinese (Traditional)" : "zh-tw",
             "japanese" : "ja",
             "korean": "ko",
             "hindi" : "hi",
             "arabic" : "ar",
             "bengali" : "bn",
             "urdu" : "ur",
             "tamil" : "ta",
            "telugu" : "te",
             "marathi" : "mr",
             "gujarati" : "gu",
             "malayalam" : "ml",
             "punjabi" : "pa",
             "kannada": "kn",
             "swahili" : "sw",
             "zulu": "zu",
              "vietnamese" : "vi",
              "turkish" : "tr",
              "thai" : "th",
              "polish" : "pl",
              "czech" : "cs",
              "greek" : "el",
              "hungarian" : "hu",
              "finnish" : "fi",
              "romanian": "ro", 
              "hebrew" : "he",
              "indonesian": "id",
              "malay" : "ms",
              "croatian" : "hr",
              "serbian" : "sr",
              "swedish" : "sv",
              "norwegian" : "no",
              "danish" : "da",
              "finnish" : "fi",
              "bulgarian" : "bg",
              "slovak" : "sk",
        }

        # Check if the selected language is supported by gTTS
        if target_lang not in lang_code_map:
            self.translated_text_label.config(text="Language not supported for speech synthesis.")
            return

        # Translate the text
        try:
            translation = self.translator.translate(text, src=source_lang, dest=target_lang)
            translated_text = translation.text

            # Update the translated text label
            self.translated_text_label.config(text=translated_text)

            # Get the language code for gTTS
            gtts_lang_code = lang_code_map.get(target_lang, "en")

            # Use gTTS to speak the translated text
            tts = gTTS(text=translated_text, lang=gtts_lang_code, slow=False)
            tts.save("translated_audio.mp3")

            # Play the audio file
            os.system("start translated_audio.mp3")

        except Exception as e:
            print(f"Error: {e}")
            self.translated_text_label.config(text="An error occurred. Please check your input and try again.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()