N = int(input("Введите количество слов: "))
words = []

for i in range(N):
    word = input("Введите слово: ")
    words.append(word)

result = " ".join(words)
print("Результат соединения слов:", result)