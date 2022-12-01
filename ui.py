from model import get_info
from logger import writing_scv, read_contact, writing_txt

def click():
    print('1. Добавить новую запись\n2. Вывести телефонный справочник')
    mode = int(input())
    if mode == 1:
        a = get_info()
        writing_txt(a)
        writing_scv(a)

    elif mode == 2:
        print(read_contact())

    else:
        print('неверная запись')
