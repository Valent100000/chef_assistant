from tkinter import *
#from chef_assistant import choose


def NewWindow():
    Window2 = Toplevel(Window)
    Window2.geometry('650x450+300+200')  # размер окна
    Window2['bg'] = '#FFF5cb'  # цвет окна

    #result = Label(Window2, text=choose(str(entry.get()), str(entry2.get()), str(entry3.get())))  #
    #result.place(x=120, y=305)

    #result.pack()
    button.pack()


def NewWindow2():
    Window3 = Toplevel(Window)
    Window3.geometry('650x450+300+200')  # размер окна
    Window3['bg'] = '#FFF5cb'  # цвет окна



    dish_name = Label(Window3, text="Введите название блюда:", fg="black")  # текст в окне и цвет текста
    kitchen = Label(Window3, text="Введите название кухни:")
    ingredient1 = Label(Window3, text="Ингридиент1:", fg="black")  # текст в окне и цвет текста
    valume1 = Label(Window3, text="Объем:", fg="black")  # текст в окне и цвет текста  # шрифт
    unit1 = Label(Window3, text="Ед.измер:", fg="black")
    status1 = Label(Window3, text="Статус:", fg="black")

    ingredient2 = Label(Window3, text="Ингридиент2:", fg="black")  # текст в окне и цвет текста
    valume2 = Label(Window3, text="Объем:", fg="black")  # текст в окне и цвет текста  # шрифт
    unit2 = Label(Window3, text="Ед.измер:", fg="black")
    status2 = Label(Window3, text="Статус:", fg="black")

    ingredient3 = Label(Window3, text="Ингридиент3:", fg="black")  # текст в окне и цвет текста
    valume3 = Label(Window3, text="Объем:", fg="black")  # текст в окне и цвет текста  # шрифт
    unit3 = Label(Window3, text="Ед.измер:", fg="black")
    status3 = Label(Window3, text="Статус:", fg="black")

    ingredient4 = Label(Window3, text="Ингридиент4:", fg="black")  # текст в окне и цвет текста
    valume4 = Label(Window3, text="Объем:", fg="black")  # текст в окне и цвет текста  # шрифт
    unit4 = Label(Window3, text="Ед.измер:", fg="black")
    status4 = Label(Window3, text="Статус:", fg="black")

    dish_name.place(x=50, y=50)  # расположение Название блюда
    kitchen.place(x=50, y=100)
    ingredient1.place(x=50, y=150)  # расположение текста Ингридиент1
    valume1.place(x=270, y=150)  # расположение текста Объем
    unit1.place(x=370, y=150)
    status1.place(x=480, y=150)

    ingredient2.place(x=50, y=200)  # расположение текста Ингридиент2
    valume2.place(x=270, y=200)
    unit2.place(x=370, y=200)
    status2.place(x=480, y=200)

    ingredient3.place(x=50, y=250)  # расположение текста Ингридиент3
    valume3.place(x=270, y=250)
    unit3.place(x=370, y=250)
    status3.place(x=480, y=250)

    ingredient4.place(x=50, y=300)  # расположение текста Ингридиент4
    valume4.place(x=270, y=300)
    unit4.place(x=370, y=300)
    status4.place(x=480, y=300)

    dish = Entry(Window3, bg="white", fg="black", width=30)  # строка для ввода Названия блюда
    kitch = Entry(Window3, bg="white", fg="black", width=20)
    ingr1 = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода Ингридиент1
    val1 = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода Объем
    un1 = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения
    st1 = Entry(Window3, bg="white", fg="black", width=15)  # строка для ввода Объем

    ingr2 = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода Ингридиент2
    val2 = Entry(Window3, bg="white", fg="black", width=5)
    un2 = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения
    st2 = Entry(Window3, bg="white", fg="black", width=15)  # строка для ввода Объем

    ingr3 = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода Ингридиент3
    val3 = Entry(Window3, bg="white", fg="black", width=5)
    un3 = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения
    st3 = Entry(Window3, bg="white", fg="black", width=15)  # строка для ввода Объем

    ingr4 = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода Ингридиент4
    val4 = Entry(Window3, bg="white", fg="black", width=5)
    un4 = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения
    st4 = Entry(Window3, bg="white", fg="black", width=15)  # строка для ввода Объем

    dish.place(x=200, y=50)  # расположение поля ввода
    kitch.place(x=200, y=100)

    ingr1.place(x=140, y=150)
    val1.place(x=320, y=150)
    un1.place(x=430, y=150)
    st1.place(x=530, y=150)

    ingr2.place(x=140, y=200)
    val2.place(x=320, y=200)
    un2.place(x=430, y=200)
    st2.place(x=530, y=200)

    ingr3.place(x=140, y=250)
    val3.place(x=320, y=250)
    un3.place(x=430, y=250)
    st3.place(x=530, y=250)

    ingr4.place(x=140, y=300)
    val4.place(x=320, y=300)
    un4.place(x=430, y=300)
    st4.place(x=530, y=300)


    button2.pack()  # вызов кнопкой окна 2


