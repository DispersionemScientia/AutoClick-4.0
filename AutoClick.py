import time
from tkinter import *
import pyautogui as pag
import keyboard


# механика кликера
class Clicker:
    def __init__(self):
        self.pag_pause = 0.1

    def change_speed(self, speed):
        self.pag_pause = speed
        self.update_speed()

    def custom_speed(self, speed):
        try:
            speed = float(speed)
            self.pag_pause = speed
            self.update_speed()
        except:
            pass

    def update_speed(self):
        pag.PAUSE = float(self.pag_pause)

    @staticmethod
    def click(starting: str, stopping: str):
        try:
            while True:
                if keyboard.is_pressed(starting):
                    break
            while True:
                pag.click()
                if keyboard.is_pressed(stopping):
                    break
        except:
            pass

    @staticmethod
    def help_me():
        helpFrame = Frame(root, bg=color_bg)
        helpText = Label(helpFrame, text='Справочник:\n'
                                         'вначале, нужно назначить\n'
                                         ' старт и стоп клавишами,\n'
                                         'далее можете запускать.\n'
                                         'Всё просто,\n так-же '
                                         'советую\n'
                                         ' поизменять скорости,\n'
                                         'вы можете назначить\n'
                                         'кастомную(свою) скорость\n'
                                         '(пример 0.1 - минимальная\n'
                                         'или 0.00001 - абсолютная\n'
                                         '(я так сделал, и оно работает)\n'  # говорят 66 - плохое число
                                         'не советую ставить 0 секунд).\n'
                                         'Нажмите кстати на букву "K"\n'
                                         'окно откалибруется, и станет\n'
                                         'видимым на панели приложений',
                         fg=color_text, bg=color_bg, font=('', 8, ''))

        helpFrame.place(x=0, y=160, width=220, height=240)
        helpText.place(x=0, y=5, width=200, height=240)

    @staticmethod
    def unfocus_button(button):
        button.configure(bg=color_button_active)

    @staticmethod
    def on_press_window(event):
        global x, y
        x = event.x
        y = event.y

    @staticmethod
    def on_drag_window(event):
        deltax = event.x - x
        deltay = event.y - y
        x0 = root.winfo_x() + deltax
        y0 = root.winfo_y() + deltay
        root.geometry(f"+{x0}+{y0}")

    @staticmethod
    def protokol_IISUS():
        global root

        for i in range(10, 0, -1):
            root.attributes('-alpha', i/10)
            time.sleep(0.1)
            if i == 0:
                break

        for i in range(0, 11, 1):
            time.sleep(0.1)
            root.attributes('-alpha', i/10)

        calibrovka = Toplevel(root)
        calibrovka.overrideredirect(1)
        Button(calibrovka, text='Нажмите для калибровки', bg=color_button, fg=color_text, font=('', 20, 'bold'),
               activebackground=color_bg, activeforeground=color_text, highlightthickness=10,
               command=lambda: calibrovka.destroy()).pack()
        calibrovka.geometry(f'+{int(screen_width/2-200)}+{int(screen_height/2-100)}')
        calibrovka.attributes('-topmost', True)
        calibrovka.resizable(False, False)

        calibrovka.mainloop()


    @staticmethod
    def custom():
        CustomSpeedText = Label(frame_speed, text='Введите\n скорость:\n'
                                                  '    (в секундах)',
                                font=('', 8, ''), bg=color_bg, fg=color_text)

        speed = StringVar()
        CustomSpeedText.place(x=0, y=200, width=85, height=40)

        Entry(frame_speed, textvariable=speed).place(x=5, y=240, width=80, height=20)

        CustomSpeedButton = Button(frame_speed, text='Кастомная', bg=color_button, fg=color_text,
                                   activebackground=color_button_active, activeforeground=color_text, bd=1,
                                   cursor=button_cursor,
                                   font=('', 8, ''), command=lambda: clicker.custom_speed(speed=speed.get()))
        CustomSpeedButton.place(x=5, y=270, width=80, height=40)


clicker = Clicker()  # кликер

# переменные с настройками
color_bg = '#222222'
titr_bg = '#333333'

color_text = 'white'
color_button = '#777777'
color_direct = '#151719'
color_direct_text = '#F5FFFA'
color_button_active = '#888888'

button_cursor = 'hand2'

width = 400
height = 450

screen_width, screen_height = pag.size()

# Создание рута, главное потом снова не потерять
root = Tk()

