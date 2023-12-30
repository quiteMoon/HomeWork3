import random

# Task 1

# str1 = str(input("Enter your palindrom text: "))

# str = str1.lower()
# str2 = str.replace(" ", "")
# print(str2)
# if str2 == str2[::-1]: print("Its palindrom")
# else: print("Its not palindrom")

# Task 2

# text = str(input("Введіть текст: "))
# reserved_words = str(input("Введіть список зарезервованих слів через кому без пробілів: ")).split(',')
# for word in text.split():
#     if word.lower() in reserved_words:
#         text = text.replace(word, word.upper())
# print(text)

# Task 3

# text = str(input("Enter text: ")).split(".")
# if text[-1] == "": del(text[-1])
# print(f"Sentence in your text = {len(text)}")

# Task 4

# print(eval(input("Enter your mathematical expression: ")))

# Task 5

# zero = 0
# positive = 0
# negative = 0

# randomlist = [random.randint(-100, 100) for i in range(100)]
# for i in range(100):
#     if randomlist[i] == 0: zero += 1
#     elif randomlist[i] > 0: positive += 1
#     elif randomlist[i] < 0: negative += 1
# print(f"Max = {max(randomlist)}, Min = {min(randomlist)}")
# print(f"Positive = {positive}, Negative = {negative}, Zero = {zero}")