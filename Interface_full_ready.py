from tkinter import *

from chef_assistant import choose
from database import refill_recipe_database, refill_product_database, refill_characteristic_database, delete_product, delete_recipe

def NewWindow():
    """
    creating the main window
    result: collects data entered in the entry\n
    создание главного окна
    результат: собирает данные, введенные в поля для ввода
    """
    Window1 = Toplevel(Window)
    Window1.geometry('650x450+300+200')  # размер окна
    Window1['bg'] = '#FFF5cb'  # цвет окна
    Label(Window1, text='Что можно приготовить:', bg='#FFF5cb', fg='#4F6000', font=("Etna", 13, "italic")).place(x=10,
                                                                                                                 y=40)

    result = Label(Window1, text=choose(str(entry.get()), str(entry2.get()), str(entry3.get())), bg='#FFF5cb',
                   fg='#4F6000', font=("Etna", 13, "italic"))  # текстовый результат для выбора блюда
    result.place(x=200, y=70)


def NewWindow2():
    """
    creating a child window, in which we add recipes to the database\n
    создание дочернего окна, в котором мы добавляем рецепт в базу данных
    основа кода добавления прокрутки окна на строках 33-41 и 122 - 126 была взята с источника: https://blog.teclado.com/tkinter-scrollable-frames/
    """
    Window2_host = Toplevel(Window)
    Window2_host.geometry('650x450+300+200')  # размер окна
    Window2_host['bg'] = '#FFF5cb'  # цвет окна
    canvas = Canvas(Window2_host)  # прокручиваемый контейнер
    Window2 = Frame(canvas)  # добавление фрейм в контейнер canvas
    Window2_host.bind( "<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) #

    frame = Frame(Window2, bg='#FFF5cb')  # добавление спец поля для прокручиваемых элементов
    scrollbar = Scrollbar(Window2_host, orient='vertical',
                          command=canvas.yview)  # скролл в окне, ориентация вертикальная, команда пролистывания контейнер
    scrollbar.pack(side=RIGHT, fill=Y)  # расположение скролла по правой стороне и движение по оси У
    canvas.configure(yscrollcommand=scrollbar.set)  # перемещение поля canvas по вертикали

    dish_name = Label(Window2, text="Введите название блюда:", bg="#FFF5cb", fg="black",
                      font=("Etna", 10, "italic"))  # текст в окне , цвет текста, цвет заднего поля # шрифт
    kitchen = Label(Window2, bg="#FFF5cb", text="Введите название кухни:", font=("Etna", 10, "italic")) # текст в окне , цвет текста, цвет заднего поля # шрифт
    type_of_eating_time = Label(Window2, bg="#FFF5cb", text="Введите приём пищи:", font=("Etna", 10, "italic")) # текст в окне , цвет текста, цвет заднего поля # шрифт

    dish_name.place(x=50, y=50)  # расположение Название блюда
    kitchen.place(x=50, y=100)  # расположение Название кухни
    type_of_eating_time.place(x=50, y=75) # расположение текста тип приема пищи

    dish = Entry(Window2, bg="white", fg="black", width=30)  # строка для ввода Названия блюда
    kitch = Entry(Window2, bg="white", fg="black", width=20)    # строка для ввода Названия кухни
    type_time = Entry(Window2, bg="white", fg="black", width=20) # строка для ввода типа приема пищи
    dish.place(x=250, y=50)  # расположение поля ввода названия блюда
    kitch.place(x=250, y=100) # расположение поля ввода названия кухни
    type_time.place(x=250, y=75) # расположение поля ввода типа приема пищи

    entryWidgets = []
    massive_ingredients = []
    labelWidgets = []

    class Widgets():
        """
        class for working with ingredients entered in the added entries when the button is clicked\n
        класс для работы с ингредиентами, введенными в добавленные поля ввода с помощью кнопки
        """

        def add_entry(self, entryWidgets, labelWidgets):
            """
            function for adding a new field for entering information when the button is clicked\n
            функция для добавления нового поля для ввода информации при нажатии на кнопку
            """
            global ingr_ingr_horiz_coord, ingr_ingr_txt_horiz_coord, ingr_val_horiz_coord, ingr_val_txt_horiz_coord, ingr_un_horiz_coord, ingr_un_txt_horiz_coord, ingr_st_horiz_coord, ingr_st_txt_horiz_coord, ingr_vertical_coord
            entryWidgets.append(
                [Entry(frame, bg="white", fg="black", width=20), Entry(frame, bg="white", fg="black", width=5),
                 Entry(frame, bg="white", fg="black", width=5), Entry(frame, bg="white", fg="black", width=15)])
            entryWidgets[-1][0].place(x=ingr_ingr_horiz_coord, y=ingr_vertical_coord)
            entryWidgets[-1][1].place(x=ingr_val_horiz_coord, y=ingr_vertical_coord)
            entryWidgets[-1][2].place(x=ingr_un_horiz_coord, y=ingr_vertical_coord)
            entryWidgets[-1][3].place(x=ingr_st_horiz_coord, y=ingr_vertical_coord)

            labelWidgets.append(
                [Label(frame, text="Ингредиент:", bg="#FFF5cb", fg="black", font=("Etna", 10, "italic")),
                 Label(frame, text="Объем:", bg="#FFF5cb", fg="black", font=("Etna", 10, "italic")),
                 Label(frame, text="Ед.измер:", bg="#FFF5cb", fg="black", font=("Etna", 10, "italic")),
                 Label(frame, text="Статус:", bg="#FFF5cb", fg="black", font=("Etna", 10, "italic"))])
            labelWidgets[-1][0].place(x=ingr_ingr_txt_horiz_coord, y=ingr_vertical_coord)
            labelWidgets[-1][1].place(x=ingr_val_txt_horiz_coord, y=ingr_vertical_coord)
            labelWidgets[-1][2].place(x=ingr_un_txt_horiz_coord, y=ingr_vertical_coord)
            labelWidgets[-1][3].place(x=ingr_st_txt_horiz_coord, y=ingr_vertical_coord)

            ingr_vertical_coord += 50

        def getEntries(self, entryWidgets, massive_ingridients):
            """
            function for reading information about the entered ingredient and sending it to the database\n
            функция для считывания информации о введенном ингредиенте и отправки его в базу данных
            """
            for x in entryWidgets:
                massive_ingridients.append([str(x[0].get()), str(x[1].get()), str(x[2].get()), str(x[3].get())])

            return (massive_ingridients)

    def delete_button():
        """
        function to close the child window when the button is pressed\n
        функция закрывает дочернее окно при нажатии на кнопку 'Готово'
        """
        global ingr_vertical_coord
        ingr_vertical_coord = 145
        Window2_host.destroy()

    button4 = Button(Window2_host, text="Готово", command=lambda: (
        refill_characteristic_database(str(dish.get()), str(kitch.get()),
                                       str(type_time.get())),
        refill_recipe_database(str(dish.get()), Widgets().getEntries(entryWidgets, massive_ingredients)),
        delete_button()))  # кнопка добавить рецепт в базу данных и закрыть окно
    button4.place(x=300, y=10) # расположение кнопки добавить рецепт в базу данных и закрыть окно

    Widgets().add_entry(entryWidgets, labelWidgets)
    Button(Window2_host, text='+', command=lambda: Widgets().add_entry(entryWidgets, labelWidgets)).place(x=550, y=80) # кнопка добавить доп поля для ввода и расположение кнопки

    scrollbar.pack()
    frame.pack(side='left', ipadx=400, ipady=800, expand=True)  # размер окна frame
    Window2.pack(side="left", fill="both", expand=True)  # выравнивание по левой стороне,
    canvas.create_window((0, 0), window=Window2,anchor="nw")  # расположение контейнера, левый верхний угол имеет координаты 0,0
    canvas.pack(side="left", fill="both", expand=True)  # выравнивание по левой стороне,


def NewWindow3():
    """
    creating a child window, in which we add products or delete the product from the database and delete the recipe from the database\n
    создание дочернего окна, в котором мы добавляем продукт или удаляем продукт из базы данных, удаляем рецепт из базы данных
    """
    Window3 = Toplevel(Window)
    Window3.geometry('650x450+300+200')  # размер окна
    Window3['bg'] = '#FFF5cb'  # цвет окна

    label = Label(Window3, text="Добавление продукта на склад:", fg="black", bg='#FFF5cb', font=("Times", "20", "bold")) # текст в окне и цвет текста # шрифт
    product = Label(Window3, text="Продукт:", bg="#FFF5cb", fg="black",
                    font=("Etna", 10, "italic"))  # текст в окне и цвет текста # шрифт
    valume = Label(Window3, text="Объем:", bg="#FFF5cb", fg="black",
                   font=("Etna", 10, "italic"))  # текст в окне и цвет текста  # шрифт
    unit = Label(Window3, text="Ед.измер:", bg="#FFF5cb", fg="black", font=("Etna", 10, "italic")) # текст в окне и цвет текста # шрифт

    label.place(x=130, y=50)  # расположение текста Добавление продукта на склад
    product.place(x=50, y=110)  # расположение текста продукт
    valume.place(x=270, y=110)  # расположение текста объем
    unit.place(x=370, y=110)    # расположение текста ед. измерения

    prod = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода продукт
    val = Entry(Window3, bg="white", fg="black", width=5)   # строка для ввода объема
    un = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения

    prod.place(x=140, y=110) # расположение поля для ввода продукт
    val.place(x=330, y=110) # расположение поля для ввода объема
    un.place(x=440, y=110)  # расположение поля для ввода единица измерения

    label2 = Label(Window3, text="Удаление продукта со склада:", fg="black", bg='#FFF5cb',
                  font=("Times", "20", "bold"))  # текст в окне и цвет текста # шрифт
    product2 = Label(Window3, text="Продукт:", bg="#FFF5cb", fg="black",
                    font=("Etna", 10, "italic"))  # текст в окне и цвет текста # шрифт


    label2.place(x=130, y=180)  # расположение текста Удаление продукта со склада
    product2.place(x=50, y=250)  # расположение текста продукт


    prod2 = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода продукт

    prod2.place(x=140, y=250)  # расположение поля для ввода продукт

    label3 = Label(Window3, text="Удаление рецепта:", fg="black", bg='#FFF5cb',
                   font=("Times", "20", "bold"))  # текст в окне и цвет текста # шрифт
    product3 = Label(Window3, text="Продукт:", bg="#FFF5cb", fg="black",
                     font=("Etna", 10, "italic"))  # текст в окне и цвет текста # шрифт

    label3.place(x=130, y=290)  # расположение текста Удаление рецепта со склада
    product3.place(x=50, y=350)  # расположение текста продукт

    prod3 = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода продукт

    prod3.place(x=140, y=350)  # расположение поля для ввода продукт


    def delete_button():
        """
        function to close the child window when the button is pressed\n
        функция закрывает дочернее окно при нажатии на кнопку 'Добавить'
        """
        Window3.destroy()


    button5 = Button(Window3, text="Готово", command=lambda: (refill_product_database(str(prod.get()), str(val.get()),
                                                                                        str(un.get())), delete_product(prod2.get()),delete_recipe(prod3.get()), delete_button())) # передача данных в ответственные функции

    button5.place(x=300, y=400)  # расположение кнопки для добавления продукта на склад и закрытие окна


Window = Tk()  # основное окно
Window.title('Помощник Повара')  # заголовок
Window.geometry('650x450+300+200')  # размер окна
Window.resizable(width=False, height=False)  # невозможность менять размер окна
Window.image = PhotoImage(file='bg.png')  # установка картинки на задний фон
bg_img = Label(Window, image=Window.image)  # установка картинки задним фоном
bg_img.place(x=0, y=0)  # расположение картинки

button = Button(Window, text="Показать варианты", command=NewWindow)  # кнопка показать результат
button.place(x=250, y=300)  # расположение кнопки

button2 = Button(Window, text="Добавить рецепт", command=NewWindow2)  # кнопка добавить рецепт
button2.place(x=510, y=390)  # расположение кнопки 'Добавить рецепт'

button3 = Button(Window, text="Редактировать базы данных", command=NewWindow3)  # кнопка добавить рецепт
button3.place(x=280, y=390)  # расположение кнопки 'Добавить продукт на склад'

text1 = Label(Window, text="Введите название кухни:", bg="#FFF5cb", fg="#4F6000",
              font=("Etna", 11, "italic"))  # текст в основном окне и цвет текста # шрифт
text2 = Label(Window, text="Введите тип приема пищи:", bg="#FFF5cb", fg="#4F6000",
              font=("Etna", 11, "italic"))  # текст в основном окне и цвет текста  # шрифт
text3 = Label(Window, text="Введите количество человек:", bg="#FFF5cb", fg="#4F6000",
              font=("Etna", 11, "italic"))  # текст в основном окне и цвет текста  # шрифт

text1.place(x=110, y=130)  # расположение текста введите название кухню
text2.place(x=100, y=180)  # расположение текста введите тип приема пищи
text3.place(x=80, y=230)  # расположение текста введите количество человек

entry = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Названия Кухни
entry2 = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Типа приема пищи
entry3 = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Количества порций

entry.place(x=300, y=130)  # расположение поля ввода
entry2.place(x=300, y=180)  # расположение поля ввода2
entry3.place(x=300, y=230)  # расположение поля ввода3

ingr_ingr_horiz_coord = 140
ingr_val_horiz_coord = 320
ingr_un_horiz_coord = 430
ingr_st_horiz_coord = 530
ingr_ingr_txt_horiz_coord = 45
ingr_val_txt_horiz_coord = 265
ingr_un_txt_horiz_coord = 365
ingr_st_txt_horiz_coord = 465
ingr_vertical_coord = 145

Window.mainloop()
