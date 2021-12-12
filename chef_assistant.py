def choose (entry, entry2, entry3):
    def filtr(kitchen, time):
        choose_meals = []
        characteristic_dataframe = tinydb.TinyDB('characteristic.db')
        recipe = tinydb.Query()
        for recipe in characteristic_dataframe:
            if kitchen in recipe["Кухни"] and time in recipe["Приём пищи"]:
                choose_meals.append(str(recipe["Блюдо"]))
        return choose_meals

    def choose_recipes(choose_meals, consumers):


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

                if (not float(pr["Объём"])*consumers<=float(kol[0]["Объём"])) and pr["Статус"] == "Обязательно":
                    flag=2
                elif (not float(pr["Объём"])*consumers<=float(kol[0]["Объём"])) and pr["Статус"] == "Необязательно" and flag!=2:
                    flag=1
                    trouble.append(pr["Продукт"])
            if flag == 0:
                full.append(meal + " (FULL)")
            if flag  == 1:
                part.append(meal + " (PART) Trouble:" + ";".join(trouble))
        return (full+part)


    import tinydb
    from tinydb import TinyDB, Query, where
    kitchen = entry
    time = entry2
    consumers = int(entry3)
    return (";".join(choose_recipes(filtr(kitchen, time), consumers)))
