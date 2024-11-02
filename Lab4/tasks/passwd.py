import random
from string import ascii_lowercase, ascii_uppercase

def generate_passwords(chars, length=12):
    if length<1:
        raise ValueError("Такой пароль не может быть")
    while True:
        password = ''.join(random.choice(chars) for i in range(length))
        yield password

def main():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    try:
        password_generator = generate_passwords(chars,10)

        for i in range(5):
            print(next(password_generator))
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()