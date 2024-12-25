#ENCRYPTION
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# #1. create a function encrypt() that takes original text and shift amount as inputs.
# def encrypt(original_text,shift_number):
# #2 inside the function shift original text and print the encrypted text
#     cipher_text = ""

#     for char in original_text:
#         initial_index = alphabet.index(char)
#         shifted_index = initial_index+shift_number
# #what happens when z is shifted by 9
#         shifted_index %= len(alphabet) #if not more than 25 returns the exact no., and if more than substracts itself out of 25 

#         cipher_text+=alphabet[shifted_index]


#     print(f"Here is the encoded result: {cipher_text}")
# #3 call the function
# encrypt(original_text=text, shift_number=shift)

# #DECRYPTION
# #1. create a function decrypt() that takes original text and shift amount as inputs.
# def decrypt(original_text,shift_number):
# #2 inside the function shift original text and print the encrypted text

#     output_text = ""

#     for char in original_text:
#         initial_index = alphabet.index(char)
#         shifted_index = initial_index-shift_number
#         shifted_index %= len(alphabet) 
#         output_text+=alphabet[shifted_index]

#     print(f"Here is the encoded result: {output_text}")

# decrypt(original_text=text, shift_number=shift)

#COMBINING BOTH DECODE AND ENCODE INTO A FUNCTION (FINAL PROJECT, REST ABOVE IS JUST FOR BUILDING CONCEPTS)

#****What if user enters spaces /numbers /symbols?
def caesar(original_text,shift_number,encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
                shift_number *= -1 #changes the shift number into negative indirecly substracting shift from initial index

    for char in original_text:

        if char not in alphabet:
            output_text+=char
        else:
                
            initial_index = alphabet.index(char)
            shifted_index = initial_index+shift_number
            shifted_index %= len(alphabet)
            output_text+=alphabet[shifted_index]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

#****figure a way to restart the cipher program?
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
