data_1 = ["1", "2", "3"]
data_2 = ["a", "b", "c"]
data_3 = ["!", "?", "#"]

with open("resource/file1.txt", "w") as file:
    for i in data_1:
        file.write(i)

with open("resource/file1.txt", "r") as file:
    print("=== Содержимое file1.txt ===")
    for line in file:
        print(line)

with open("resource/file2.txt", "w") as file:
    for i in data_2:
        file.write(i)

with open("resource/file2.txt", "r") as file:
    print("\n=== Содержимое file2.txt ===")
    for line in file:
        print(line)

with open("resource/file3.txt", "w") as file:
    for i in data_3:
        file.write(i)

with open("resource/file3.txt", "r") as file:
    print("\n=== Содержимое file3.txt ===")
    for line in file:
        print(line)

with open('resource/combined.txt', 'w') as outfile:
    for f in ['file1.txt', 'file2.txt', 'file3.txt']:
        with open(f, 'r') as infile:
            outfile.write(infile.read())

with open("resource/combined.txt", "r") as outfile:
    print("\n=== Содержимое combined.txt ===")
    for line in outfile:
        print(line)