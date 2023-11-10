### PASSWORD GENERATOR
import string
import random

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special = string.punctuation
all = string.printable

while True:
    n_characters = int(
        input("How long password do you want to generate? Minimum 8. Answer: ")
    )
    if n_characters < 8:
        print("Password too short!")
    else:
        password = []
        password.append(random.sample(uppercase, 2))
        password.append(random.sample(lowercase, 2))
        password.append(random.sample(numbers, 2))
        password.append(random.sample(special, 2))

        n_left = n_characters - 8
        for i in range(n_left):
            password.append(random.sample(all, 1))

        output = []

        for i in range(len(password)):
            for y in password[i]:
                output += y

        output = "".join(output)
        print(output)
        break
