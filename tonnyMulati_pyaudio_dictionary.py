from PyDictionary import PyDictionary
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    # Create an instance of gTTS and save the audio file
    tts = gTTS(text=text, lang='en')
    tts.save('audible.mp3')

    # Use the playsound module to play the audio file
    playsound('audible.mp3')
    os.remove('audible.mp3')


def main():
    dictionary = PyDictionary()

    while True:
        search = input("Enter the word you are searching the meaning for: ")
        if not search.isalpha():
            print("Please enter a valid word (letters only).")
            continue

        meanings = dictionary.meaning(search)

        if not meanings:
            print(f"Sorry, we could not find any meanings for '{search}'.")
            continue

        text_1 = f"Meanings of {search}"
        print(text_1)
        speak(text_1)

        for meaning_type, definitions in meanings.items():
            text_2 = f"{meaning_type}:"
            print(text_2)
            speak(text_2)

            for definition in definitions:
                text = f"  - {definition}"
                print(text)
                speak(text)

                # Only read the first definition aloud
                break

        # Ask the user if they want to look up another word
        while True:
            again = input("Do you want to look up another word? (y/n)")
            if again.lower() == 'y':
                break
            elif again.lower() == 'n':
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == '__main__':
    main()
