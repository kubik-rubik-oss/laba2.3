def count_lines(filename):
    count = 0
    with open(filename) as file:
        for i in file:
            count += 1
    return count

def count_words(filename):
    count = 0
    with open(filename) as file:
        for i in file:
            words = line.split()
            count += len(words)
    return count

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
print("Введите строки:")
for i in range(n):
    line = input(f"Строка {i+1}: ")
    lines.append(line)

with open("resource/input.txt", "w") as file:
    for i in lines:
        file.write(i + "\n")

with open("resource/input.txt", "r") as file:
    print("Файл input.txt записан. Содержимое файла:")
    for line in file:
        print(line, end="")

with open("resource/statistics.txt", "w") as file:
    file.write(f"Количество строк в файле: {count_lines('resource/input.txt')}\n")
    file.write(f"Количество слов в файле: {count_words('resource/input.txt')}")