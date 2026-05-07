def encryption():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    shift = 3
    for i in line:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += i
    return result

def decryption():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    shift = 3

    with open("resource/encrypted.txt", "r") as file:
        encrypted_text = file.read()

    for i in line:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index - shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += i
    return result

line = input("Введите строку: ").lower()

with open("resource/secret.txt", "w") as file:
    for i in line:
        file.write(i)

with open("resource/secret.txt", "r") as file:
    print("=== Содержимое secret.txt ===")
    for line in file:
        print(line)

with open("resource/encrypted.txt", "w") as file:
    for i in encryption():
        file.write(i)

with open("resource/encrypted.txt", "r") as file:
    print("\n=== Содержимое encrypted.txt ===")
    for line in file:
        print(line)

with open("resource/decrypted.txt", "w") as file:
    for i in decryption():
        file.write(i)

with open("resource/decrypted.txt", "r") as file:
    print("\n=== Содержимое decrypted.txt ===")
    for line in file:
        print(line)