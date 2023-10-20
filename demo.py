def encrypt(data, key):
    ######################################
    ## NEVER USE CAESAR OUTSIDE OF DEMO ##
    ######################################
    return caesar_cipher(data, key, mode='encrypt')

def decrypt(data, key):
    ######################################
    ## NEVER USE CAESAR OUTSIDE OF DEMO ##
    ######################################
    return caesar_cipher(data, key, mode='encrypt')

# ML func
# ceasar cipher ONLY FOR DEMO for demo
def caesar_cipher(text, shift, mode='encrypt'):
    ######################################
    ## NEVER USE CAESAR OUTSIDE OF DEMO ##
    ######################################
    result = ""
    for char in text:
        if char.isalpha():
            is_uppercase = char.isupper()
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if is_uppercase else chr((ord(char) - 97 + shift) % 26 + 97)
            if mode == 'decrypt':
                shift = -shift  # For decryption, shift in the opposite direction
            result += shifted_char
        else:
            result += char
    return result

# Example usage
text = "Hello, World!"
shift = 3
encrypted_text = encrypt(text, shift, mode='encrypt')
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift, mode='decrypt')
print("Decrypted text:", decrypted_text)
