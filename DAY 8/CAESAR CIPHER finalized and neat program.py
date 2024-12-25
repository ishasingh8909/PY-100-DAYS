import caesar_cipher_art
print(caesar_cipher_art.caesar_logo)

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_number,encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_number *= -1 
                
    for char in original_text:

        if char not in alphabet:
            output_text+=char
        else:
                
            initial_index = alphabet.index(char)
            shifted_index = initial_index+shift_number
            shifted_index %= len(alphabet)
            output_text+=alphabet[shifted_index]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue=True

while should_continue:

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type you message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_number=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue == False
        print("Goodbye")
