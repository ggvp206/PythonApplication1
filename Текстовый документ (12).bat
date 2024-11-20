import datetime
import time

class Task:
    def __init__(self, title, reminder_time):
        self.title = title
        self.reminder_time = reminder_time

def add_task(tasks, title, reminder_time):
    task = Task(title, reminder_time)
    tasks.append(task)

def check_reminders(tasks):
    current_time = datetime.datetime.now()
    for task in tasks:
        # Проверяем, нужно ли напомнить о задаче
        if task.reminder_time <= current_time:
            print(f'Напоминание: {task.title} было запланировано на {task.reminder_time}')
            tasks.remove(task)  # Удаляем задачу после напоминания

def main():
    tasks = []

    # Пример добавления задачи
    add_task(tasks, "Встреча с клиентом", datetime.datetime.now() + datetime.timedelta(seconds=10))

    while tasks:
        check_reminders(tasks)  # Проверяем напоминания
        time.sleep(5)  # Проверка каждые 5 секунд

if __name__ == "__main__":
    main()


import time


class Task:
    def init(self, name, due_date):
        self.name = name
        self.due_date = due_date


def __str__(self):
    return f"Задача: {self.name}, Срок: {self.due_date}"

class Calendar:
    def init(self):
        self.tasks = []


def add_task(self, task):
    self.tasks.append(task)
    print(f"Добавлена задача: {task}")

def check_reminders(self):
    now = datetime.datetime.now()
    for task in self.tasks:
        if task.due_date <= now:
            print(f"Напоминание: {task.name} просрочена!")

def main():
    calendar = Calendar()


# Пример добавления задач
task1 = Task("Отправить отчет", datetime.datetime(2023, 10, 20, 17, 0))
calendar.add_task(task1)

# Проверка напоминаний каждую минуту
while True:
    calendar.check_reminders()
    time.sleep(60)  # Ожидание 60 секунд

if name == "main":
    main()
