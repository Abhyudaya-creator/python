# def greet():
#     print("Hello, World!")
#     print("Welcome to the program.")

# greet()

# def greetwithname(name, location):
#     print(f"hello {name}")
#     print(f"welcome to {location}")

# greetwithname(location="Ayodhya", name="Abhi")


#love calculator

# def calculate_love_score(name1, name2):
#     combinednames = (name1 + name2).lower()

#     true_score = (
#         combinednames.count("t") +
#         combinednames.count("r") +
#         combinednames.count("u") +
#         combinednames.count("e")
#     )

#     love_score = (
#         combinednames.count("l") +
#         combinednames.count("o") +
#         combinednames.count("v") +
#         combinednames.count("e")
#     )

#     score = int(str(true_score) + str(love_score))
#     print(score)


#caesar CIPHER


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""



    for letter in original_text:
       shifted_position = alphabet.index(letter) + shift_amount

       shifted_position = shifted_position % len(alphabet)
       cipher_text += alphabet[shifted_position]



    print(f"The encoded text is {cipher_text}")


encrypt(original_text=text, shift_amount=shift)
    





    









