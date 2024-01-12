def decrypt(cipher_text, plain_text, cipher):
    fail = 0
    # check if both cipher_text and plain_text are of same length by converting to set and if the length is 26
    if len(set(cipher_text)) != len(set(plain_text)) or len(set(cipher_text)) != 26:
        print("Failed")
        return
    if fail != 1:
        # create a dictionary for mapping
        mapping = {}
        for i in range(len(cipher_text)):
            if cipher_text[i] not in mapping:
                mapping[cipher_text[i]] = plain_text[i]
            else:
                print("Failed")
                return

        # decrypt the cipher
        plain = ""
        for i in range(len(cipher)):
            plain += mapping[cipher[i]]

        print(plain)
    else:
        print("Failed")   
    
if __name__ == "__main__":
    cipher_text = input()
    plain_text = input()
    cipher = input()
    decrypt(cipher_text, plain_text, cipher)