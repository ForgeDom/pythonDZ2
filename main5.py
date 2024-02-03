user_input = input("Введіть символ")
count = 0
with open ("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith(user_input):
            count +=1
print(count)

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



def copy_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        with open(output_file, 'w') as file:
            file.writelines(lines[::-1])
        print("Операція успішна!")
    except Exception as e:
        print(e)

copy_file('file.txt', 'new_file.txt')



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




with open("file.txt","r") as f:
    lines = f.readlines()
with open("new_file.txt","a") as f:
    for line in lines:
        for i in line:
            if i == "*":
                f.write(i.replace("*","&"))
            elif i == "&":
                f.write(i.replace("&","*"))
            else:
                f.write(i)



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



def count(filename):
    try:
        with open(filename, 'r') as file:
            info = file.read()
        character_count = len(info)

        print(f"Кількість символів у файлі: {character_count}")
    except Exception as e:
        print(f"Виникла помилка: {e}")
count("file.txt")



def count_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        line_count = len(lines)
        print(f"Кількість рядків у файлі: {line_count}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

count_file("file.txt")
