def choose (entry, entry2, entry3):
    '''
    function for giving the cook a choice of dishes that he can cook
    функция для предоставления повару выбора блюд, которые он может приготовить
    '''
    def filtr(kitchen, time):
        '''
        function of filtering dishes by characteristics (kitchen, meal time)
        функция фильтрации блюд по характеристикам (кухня, время приема пищи)
        '''
        choose_meals = []
        characteristic_dataframe = tinydb.TinyDB('characteristic.db')
        recipe = tinydb.Query()
        for recipe in characteristic_dataframe:
            if kitchen in recipe["Кухни"] and time in recipe["Приём пищи"]:
                choose_meals.append(str(recipe["Блюдо"]))
        characteristic_dataframe.close()
        return choose_meals

    def choose_recipes(choose_meals, consumers):
        '''
        function that matches the ingredients of filtered dishes with a database of products
        функция, которая сопоставляет ингредиенты отфильтрованных блюд с базой данных продуктов
        '''
        trouble = []
        part = []
        full = []
        products = tinydb.TinyDB('products.db')

        recipes = tinydb.TinyDB('recipes.db')

        for meal in choose_meals:
            flag=0
            a = recipes.search(where("Блюдо") == meal)

            for pr in a:
                b=(pr["Продукт"])
                kol = products.search(where("Продукт") == b)
                if kol:
                    if (not float(pr["Объём"]) * consumers <= float(kol[0]["Объём"])) and pr["Статус"] == "Обязательно":
                        flag = 2
                    elif (not float(pr["Объём"]) * consumers <= float(kol[0]["Объём"])) and pr[
                        "Статус"] == "Необязательно" and flag != 2:
                        flag = 1
                        trouble.append(pr["Продукт"])
                else:
                    if pr["Статус"] == "Обязательно":
                        flag = 3
                    else:
                        flag = 1
                        trouble.append(pr["Продукт"])

            if flag == 0:
                full.append(meal + " (FULL)")
            if flag  == 1:
                part.append(meal + " (PART) Trouble:" + ";".join(trouble))
        products.close()
        recipes.close()
        return (full+part)


    import tinydb
    from tinydb import TinyDB, Query, where
    kitchen = entry
    time = entry2
    consumers = int(entry3)
    res = choose_recipes(filtr(kitchen, time), consumers)
    if not res:
        res = 'Блюд не найдено!\nПополните склад и \nвнесите новые рецепты в базу.'
        return res
    return (";\n".join(res))
