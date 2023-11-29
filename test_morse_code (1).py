from youssef import text_to_morse, morse_to_text

import unittest

class TestMorseCodeConversion(unittest.TestCase):
    def test_text_to_morse(self):
        # Test cases for text to Morse code conversion
        self.assertEqual(text_to_morse("Hello"), ".... . .-.. .-.. ---")
        self.assertEqual(text_to_morse("123"), ".---- ..--- ...--")
        self.assertEqual(text_to_morse(" "), " ")

    def test_morse_to_text(self):
        # Test cases for Morse code to text conversion
        self.assertEqual(morse_to_text(".... . .-.. .-.. ---"), "HELLO")
        self.assertEqual(morse_to_text(".---- ..--- ...--"), "123")
        self.assertEqual(morse_to_text(" "), " ")
        self.assertEqual(morse_to_text("--. --- --- -.."), "GOOD")
        self.assertEqual(morse_to_text("... --- ..."), "SOS")
        self.assertEqual(morse_to_text("...-.-"), "")  # Testing invalid Morse code sequence
        self.assertEqual(morse_to_text("----.--.-.-."), "")  # Testing invalid Morse code sequence

if __name__ == '__main__':
    unittest.main()

