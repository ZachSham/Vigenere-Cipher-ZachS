import string
from collections import Counter
import matplotlib.pyplot as plt

class VigenereCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = string.ascii_uppercase  # Standard alphabet used for encryption
        self.english_letter_freq = {
            'E': 12.0, 'T': 9.1, 'A': 8.1, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3, 
            'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 
            'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0, 
            'K': 0.8, 'X': 0.2, 'J': 0.2, 'Q': 0.1, 'Z': 0.1
        }

    def _clean_text(self, text):
        return ''.join(filter(str.isalpha, text)).upper()  # Only letters, uppercase

    def _extend_key(self, text):
        clean_text = self._clean_text(text)
        extended_key = self.key.upper() * (len(clean_text) // len(self.key)) + self.key.upper()[:len(clean_text) % len(self.key)]
        return extended_key

    def _shift_char(self, char, key_char, encrypt=True):
        char_pos = self.alphabet.index(char.upper())
        key_pos = self.alphabet.index(key_char.upper())
        if encrypt:
            return self.alphabet[(char_pos + key_pos) % len(self.alphabet)]
        else:
            return self.alphabet[(char_pos - key_pos) % len(self.alphabet)]

    def encrypt(self, plaintext):
        extended_key = self._extend_key(plaintext)
        encrypted_text = []
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                encrypted_char = self._shift_char(char, extended_key[key_index], encrypt=True)
                encrypted_text.append(encrypted_char if char.isupper() else encrypted_char.lower())
                key_index += 1
            else:
                encrypted_text.append(char)  # Non-alpha characters are added as is
        return ''.join(encrypted_text)

    def decrypt(self, ciphertext):
        extended_key = self._extend_key(ciphertext)
        decrypted_text = []
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                decrypted_char = self._shift_char(char, extended_key[key_index], encrypt=False)
                decrypted_text.append(decrypted_char if char.isupper() else decrypted_char.lower())
                key_index += 1
            else:
                decrypted_text.append(char)  # Non-alpha characters are added as is
        return ''.join(decrypted_text)

    def frequency_analysis(self, text):
        clean_text = self._clean_text(text)
        letter_count = Counter(clean_text)
        total_letters = len(clean_text)

        # Calculate frequency percentage for each letter in the ciphertext
        freq_distribution = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}

        # Sort letters by frequency in descending order
        sorted_freq = dict(sorted(freq_distribution.items(), key=lambda item: item[1], reverse=True))

        # Display the frequency analysis
        self._plot_frequency(sorted_freq)
        
        return sorted_freq

    def _plot_frequency(self, freq_distribution):
        letters = list(freq_distribution.keys())
        frequencies = list(freq_distribution.values())

        plt.figure(figsize=(10, 5))
        plt.bar(letters, frequencies, color='skyblue')
        plt.title('Frequency Analysis of Ciphertext')
        plt.xlabel('Letters')
        plt.ylabel('Frequency (%)')
        plt.show()

# Ask user for input
key = input("Enter the key for encryption: ")
cipher = VigenereCipher(key)

plaintext = input("Enter the message you want to encrypt: ")
encrypted = cipher.encrypt(plaintext)
decrypted = cipher.decrypt(encrypted)

print("Original Message:", plaintext)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)

# Perform frequency analysis on the encrypted text
freq_analysis = cipher.frequency_analysis(encrypted)
print("Frequency Analysis:", freq_analysis)
