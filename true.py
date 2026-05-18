from customtkinter import *
import random

set_appearance_mode("dark")
set_default_color_theme("blue")

window = CTk()
window.title("Правда чи Дія")
window.geometry("500x400")

TRUTH_COLOR = "#3b8ed0"
ACTION_COLOR = "#e67e22"

FONT_BOLD = ("Arial", 32, "bold")
FONT_REGULAR = ("Arial", 16, "bold")

# Списки: правда
truth_tasks = [
    "Який вчинок тобі досі соромно згадувати?",
    "Яка в тебе найдивніша звичка?",
    "Що може миттєво тебе вибісити?",
    'Ти колись спеціально ігнорував людину?',
    'Що ти вважаєш своїм головним мінусом?',
    'Хто знає тебе найкраще?',
    'Який твій найдивніший страх?',
    'Який твій найсмішніший фейл?',
    'Який твій найнеочікуваніший талант?',
    'Яка твоя найбільш безглузда відмазка?',
    'Що тебе найбільше бісить у собі?',
    'Яка твоя найтупіша причина образитися?'
]

# Списки: дія
action_tasks = [
    "Скажи алфавіт дуже швидко",
    "Озвуч свої думки прямо зараз",
    "Прочитай будь-яке повідомлення максимально драматичним голосом",
    'Заспівай приспів будь-якої пісні',
    'Назви 5 речей на букву «К» за 10 секунд',
    'Вигадай собі нове ім’я на наступні 5 хвилин',
    'Скажи перше слово, яке прийде в голову.',
    'Назви 3 речі, які тебе дратують.',
    'Розкажи найсмішніший випадок за останній місяць.',
    'Назви 5 країн за 10 секунд.',
    'Закукурікай як півень',
    'Промурчи як кіт',
]

# Функція: випадкова правда
def show_true():
    task =  random.choice(truth_tasks)
    label_task.configure(text = task,text_color = TRUTH_COLOR)
    label_type.configure(text = 'ПРАВДА',text_color = TRUTH_COLOR,font = FONT_BOLD)


# Функція: випадкова дія
def show_action():
    task =  random.choice(action_tasks)
    label_task.configure(text = task,text_color = ACTION_COLOR)
    label_type.configure(text = 'ДЕЙСТВИЕ',text_color = ACTION_COLOR,font = FONT_BOLD)



# Заголовок
title_label = CTkLabel(window,text = 'Правда или Дейсвие',font= FONT_BOLD)
title_label.pack(pady = 25)

# Контейнер для завдання
task_frame = CTkFrame(window,width=450, height=150,corner_radius=15)
task_frame.pack_propagate(False)
task_frame.pack(pady = 10)


# Текст: тип завдання (Правда/Дія)
label_type = CTkLabel(task_frame,text = 'Вибери категорию',font= FONT_REGULAR)
label_type.pack(pady = (15,5))



# Текст самого завдання
label_task = CTkLabel(task_frame,
                      text = 'Твое задание',
                      font= ('Arial',18),
                      wraplength=400
                      )
label_task.pack(expand = True, padx = 20)



# Фрейм для кнопок
button_frame = CTkFrame(window,fg_color='transparent')
button_frame.pack(pady = 30)



# Ліва кнопка: правда (колір при наведенні #2980b9)
btn_true = CTkButton(button_frame,
                     text = 'Правда',
                     font=FONT_REGULAR,
                     width=160,
                     height=50,
                     fg_color=TRUTH_COLOR,
                     hover_color= '#2980b9',
                     command=show_true
                     )
btn_true.pack(side = 'left',padx = 10)



# Права кнопка: дія (колір при наведенні #d35400)
btn_action = CTkButton(button_frame,
                     text = 'Действие',
                     font=FONT_REGULAR,
                     width=160,
                     height=50,
                     fg_color=ACTION_COLOR,
                     hover_color= '#d35400',
                     command=show_action
                     )
btn_action.pack(side = 'left',padx = 10)



# Запуск
window.mainloop()