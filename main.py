import random
import string

val = input("Website: ")

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(12))

with open("passwords.txt", "a") as file:
    file.write(f"{val}: {password}\n")

print(f"Password for {val} is: {password}")
print("Password saved to passwords.txt")