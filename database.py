def refill_recipe_database(meal, massive_ingridients):
    """
    function for replenishing the recipe database\n
    функция для пополнения базы данных рецептов
    """
    import tinydb
    from tinydb import TinyDB, Query
    db = tinydb.TinyDB('recipes.db')
    Ingredient = Query()
    if meal and massive_ingridients:
        for position in massive_ingridients:
            db.insert({'Блюдо': meal, 'Продукт': position[0], 'Объём': position[1], 'Единицы': position[2], 'Статус': position[3]})
    db.close()

def refill_product_database(product, amount, units):
    """
    function to replenish the database of products in stock\n
    функция для пополнения базы данных товаров на складе
    """
    import tinydb
    from tinydb import TinyDB, Query
    db_1 = tinydb.TinyDB('products.db')
    Product = Query()
    if product and amount and units:
        db_1.insert({'Продукт': product, 'Объём': amount, 'Единицы': units})
    db_1.close()

def refill_characteristic_database(meal, kitchen, time):
    """
   function to replenish the database of goods by characteristics of the kitchen and the time of food intake\n
   функция для пополнения базы данных товаров по характеристикам кухня и время приема пищи
    """
    import tinydb
    from tinydb import TinyDB, Query
    db_2 = tinydb.TinyDB('characteristic.db')
    Meals = Query()
    kitchen = kitchen.split()
    time = time.split()
    if meal and kitchen and time:
        db_2.insert({'Блюдо': meal, 'Кухни': kitchen, 'Приём пищи': time})
    db_2.close()
    
def delete_product(product):
    """
    function of delete the product from the database\n
    функция удаления продукт из базы данных
    """
    import tinydb
    from tinydb import TinyDB, Query, where
    db_1 = tinydb.TinyDB('products.db')
    Product = Query()
    if product:
        db_1.remove(where('Продукт') == product)
    db_1.close()

def delete_recipe(meal):
    """
    function of deleting a recipe from the database\
    функция удаления рецепта из базы данных
    """
    import tinydb
    from tinydb import TinyDB, Query, where
    db = tinydb.TinyDB('recipes.db')
    Resipe = Query()
    if meal:
        db.remove(where('Блюдо') == meal)
    db_2 = tinydb.TinyDB('characteristic.db')
    Meals = Query()
    if meal:
        db_2.remove(where('Блюдо') == meal)
    db.close()
    db_2.close()

