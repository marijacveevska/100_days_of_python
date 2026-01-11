# Step 1
# TODO-1 - Create a function called encrypt() that takes original_text and shift_amount as 2 inputs
# TODO-2 - inside the encrypt function shift each letter of the original_text forewards in the alphabet by shift_amount and print encrypted text. You can use the built in function index() to find the position of an item in a list. 
#          The output should be: "Here is the encoded result: "
# TODO-3 - What happens if you call z and shift it by 9 ? can you fix this so that the alphabet starts from 0 again - By using the modulo operator you can normalize and calculate the remaining letters outside of our slphabet indexes (0-25)
# TODO-4 - Call the encrypt() function and pass in the inputs
# TODO-5 - Now inplement decrypt() with a similar logic
# TODO-6 - Enable the game to restart


def encrypt(original_text, shift_amount):
    
    origin_text = original_text.lower()

    origin_text_no_space = origin_text.replace(" ","")

    new_word = ""
    for elem in origin_text_no_space:
        new_index = alphabet.index(elem) + int(shift_amount)
        new_index %= len(alphabet)
        new_letter = alphabet[new_index]
        new_word+=new_letter

    print("Here is the encoded result: "+ new_word)


def decrypt(encrypted_text, shift_amount):
    
    encrpt_text = encrypted_text.lower()

    original_word = ""
    for elem in encrpt_text:
        new_index = alphabet.index(elem) - int(shift_amount)
        new_index %= len(alphabet)

        new_letter = alphabet[new_index]
        original_word+=new_letter

    print("Here is the decoded result: "+ original_word)


should_restart = True

while should_restart:
    direction = input("Type 'encode' if you want to encrypt your message or type 'decode' to decrypt a message: \n").lower()

    Q1 = input("What is your message? ")
    Q2 = input("What is your desired shift amount? ")

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if direction == "encode":
        encrypt(Q1, Q2)
    elif direction == "decode":
        decrypt(Q1, Q2)
    else:
        print("Invaild input")

    
    Q0 = input("Do you want to go again? 'yes' or 'no'? ").lower()
    if Q0 != "yes":
        should_restart = False
        print("Bye-Bye!")
