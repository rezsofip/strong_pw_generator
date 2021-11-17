import random

# asking for user input on character length
length = int(input("Enter a password length [8-15] "))
while length not in range(8, 16):
    length = int(input("The length is not valid. Enter a password length [8-15] "))

# store all the special characters in a tuple
spec_chars = tuple(chr(i) for i in range(128) if i in range(33, 48) or i in range(58, 65) or i in range(91, 97))
# print(spec_chars)
# print(len(spec_chars))

# this is where I store the generated characters
generated_chars = []

# first I generate 1 lowercase letter, 1 uppercase letter, and 1 special character
generated_chars.append(chr(random.randint(97, 122)))
generated_chars.append(chr(random.randint(65, 90)))
generated_chars.append(spec_chars[random.randint(0, len(spec_chars)-1)])
# then I add the other characters which can be all of the 3 categories
for i in range(3, length):
    generated_char = []
    generated_char.append(chr(random.randint(97, 122)))
    generated_char.append(chr(random.randint(65, 90)))
    generated_char.append(spec_chars[random.randint(0, len(spec_chars) - 1)])
    generated_chars.append(generated_char[random.randint(0, 2)])
# I shuffle the characters to be more randomized
for i in range(1, 4):
    random.shuffle(generated_chars)
print("Your generated strong password is: " + "".join(generated_chars))
