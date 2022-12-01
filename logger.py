
from model import get_info as info

def read_contact():
    with open('Phonebook.csv', 'r', encoding='utf=8') as f:
        return f.read()

def writing_scv (info):
    file = 'phonebook.csv'
    with open (file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}; Имя: {info[1]}; Номер телефона: {info[2]}; Номер телефона: {info[3]}\n')

def writing_txt (info):
    file = 'phonebook.txt'
    with open (file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nНомер телефона: {info[3]}\n\n')