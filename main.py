import string
digit_quantity = 0
s = "маємо певний текст. реалізуйте! до нього наступну3 функціональність. з!мініть текст таким чином, що5б кожне речення починалася з великої !літери.підрахуйте кількість цифр у тексті. підрахуйте кількі6сть розділових знаків у те!ксті. підрахуйте кількість знаків оклику у тексті."
punctual = string.punctuation
punctual_quantity = 0
hailsign_quantity = s.count("!")
for i in s:
    if i.isdigit():
        digit_quantity += 1
    elif i in punctual:
        punctual_quantity += 1
print(f"{string.capwords(s, sep='. ')}\nQuantity of Digits:{digit_quantity}\nQuantity of punctuals:{punctual_quantity}\nQuantity of hail sign:{hailsign_quantity}")


a = input("Введіть речення")
word_count = len(a.split())
print(f"Кількість слів у рядку: {word_count}")


import string
import random
letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.digits
random_str = "".join(random.sample(letters, 8))
digit_sum = sum(int(char) for char in random_str if char.isdigit())
print(f"Рядок: {random_str}")
print(f"Сума цифр у рядку: {digit_sum}")


input_string = "багато    пробілів   між    словами"
space_count = sum(1 for char in input_string if char.isspace())
print(f"Рядок: {input_string}")
print(f"Кількість пробілів у рядку: {space_count}")

s = "In the hole in the ground there lived a hobbit"
l = s.find("h")
r = s.rfind("h")
result = ''
print(result + s[:l-1]+ s[r+1:] )


first = input("First sentence:")
second = input("Second sentence:")
third = input("Third sentence:")
result =''
for i,k,x in zip(first,second,third):
    result += i+k+x
print(result)







password = input("Введіть пароль: ")
if len(password) < 5:
    print("Пароль занадто короткий.")
else:
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    if not (upper and lower):
        print("Пароль має містити літери верхнього і нижнього регістрів.")
    digit = any(char.isdigit() for char in password)
    if not digit:
        print("Пароль має містити цифри.")
    symbol = any(char in "@#%&" for char in password)
    if not symbol:
        print("Пароль має містити символи @, #, % або &.")
    if upper and lower and digit and symbol:
        print("Пароль прийнятний.")