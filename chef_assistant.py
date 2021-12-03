def filtr(kitchen, time):#выдаёт массив названий блюд, подходящих по кухне блюда и времени еды
    a = []#массив с строками файла
    with open("recepts.csv", "r", encoding="utf-8-sig") as f:#кодировка sig для игнорирования ненужных настроечных битов в начале файла
        for line in f:
            a.append(line.rstrip())

    correct = []#отфильтрованные строки
    meals = []#массив названий найденных отсортированных блюд
    for i in range(len(a)):
        if kitchen in a[i] and time in a[i]:
            correct.append(a[i])
    for eda in correct:
        eda = eda[:eda.find(";")]#срез с названием блюда
        meals.append(eda)
        #print(meals)
    return (meals)

def choose_recipes(meals):#расчёт из количества продуктов
    result_full = []
    result_part = []
    fls = []
    for meal in meals:
        recipe_dataframe = pandas.read_excel(meal+".xlsx")#открываем файл рецепта
        recipe_dataframe = pandas.merge(recipe_dataframe, products_dataframe, how='left', on='Продукт')#добавляем в датафрейм рецепта объём необходимых продуктов на складе
        recipe_dataframe ['Объём_x'] = recipe_dataframe ['Объём_x'].multiply(consumers)#умножаем объём необходимых продуктов на количество людей
        recipe_dataframe['Сравнение'] = recipe_dataframe['Объём_x'] <= recipe_dataframe['Объём_y']#сравнение массы необходимых и имеющихся продуктов
        #print(recipe_dataframe)
        if  not False in recipe_dataframe["Сравнение"].values:
            result_full.append(meal+" (FULL)")
        else:
            fls = recipe_dataframe.query('Сравнение == False')
            #print(fls)
            if not "Обязательно" in fls["Статус"].values:
                result_part.append(meal + " (PART) Trouble:" + str(fls["Продукт"].values))


    return (result_full+result_part)

import pandas
kitchen = input("Какая кухня подаётся сегодня? ")
time = input("Какой приём пищи? ")
consumers = int(input("Сколько человек придёт на приём пищи? "))
products_dataframe = pandas.read_excel('Products.xlsx')
print("Choose:", ";".join(choose_recipes(filtr(kitchen, time))))