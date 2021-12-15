from tkinter import *
from tkinter.ttk import Combobox

from chef_assistant import choose
from database import refill_recipe_database, refill_product_database, refill_characteristic_database


def NewWindow():
    Window1 = Toplevel(Window)
    Window1.geometry('650x450+300+200')  # размер окна
    Window1['bg'] = '#FFF5cb'  # цвет окна

    result = Label(Window1, text=choose(str(entry.get()), str(entry2.get()), str(entry3.get())))  #
    result.place(x=120, y=305)



def NewWindow2():
    Window2 = Toplevel(Window)
    Window2.geometry('650x450+300+100')  # размер окна
    Window2['bg'] = '#FFF5cb'  # цвет окна


    dish_name = Label(Window2, text="Введите название блюда:", bg="#FFF5cb",fg="black", font=("Etna", 10, "italic") )  # текст в окне и цвет текста
    kitchen = Label(Window2, bg="#FFF5cb", text="Введите название кухни:", font=("Etna", 10, "italic"))
    type_of_eating_time = Label(Window2,bg="#FFF5cb", text="Введите приём пищи:", font=("Etna", 10, "italic"))  # !!!!!!!!!!!

    dish_name.place(x=50, y=50)  # расположение Название блюда
    kitchen.place(x=50, y=100)
    type_of_eating_time.place(x=50, y=75)  # !!!!!!!

    dish = Entry(Window2, bg="white", fg="black", width=30)  # строка для ввода Названия блюда
    kitch = Entry(Window2, bg="white", fg="black", width=20)
    type_time = Entry(Window2, bg="white", fg="black", width=20)  # !!!!!!!!!!!!
    dish.place(x=250, y=50)  # расположение поля ввода
    kitch.place(x=250, y=100)
    type_time.place(x=250, y=75)  # !!!!!!!!!!!

    entryWidgets = []
    massive_ingridients = []
    labelWidgets = []

    class entrylabel():
        def add_entry(self, entryWidgets, labelWidgets):
            global ingr_ingr_horiz_coord, ingr_ingr_txt_horiz_coord, ingr_val_horiz_coord, ingr_val_txt_horiz_coord, ingr_un_horiz_coord, ingr_un_txt_horiz_coord, ingr_st_horiz_coord, ingr_st_txt_horiz_coord, ingr_vertical_coord
            entryWidgets.append(
                [Entry(Window2, bg="white", fg="black", width=20), Entry(Window2,bg="white",fg="black", width=5),
                 Entry(Window2, bg="white", fg="black", width=5), Entry(Window2, bg="white", fg="black", width=15)])
            entryWidgets[-1][0].place(x=ingr_ingr_horiz_coord, y=ingr_vertical_coord)
            entryWidgets[-1][1].place(x=ingr_val_horiz_coord, y=ingr_vertical_coord)
            entryWidgets[-1][2].place(x=ingr_un_horiz_coord, y=ingr_vertical_coord)
            entryWidgets[-1][3].place(x=ingr_st_horiz_coord, y=ingr_vertical_coord)

            labelWidgets.append(
                [Label(Window2, text="Ингредиент:",bg="#FFF5cb", fg="black", font=("Etna", 10, "italic")), Label(Window2, text="Объем:", bg="#FFF5cb",fg="black", font=("Etna", 10, "italic")),
                 Label(Window2, text="Ед.измер:", bg="#FFF5cb",fg="black", font=("Etna", 10, "italic")), Label(Window2, text="Статус:", bg="#FFF5cb",fg="black", font=("Etna", 10, "italic"))])
            labelWidgets[-1][0].place(x=ingr_ingr_txt_horiz_coord, y=ingr_vertical_coord)
            labelWidgets[-1][1].place(x=ingr_val_txt_horiz_coord, y=ingr_vertical_coord)
            labelWidgets[-1][2].place(x=ingr_un_txt_horiz_coord, y=ingr_vertical_coord)
            labelWidgets[-1][3].place(x=ingr_st_txt_horiz_coord, y=ingr_vertical_coord)

            ingr_vertical_coord += 50

        def getEntries(self, entryWidgets, massive_ingridients):
            for x in entryWidgets:# i.e for each widget in entryWidget list
                massive_ingridients.append([str(x[0].get()), str(x[1].get()),str(x[2].get()), str(x[3].get())])

            print(massive_ingridients)
            return(massive_ingridients)
        # ingr_vertical_coord = add_entry(self, entryWidgets, labelWidgets)

    # Ингредиент, Объем, единица измерения, статус
    def delete_button():
        Window2.destroy()
    button4 = Button(Window2, text="Готово", command=lambda: (
                refill_characteristic_database(str(dish.get()), str(kitch.get()),
                                       str(type_time.get())), refill_recipe_database(str(dish.get()), entrylabel().getEntries(entryWidgets, massive_ingridients)), delete_button()))  # кнопка добавить рецепт !!!!!!!!!!
    button4.place(x=300, y=10)
    entrylabel().add_entry(entryWidgets, labelWidgets)
    Button(Window2, text='+', command=lambda: entrylabel().add_entry(entryWidgets, labelWidgets)).place(x=550, y=80)





