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
