def sorted_alphabetically():
    return sorted(lines)

def sorted_by_length():
    return sorted(lines, key = len)

def sorted_reverse():
    return sorted(lines, reverse = True)

while True:
    try:
        n = int(input("Введите количество строк: "))
        if n <= 0:
            print("Ошибка: количество строк должно быть положительным числом!")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число!")

lines = []
print("Введите строки: ")
for i in range(n):
    line = input(f"Строка {i+1}: ").lower()
    lines.append(line)

with open("resource/words.txt", "w") as file:
    for i in lines:
        file.write(i + "\n")

with open("resource/words.txt", "r") as file:
    print("\n=== Содержимое words.txt ===")
    for line in file:
        print(line, end="")

with open("resource/sorted_alphabetically.txt", "w") as file:
    for i in sorted_alphabetically():
        file.write(i + "\n")

with open("resource/sorted_alphabetically.txt", "r") as file:
    print("\n=== Содержимое sorted_alphabetically.txt ===")
    for line in file:
        print(line, end="")

with open("resource/sorted_by_length.txt", "w") as file:
    for i in sorted_by_length():
        file.write(i + "\n")

with open("resource/sorted_by_length.txt", "r") as file:
    print("\n=== Содержимое sorted_by_length.txt ===")
    for line in file:
        print(line, end="")

with open("resource/sorted_reverse.txt", "w") as file:
    for i in sorted_reverse():
        file.write(i + "\n")

with open("resource/sorted_reverse.txt", "r") as file:
    print("\n=== Содержимое sorted_reverse.txt ===")
    for line in file:
        print(line, end="")