def NewWindow3():
    Window3 = Toplevel(Window)
    Window3.geometry('650x450+300+200')  # размер окна
    Window3['bg'] = '#FFF5cb'  # цвет окна

    label = Label(Window3, text="Добавление продукта на склад:", fg="black", bg='#FFF5cb', font=("Times", "20", "bold"))
    product = Label(Window3, text="Продукт:", bg="#FFF5cb", fg="black",font=("Etna", 10, "italic"))  # текст в окне и цвет текста
    valume = Label(Window3, text="Объем:", bg="#FFF5cb", fg="black",font=("Etna", 10, "italic"))  # текст в окне и цвет текста  # шрифт
    unit = Label(Window3, text="Ед.измер:", bg="#FFF5cb", fg="black", font=("Etna", 10, "italic"))

    label.place(x=130, y=100)
    product.place(x=50, y=200)  # расположение текста Ингридиент2
    valume.place(x=270, y=200)
    unit.place(x=370, y=200)

    prod = Entry(Window3, bg="white", fg="black", width=20)  # строка для ввода Ингридиент2
    val = Entry(Window3, bg="white", fg="black", width=5)
    un = Entry(Window3, bg="white", fg="black", width=5)  # строка для ввода единица измерения

    prod.place(x=140, y=200)
    val.place(x=330, y=200)
    un.place(x=440, y=200)

    def delete_button2():
        Window3.destroy()
    button5 = Button(Window3, text="Добавить", command=lambda: (refill_product_database(str(prod.get()), str(val.get()),
                                                                                        str(un.get())), delete_button2()))  # кнопка
    # добавить
    # продукт !!!!!!!!!!!!!!!!!!!!

    button5.place(x=280, y=400)


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
button2.place(x=510, y=400)  # расположение кнопки добавить рецепт

button3 = Button(Window, text="Добавить продукт на склад", command=NewWindow3)  # кнопка добавить рецепт
button3.place(x=280, y=400)  # расположение кнопки добавить рецепт

text1 = Label(Window, text="Введите название кухни:",bg="#FFF5cb", fg="#4F6000",font=("Etna", 11, "italic"))  # текст в основном окне и цвет текста # шрифт
text2 = Label(Window, text="Введите тип приема пищи:", bg="#FFF5cb", fg="#4F6000", font=("Etna", 11, "italic"))  # текст в основном окне и цвет текста  # шрифт
text3 = Label(Window, text="Введите количество человек:", bg="#FFF5cb",fg="#4F6000", font=("Etna", 11, "italic"))  # текст в основном окне и цвет текста  # шрифт

text1.place(x=110, y=130)  # расположение текста введите название кухню
text2.place(x=100, y=180)  # расположение текста введите тип приема пищи
text3.place(x=80, y=230)  # расположение текста введите количество человек

entry = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Названия Кухни
entry2 = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Типа приема пищи
entry3 = Entry(Window, bg="white", fg="black", width=30)  # строка для ввода Количества порций

entry.place(x=300, y=130)  # расположение поля ввода
entry2.place(x=300, y=180)  # расположение поля ввода2
entry3.place(x=300, y=230)  # расположение поля ввода3

ingr_ingr_horiz_coord=140
ingr_val_horiz_coord=320
ingr_un_horiz_coord=430
ingr_st_horiz_coord=530
ingr_ingr_txt_horiz_coord=45
ingr_val_txt_horiz_coord=265
ingr_un_txt_horiz_coord=365
ingr_st_txt_horiz_coord=465
ingr_vertical_coord=145


Window.mainloop()