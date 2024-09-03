'''
# Exercise 2: Generate a Password with Specific Character Types
# Write a Python program that generates a random password of a given length, 
ensuring it includes at least one uppercase letter, one lowercase letter, 
and one digit.
# Example input: length = 8
# Expected output: A random password of 8 characters, including at least 
one uppercase, one lowercase, and one digit, e.g., 'aB3xG2#1'
ASCII between 65 - 90     # Uppercase letter
ASCII between 97 - 122    # Lowercase letter
ASCII between 48 - 57     # Digit
'''
# Write and test your code here

# import random
# length = 8
# def generate_password(length):
#     if length < 3:
#         return "Password must be at least 3"
#     uppercase = chr(random.randint(65,90))
#     lowercase = chr(random.randint(97,122))
#     digit = chr(random.randint(48,57))
#     remainder = length - 3
#     password = [uppercase, lowercase, digit]
#     #password = uppercase + lowercase + digit
#     for i in range(remainder):
#         char_type = random.choice([1,2,3])
#         if char_type == 1:
#             password.append(chr(random.randint(65,90)))
#            # password = password + chr(random.randint(65,90))
#         elif char_type == 2:
#             password.append(chr(random.randint(97,122)))
#         elif char_type == 3:
#             password.append(chr(random.randint(48,57)))
#     return password
# password = ''.join(generate_password(length)) ### ''.join([list])
# print("Generated password: {}".format(password))

### ''.join([list]) is as good as you doing the code below
# output = ''
# for item in thislist:
#     output = output + item
def encrypt_letter(char,shift):
    offset = 32
    encrypt_ord = offset + (ord(char) - offset + shift) % 95
    encrypted_letter = chr(encrypt_ord)
    return encrypted_letter
print(encrypt_letter("z",20))
print(encrypt_letter("!",-5))

sentence = input("Enter something: ")
shift = -7
def encrypt_sentence(sentence, shift):
    encrypted_sentence = ""
    for char in sentence:
        encrypted_sentence += encrypt_letter(char,shift)
    return encrypted_sentence
encrypted_sentence =  encrypt_sentence(sentence, shift)
print("Encrypted sentence: ", encrypted_sentence)
# Whnlz'"v|'}pl~'pu'{opz'~pukv~'~vu.{'hwwlhy'pu'{ol'iyv~zly'opz{vy"'huk'{ol"'~vu.{'slh}l'v{oly'{yhjlz3'sprl'jvvrplz3'vu'{ol'jvtw|{ly'hm{ly'"v|'jsvzl'hss'vwlu'N|lz{'~pukv~z5'Hu"'mpslz'"v|'kv~usvhk'~pss'il'wylzly}lk3'ov~l}ly5
# cyper = 7