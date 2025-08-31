def encrypt(original_text, shift_amount, change):
    storing = ''
    for ch in original_text:
        ch_value = ord(ch)
        if change in ["addition", "add"]:
            if 'a' <= ch <= 'z':
                storing += chr((ch_value - 97 + shift_amount) % 26 + 97)
            elif 'A' <= ch <= 'Z':
                storing += chr((ch_value - 65 + shift_amount) % 26 + 65)
            else:
                storing += ch
        elif change in ["subtraction", "sub"]:
            if 'a' <= ch <= 'z':
                storing += chr((ch_value - 97 - shift_amount) % 26 + 97)
            elif 'A' <= ch <= 'Z':
                storing += chr((ch_value - 65 - shift_amount) % 26 + 65)
            else:
                storing += ch
        else:
            storing += ch
    return storing


def decrypt(original_text, shift_amount, change):
    storing = ''
    for ch in original_text:
        ch_value = ord(ch)
        if change in ["addition", "add"]:
            if 'a' <= ch <= 'z':
                storing += chr((ch_value - 97 - shift_amount) % 26 + 97)
            elif 'A' <= ch <= 'Z':
                storing += chr((ch_value - 65 - shift_amount) % 26 + 65)
            else:
                storing += ch
        elif change in ["subtraction", "sub"]:
            if 'a' <= ch <= 'z':
                storing += chr((ch_value - 97 + shift_amount) % 26 + 97)
            elif 'A' <= ch <= 'Z':
                storing += chr((ch_value - 65 + shift_amount) % 26 + 65)
            else:
                storing += ch
        else:
            storing += ch
    return storing


# Main loop
while True:
    text = input("Enter the Message: ")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    change = input("How would you like to encode your text — by Addition or Subtraction? ").lower()
    shift = int(input("By how much would you like to shift? "))

    if direction == "encode":
        result = encrypt(text, shift, change)
        print("Encrypted Text:", result)
    elif direction == "decode":
        result = decrypt(text, shift, change)
        print("Decrypted Text:", result)
    else:
        print("Invalid choice!")

    again = input("Type 'yes' to continue, or 'exit' to quit: ").lower()
    if again == "exit":
        print("Goodbye 👋")
        break
