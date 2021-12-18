def refill_recipe_database(meal, massive_ingredients):
    """
    function for replenishing the recipe database
    Parameters
    meal: str
    name of the dish

    massive_ingredients: array with arrays for each ingredient,
    nested arrays have a structure of strings.
    elements:
    [0] - product
    [1] - volume
    [2] - units
    [3] - status (Required/ Optional)

    функция для пополнения базы данных рецептов
    meal: строка с названием блюда

    massive_ingredients: массив с массивами для каждого ингредиента,
    вложенные массивы имеют структуру из строк.
    элементы:
    [0] - продукт
    [1] - объём
    [2] - единицы
    [3] - статус (Обязательно/ Необязательно)
    """
    import tinydb
    from tinydb import TinyDB, Query
    db = tinydb.TinyDB('recipes.db')
    Ingredient = Query()
    if meal and massive_ingredients:
        for position in massive_ingredients:
            db.insert({'Блюдо': meal, 'Продукт': position[0], 'Объём': position[1], 'Единицы': position[2], 'Статус': position[3]})
    db.close()

def refill_product_database(product, amount, units):
    """
    function to replenish the database of products in stock
    Parameters
    product: str
    entering product
    amount: str
    entering the volume
    units: str
    entering the unit of measurement

    функция для пополнения базы данных товаров на складе
    Параметры:
    product: фильтр продукт
    amount: фильтр объёма
    units: фильтр единицы измерения
    product, amount, units --> строковые
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
   function to replenish the database of goods by characteristics of the kitchen and the time of food intake
   Parameters
   meal: str
   kitchen: str
   time: str

   функция для пополнения базы данных продуктов по характеристикам кухня и время приема пищи
   Параметры
   характеристики: meal, kitchen, time --> строковые
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
    function of delete the product from the database
    Parameter
    product: str
    parameter product, that is being deleted from the database
    функция удаления продукт из базы данных
    Параметр
    product: строковый
    параметр продукт, по которому происходит удаление из базы данных
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
    function of deleting a recipe from the database
    Parameter
    meal: str
    parameter meal, that is being deleted from the database

    функция удаления рецепта из базы данных
    Параметр
    meal: строковый
    параметр блюдо, по которому происходит удаление из базы данных
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

