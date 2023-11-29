morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}

def text_to_morse(text):
    # Converts a text phrase to Morse code
    morse_code = ' '.join([morse_code_dict.get(char.upper(), '') for char in text])
    return morse_code

def morse_to_text(morse_code):
    morse_code_words = morse_code.strip().split(' ')  
    decrypted_text = ''

    for word in morse_code_words:
        if word == '':
            decrypted_text += ' '  
        else:
            try:
                decrypted_text += [key for key, value in morse_code_dict.items() if value == word][0]
            except IndexError:
                print("Error: Invalid Morse code detected during decryption.")
                return ''

    return decrypted_text

def display_menu():
    # Displays the menu options 
    print("\nMenu:")
    print("a. Translate English to Morse code")
    print("b. Translate Morse code to English")
    print("c. Exit")

def main():
    # Main function for the translation application 
    while True:
        display_menu()
        choice = input("Enter your choice (a, b, or c): ").lower()

        if choice == 'a':
            input_text = input("Enter a phrase to translate to Morse code: ")
            translated_text = text_to_morse(input_text)
            print("Translated Morse Code:", translated_text)
        elif choice == 'b':
            input_morse_code = input("Enter Morse code to translate to English: ")
            translated_text = morse_to_text(input_morse_code)
            if translated_text:
                print("Translated Text:", translated_text)
        elif choice == 'c':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter 'a', 'b', or 'c'.")

if __name__ == "__main__":
    main()
