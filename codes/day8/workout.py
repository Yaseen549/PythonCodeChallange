
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



def caesar(encryption_direction, text_to_encrypt, shift_number):
    text_to_encode_or_decode = ""
    if encryption_direction == "decode":
        shift_number *= -1
    for char in text_to_encrypt:
        position = alphabet.index(char)
        new_position = position + shift_number
        text_to_encode_or_decode += alphabet[new_position]
    print(f"Your {encryption_direction}d message is {text_to_encode_or_decode}")



should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    caesar(encryption_direction = direction, text_to_encrypt = text, shift_number = shift)
    user_input = input("Type 'yes' to continue, 'no' to exit.")
    if user_input == "no":
        should_continue = False
        print("Goodbye.")


# encode(encryption_direction = direction, text_to_encrypt = text, shift_number = shift)
# decode(encryption_direction = direction, text_to_decrypt = text, shift_number = shift)
