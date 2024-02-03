def count_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        line_count = len(lines)
        print(f"Кількість рядків у файлі: {line_count}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

count_file("file.txt")
