def count(filename):
    try:
        with open(filename, 'r') as file:
            info = file.read()
        character_count = len(info)

        print(f"Кількість символів у файлі: {character_count}")
    except Exception as e:
        print(f"Виникла помилка: {e}")
count("file.txt")
