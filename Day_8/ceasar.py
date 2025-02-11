import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index + shift
        new_index %= len(alphabet)
        encrypted_text += alphabet[new_index]
    print(encrypted_text)

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index - shift
        if new_index < 0:
            new_index = -1 * (abs(new_index) % len(alphabet))
        decrypted_text += alphabet[new_index]
    print(decrypted_text)

def cesar(direction, text, shift):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Wrong choice")

retry = True
while retry:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = ""
    while not text.isalpha():
        text = input("Type your message:\n").lower()
        if not text.isalpha():
            print("Type only letters")
    shift = int(input("Type the shift number:\n"))
    cesar(direction, text, shift)
    another_go = ""
    while not ( another_go == "yes" or another_go == "no"):
        another_go = input("Do you want another go?(yes/no)").lower()
        if another_go == "no":
            print("Bye!")
            retry = False
