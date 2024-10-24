# Vigenère Cipher Implementation

This project is a Python-based implementation of the Vigenère cipher, a classical encryption technique. It includes features for encrypting and decrypting messages, as well as 
performing frequency analysis to aid in cryptanalysis.

## Features:
Encryption & Decryption: Encrypts and decrypts messages using the Vigenère cipher. Also supports handling of uppercase, lowercase, spaces, and special characters.
Frequency Analysis: Analyzes letter frequencies in the ciphertext to help determine assist in possibly breaking the cipher.

## How It Works:

Vigenère Cipher: The Vigenère cipher uses a key to shift each character in the plaintext by a certain number of positions in the alphabet. The key is repeated throughout the message, 
creating a series of shifts based on each letter in the key.
Frequency Analysis: Calculates the frequency of each letter in the ciphertext. Helps identify the most likely key length by analyzing letter distribution patterns.

## Limitations:
~ The implementation is not optimized for large texts or very long keys. 

~ It does not include advanced cryptanalysis methods like the Kasiski examination or Friedman test.

## Future Improvements
~ Add support for key estimation using Kasiski examination or the Friedman test.

~ Implement a more user-friendly interface, such as a web-based UI.


## Contact

Zach Shamieh
zachshamieh@gmail.com
