alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print(len(alphabet))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    plaintext_list = [char for char in text]
    ciphertext = ""
   
    for x in plaintext_list:
        if x in alphabet:   
            print(alphabet.index(x))
            idx = (alphabet.index(x) + shift) % len(alphabet) 
            ciphertext+=alphabet[idx]
        else:
            ciphertext+=x

    return ciphertext

def decrypt(cipher, shift):
    cipher_list = [char for char in cipher]
    plaintext = ""

    for x in cipher_list:
        if x in alphabet:   
            idx = alphabet.index(x) - shift % len(alphabet)
            plaintext+=alphabet[idx]
        else:
            plaintext+=x

    return plaintext
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == 'encode':
    print(encrypt(text, shift))
elif direction == 'decode':
    print(decrypt(text, shift))

print(print(decrypt(encrypt(text, shift), shift)))