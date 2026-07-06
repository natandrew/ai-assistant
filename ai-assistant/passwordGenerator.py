import random
import string


def pw():
    pwd = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd_char = random.choices(characters, k=8)

    for ch in pwd_char:
        pwd += ch

    print("\n" + pwd, end="\n\n")
