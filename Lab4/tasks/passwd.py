import random
from string import ascii_lowercase, ascii_uppercase


def generate_passwords(chars, length=12):
    if len(length)<1:
        raise ValueError("В пароле не может быть меньше 1 символа")
    while True:
        password = ''.join(random.choice(chars) for i in range(length))
        yield password

def main():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

    password_generator = generate_passwords(chars)

    for i in range(5):
        print(next(password_generator))

if __name__ == "__main__":
    main()