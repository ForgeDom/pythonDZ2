def filter_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            print(type(lines))
        filter_words = []

        for line in lines:
            words = line.split()
            for word  in words:
                if len(word) >= 7:
                    filter_words.append(word)

        with open(output_file, 'w') as file:
            file.write(', '.join(filter_words))
        print("Операція успішна!")
    except Exception as e:
        print(e)
filter_words('file.txt', 'new_file.txt')





