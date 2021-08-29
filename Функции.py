documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}



def people():
    number = input('Введите номер документа\n')
    for elem in documents:
        if number in elem.values():
            print(elem.get('name'))





def sheld():
    number = input('Введите номер документа\n')
    for elem in directories:
        print(elem)
        if number in directories.get(elem):
            print(f'Документ находится на полке: {elem}')

        else:
            print(f'Не правильно указан номер документа')
            break




def list():
    for elem in documents:
        type = elem.get('type')
        number = elem.get('number')
        name = elem.get('name')
        print(f'{type} {number} {name}')



def add():
    new_type = input('Введите тип документа\n')
    new_number = input('Введите номер документа\n')
    new_name = input('Введите имя владельца\n')
    number_directories = input('Введите номер полки\n')

    new_directories = {}
    new_directories['type'] = new_type
    new_directories['number'] = new_number
    new_directories['name'] = new_name
    documents.append(new_directories)
    print(documents)
    if number_directories in directories:
        directories[number_directories].append(new_number)
        print(directories)
    else:
        print('Ошибка')




def delete():
    delete = input('введите номер документа\n')
    for elem in documents:
        if delete in elem.values():
            del elem['type']
            del elem['number']
            del elem['name']
            del documents[1]
            for elem in directories.values():
                if delete in elem:
                    elem.remove(delete)
                    print(f'Документ с номером {delete}, был удален из документов и полок')
                    return




        print('Ошибка ввода')
        return



def move():
    number = input('Укажите номер документа\n')
    new_directories = input('На какую полку перенести документ?\n')
    for elem in directories.values():
        if number in elem:
            elem.remove(number)



            for elem in directories:
                if elem == new_directories:
                     directories[new_directories].append(number)
                     print(f'Документ был перемещен на полку {new_directories}')
                     return

        print('Не найден документ или полка')
        return


def add_sheld():
    new_sheld = input('Укажите новый номер полки\n')
    if new_sheld not in directories:
        directories[new_sheld] = []
        print(directories)
    else:
        print('Такая полка уже существует')






def start():
    ask = input('Вы хотите начать работать? Нажмите Y/N\n')
    if ask == 'Y':
        p = input('Нажмите \'p\', что бы вывести имя человека\n'
                  'Нажмите\'s\', что бы вывести номер полки\n'
                  'Нажмите \'l\' что бы вывести весь список документов\n '
                  'Нажмите \'a\' что бы добавить новый документ\n'
                  'Нажмите \'d\' что бы добавить новый документ\n'
                  'Нажмите \'m\' что бы переместить документ на другую полку\n'
                  'Нажмите \'as\' что бы добавить новую полку в переччень\n')
        if p == 'p':
            people()
        elif p == 's':
            sheld()
        elif p == 'l':
            list()
        elif p == 'a':
            add()
        elif p == 'd':
            delete()
        elif p == 'm':
            move()
        elif p == 'as':
            add()
    elif ask == 'n':
        print('Выход из программы')
        return




start()





















