# настройки
root.title('Кликер')
root.config(bg=color_bg)
root.geometry(f'{width}x{height}+100+100')
root.overrideredirect(1)

root.wait_visibility(root)


root.resizable(width=False, height=False)


# Иконку ставим
root.iconphoto(False, PhotoImage(file='Image/Icon.png'))


# директ (меню сверху, где крестик короче)
direct = Frame(width=width, height=20, bg=color_direct)

btnExit = Button(text='X', font=('', 12, 'bold'), bg=color_direct, fg=color_text,
                 bd=0, activebackground=color_direct, activeforeground=color_text,
                 command=lambda: root.destroy())

tittle_Text = Label(direct, text='Кликер', bg=color_direct, bd=0, font=('Arial', 11, 'bold'), fg=color_direct_text)

direct.place(x=0, y=0)  # всё размещаем
btnExit.place(x=width - 40, y=3, width=30, height=16)
tittle_Text.place(x=0, y=0, width=60, height=20)


direct.bind('<Button-1>', clicker.on_press_window)  # это для передвижения окна
direct.bind('<B1-Motion>', clicker.on_drag_window)

# логотип
logo = Canvas(root, width=65, height=65, bg=color_bg, bd=0, highlightthickness=0)
logo.place(x=140, y=70)

logo.create_oval(10, 10, 60, 60, fill=color_bg, outline='red', width=3)  # круг, в которой будет буква K

logo.create_line(30, 6, 20, 62, fill='red', width=3)  # буква K
logo.create_line(27, 35, 50, 10, fill='red', width=3)
logo.create_line(27, 35, 50, 60, fill='red', width=3)

logo.bind('<Button-1>', lambda x=10: clicker.protokol_IISUS())

# данные о старт и стоп
start = StringVar()
StartText = Label(text='Старт:', bg=color_bg, fg=color_text)  # создаю текст
StartText.place(x=5, y=70, width=50, height=25)  # отображаю текст
Entry(textvariable=start).place(x=55, y=70, width=40, height=25)  # ввод

stop = StringVar()
StopText = Label(text='Стоп:', bg=color_bg, fg=color_text)
StopText.place(x=5, y=120, width=50, height=25)
Entry(textvariable=stop).place(x=55, y=120, width=40, height=25)

# кнопки
btnStart = Button(text='Запуск', font=('Arial', 14, 'bold'), bg=color_button, fg=color_text,
                  activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                  command=lambda: clicker.click(starting=start.get(), stopping=stop.get()))
btnStart.place(x=10, y=23, width=300, height=40)

btnHelp = Button(text='Справка', bg=color_button, fg=color_text,
                 activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                 command=lambda: clicker.help_me())
btnHelp.place(x=5, y=180, width=90, height=60)

# Фрейм скоростей
frame_speed = Frame(root, bg=color_bg)
frame_speed.place(x=310, y=23, width=100, height=400)

speed_min = Button(frame_speed, text='Минимальная',  # одна
                   bg=color_button, fg=color_text, font=('', 8, ''),
                   activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                   command=lambda: clicker.change_speed(0.1))

speed_med = Button(frame_speed, text='Средняя',  # вторая
                   bg=color_button, fg=color_text, font=('', 8, ''),
                   activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                   command=lambda: clicker.change_speed(0.001))

speed_max = Button(frame_speed, text='Максимальная',  # третья
                   bg=color_button, fg=color_text, font=('', 8, ''),
                   activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                   command=lambda: clicker.change_speed(0.0001))

speed_absolyte = Button(frame_speed, text='Абсолютная',  # четвёртая
                        bg=color_button, fg=color_text, font=('', 8, ''),
                        activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                        command=lambda: clicker.change_speed(0.00001))

speed_custom = Button(frame_speed, text='Кастом',  # пятая
                      bg=color_button, fg=color_text, font=('', 8, ''),
                      activebackground=color_button_active, activeforeground=color_text, bd=1, cursor=button_cursor,
                      command=lambda: clicker.custom())

# размещаем кнопки изменения скорости
speed_min.place(x=5, y=0, width=80, height=40)  # Минимальную скорость ставим
speed_med.place(x=5, y=50, width=80, height=40)  # Среднюю
speed_max.place(x=5, y=100, width=80, height=40)  # Максимальную
speed_absolyte.place(x=5, y=150, width=80, height=40)  # Абсолютную
speed_custom.place(x=5, y=200, width=80, height=40)  # абсолютная

root.mainloop()
