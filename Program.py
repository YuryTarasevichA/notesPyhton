import json
from datetime import datetime


# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)


# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    print("Заметка успешно сохранена")


# Функция для редактирования существующей заметки
def edit_note():
    note_id = int(input("Введите идентификатор заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note['title'] = title
            note['body'] = body
            note['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным идентификатором не найдена")


# Функция для удаления существующей заметки
def delete_note():
    note_id = int(input("Введите идентификатор заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным идентификатором не найдена")


# Функция для вывода списка всех заметок
def list_notes():
    for note in notes:
        print(f"id заметки: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['body']}")
        print(f"Дата создания: {note['created_at']}")
        print()


# Основная часть программы

notes = load_notes()

while True:
    print("Выберите команду для выполнения: \n"
          "add - для добавления заметки\n"
          "edit - для редактирования заметки\n"
          "delete - для удаления заметки\n"
          "list - для показа всех существующих заметок\n"
          "save - для сохранения новых заметок\n"
          "exit - для выхода из приложения заметок\n")
    command = inputcommand = input("Введите команду: ")

    if command == "add":
        add_note()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "list":
        list_notes()
    elif command == "save":
        save_notes(notes)
        print("Заметки успешно сохранены")
    elif command == "exit":
        break
    else:
        print("Неверная команда")

print("Программа завершена")
