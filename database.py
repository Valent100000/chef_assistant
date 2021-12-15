def refill_recipe_database(meal, massive_ingridients):
    import tinydb
    from tinydb import TinyDB, Query
    db = tinydb.TinyDB('recipes.db')
    Ingredient = Query()
    for position in massive_ingridients:
        db.insert({'Блюдо': meal, 'Продукт': position[0], 'Объём': position[1], 'Единицы': position[2], 'Статус': position[3]})

def refill_product_database(product, amount, units):
    import tinydb
    from tinydb import TinyDB, Query
    db_1 = tinydb.TinyDB('products.db')
    Product = Query()
    db_1.insert({'Продукт': product, 'Объём': amount, 'Единицы': units})

def refill_characteristic_database(meal, kitchen, time):
    import tinydb
    from tinydb import TinyDB, Query
    db_2 = tinydb.TinyDB('characteristic.db')
    Meals = Query()
    kitchen = kitchen.split()
    time = time.split()
    db_2.insert({'Блюдо': meal, 'Кухни': kitchen, 'Приём пищи': time})

