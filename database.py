def refill_recipe_database(meal, product, amount, units, status):
    import tinydb
    from tinydb import TinyDB, Query
    db = tinydb.TinyDB('recipes.db')
    Ingredient = Query()
    db.insert({'Блюдо': meal, 'Продукт': product, 'Объём': amount, 'Единицы': units, 'Статус': status})

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


