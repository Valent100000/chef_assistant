def refill_recipe_database(meal, massive_ingridients):
    import tinydb
    from tinydb import TinyDB, Query
    db = tinydb.TinyDB('recipes.db')
    Ingredient = Query()
    for position in massive_ingridients:
        db.insert({'Блюдо': meal, 'Продукт': position[0], 'Объём': position[1], 'Единицы': position[2], 'Статус': position[3]})
    db.close()

def refill_product_database(product, amount, units):
    import tinydb
    from tinydb import TinyDB, Query
    db_1 = tinydb.TinyDB('products.db')
    Product = Query()
    db_1.insert({'Продукт': product, 'Объём': amount, 'Единицы': units})
    db_1.close()

def refill_characteristic_database(meal, kitchen, time):
    import tinydb
    from tinydb import TinyDB, Query
    db_2 = tinydb.TinyDB('characteristic.db')
    Meals = Query()
    kitchen = kitchen.split()
    time = time.split()
    db_2.insert({'Блюдо': meal, 'Кухни': kitchen, 'Приём пищи': time})
    db_2.close()

def delete_product(product):
    import tinydb
    from tinydb import TinyDB, Query, where
    db_1 = tinydb.TinyDB('products.db')
    Product = Query()
    db_1.remove(where('Продукт') == product)
    db_1.close()

def delete_recipe(meal):
    import tinydb
    from tinydb import TinyDB, Query, where
    db = tinydb.TinyDB('recipes.db')
    Resipe = Query()
    db.remove(where('Блюдо') == meal)
    db_2 = tinydb.TinyDB('characteristic.db')
    Meals = Query()
    db_2.remove(where('Блюдо') == meal)
    db.close()
    db_2.close()
