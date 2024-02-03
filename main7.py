def write_file(array, output_file):
    try:
        with open(output_file, 'w') as file:
            for item in array:
                file.write(str(item) + '\n')

        print(f"Масив записано у файл")
    except Exception as e:
        print(f"Виникла помилка: {e}")
my_array = ["A", "B", "C"]
write_file(my_array, 'file.txt')
