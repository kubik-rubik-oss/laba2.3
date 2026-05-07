def found_word(filename):
    search_word = input("\nВведите слово для поиска: ")
    found = False
    total_count = 0

    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            line_lower = line.lower()
            word_lower = search_word.lower()
            count_in_line = line_lower.count(word_lower)

            if count_in_line > 0:
                print(f"Слово '{search_word}' найдено в строке {line_num}: {line.strip()}")
                print(f"Вхождений в строке: {count_in_line}")
                found = True
                total_count += count_in_line

    if found:
        print(f"\nВсего найдено вхождений слова '{search_word}': {total_count}")
    else:
        print(f"Слово не найдено")

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

with open("resource/text.txt", "w") as file:
    for i in lines:
        file.write(i + "\n")

with open("resource/text.txt", "r") as file:
    print("Файл input.txt записан. Содержимое файла:")
    for line in file:
        print(line, end="")

found_word("resource/text.txt")