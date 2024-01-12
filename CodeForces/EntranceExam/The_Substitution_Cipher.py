def decrypt(cipher_text, plain_text, cipher):
    """
    Decrypt a given cipher text using a provided mapping.

    Args:
    - cipher_text (str): Encrypted text.
    - plain_text (str): Corresponding decrypted text.
    - cipher (str): Text to be decrypted.

    Returns:
    - None: Prints the decrypted text or "Failed" if decryption fails.
    """

    # Check if both cipher_text and plain_text have the same length and contain all 26 unique characters
    if len(set(cipher_text)) != len(set(plain_text)) or len(set(cipher_text)) != 26:
        print("Failed")
        return

    # Create a dictionary for mapping characters from cipher_text to plain_text
    mapping = {}

    # Populate the mapping dictionary
    for cipher_char, plain_char in zip(cipher_text, plain_text):
        if cipher_char not in mapping:
            mapping[cipher_char] = plain_char
        else:
            print("Failed")
            return

    # Decrypt the cipher using the created mapping
    decrypted_text = "".join(mapping[char] for char in cipher)

    # Print the decrypted text
    print(decrypted_text)

if __name__ == "__main__":
    # Input encrypted text, corresponding decrypted text, and the text to be decrypted
    cipher_text = input()
    plain_text = input()
    cipher = input()

    # Call the decrypt function with the provided inputs
    decrypt(cipher_text, plain_text, cipher)
