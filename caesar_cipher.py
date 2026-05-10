def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            # Check uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97

            # Encrypt character
            encrypted_char = chr(
                (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            )

            result += encrypted_char

        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher Tool ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' for Encrypt or 'd' for Decrypt: ").lower()

if choice == 'e':

    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == 'd':

    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")