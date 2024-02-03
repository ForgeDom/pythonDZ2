def stars(input_file, output_file):
    try:
        with open(input_file, 'r') as input_file:
            lines = input_file.readlines()
            last_index = None
            for i in range(len(lines) - 1, -1, -1):
                if ',' not in lines[i]:
                    last_index = i
                    break
            stars = '************\n'
            if last_index is not None:
                lines.insert(last_index + 1, stars)
            else:
                lines.append(stars)
        with open(output_file, 'w') as output_file:
            output_file.writelines(lines)

        print("Операція успішна!")
    except Exception as e:
        print(f"Виникла помилка: {e}")

stars('file.txt', 'new_file.txt')