def NewWindow3():
    Window3 = Toplevel(Window)
    Window3.geometry('650x450+300+200')  # размер окна
    Window3['bg'] = '#FFF5cb'  # цвет окна

    label = Label(Window3, text="Добавление продукта на склад:", fg="black", bg='#FFF5cb', font=("Times", "20", "bold"))
    product = Label(Window3, text="Продукт:", fg="black")  # текст в окне и цвет текста
    valume = Label(Window3, text="Объем:", fg="black")  # текст в окне и цвет текста  # шрифт
    unit = Label(Window3, text="Ед.измер:", fg="black")

    label.place(x=100, y=100)
    product.place(x=50, y=200)  # расположение текста Ингридиент2
    valume.place(x=270, y=200)
    unit.place(x=370, y=200)

    prod = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода Ингридиент2
    val = Entry(Window3, bg="white", fg="black", width=5)
    un = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения

    prod.place(x=140, y=200)
    val.place(x=320, y=200)
    un.place(x=430, y=200)

    button3.pack()


Window = Tk()  # основное окно
Window.title('Помощник Повара')  # заголовок
Window.geometry('650x450+300+200')  # размер окна
Window.resizable(width=False, height=False)  # невозможность менять размер окна
Window.image = PhotoImage(file='ф.png')  # установка картинки на задний фон
bg_img = Label(Window, image=Window.image)  # установка картинки задним фоном
bg_img.place(x=0, y=0)  # расположение картинки

button = Button(Window, text="Показать варианты", command=NewWindow)  # кнопка показать результат
button.place(x=250, y=300)  # расположение кнопки

button2 = Button(Window, text="Добавить рецепт", command=NewWindow2)  # кнопка добавить рецепт
button2.place(x=510, y=400)  # расположение кнопки добавить рецепт

button3 = Button(Window, text="Добавить продукт на склад", command=NewWindow3)  # кнопка добавить рецепт
button3.place(x=280, y=400)  # расположение кнопки добавить рецепт

text1 = Label(Window, text="Введите название кухни(-онь):", fg="black")  # текст в основном окне и цвет текста # шрифт
text2 = Label(Window, text="Введите тип(-ы) приема пищи:", fg="black")  # текст в основном окне и цвет текста  # шрифт
text3 = Label(Window, text="Введите количество человек:", fg="black")  # текст в основном окне и цвет текста  # шрифт

text1.place(x=120, y=130)  # расположение текста введите название кухню
text2.place(x=120, y=180)  # расположение текста введите тип приема пищи
text3.place(x=120, y=230)  # расположение текста введите количество человек

entry = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Названия Кухни
entry2 = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Типа приема пищи
entry3 = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Количества порций

entry.place(x=300, y=130)  # расположение поля ввода
entry2.place(x=300, y=180)  # расположение поля ввода2
entry3.place(x=300, y=230)  # расположение поля ввода3

Window.mainloop()
