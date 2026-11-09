import csv
# синхронная работа с csv файлами

data = [
    ["product", "price", "stock"],
    ["Клавиатура", 45.5, 10],
    ["Мышь", 20.0, 25],
    ["Монитор", 250.0, 5]
]
with open('csv1.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f) # создаем помощника, который будет записывать в наш файл
    writer.writerows(data) # передаем помощнику список, который надо написать
with open('csv1.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)  # создаем помощника, который будет читать файл
    for row in reader: # читаем файл построчно, чтобы не нагружать оперативную память
        print(row)