def decrypt(cipher, plain_text, prompt):
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
    if len(set(cipher)) != len(set(plain_text)):
        return('Failed')
    if len(set(cipher)) < 26 or len(set(plain_text)) < 26:
        return('Failed')
    
    # Create a dictionary for mapping characters from cipher_text to plain_text
    mapping = {}

    # Populate the mapping dictionary
    for cipher_char, plain_char in zip(cipher, plain_text):
        if cipher_char in mapping:
            if mapping[cipher_char] != plain_char:
                return('Failed')
        else:
            mapping[cipher_char] = plain_char

        

    # Decrypt the cipher using the created mapping
    decrypted_text = "".join(mapping[char] for char in prompt)

    # Print the decrypted text
    return decrypted_text

if __name__ == "__main__":
    # Input encrypted text, corresponding decrypted text, and the text to be decrypted
    cipher = input()
    plain_text = input()
    prompt = input()

    # Call the decrypt function with the provided inputs
    print(decrypt(cipher, plain_text, prompt))
