import Ceaser_logo

print(Ceaser_logo.logo)

while True:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % 26
                end_text += alphabet[new_position]
            else:
                end_text += letter

        print(f"Here is {direction} result: {end_text}")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    game = input("If you want to Restart please 'yes' or 'no' for End.")
    if game == "no":
        print("See you soon!!! Goodbye.")
        break
    else:
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
