import unittest
from chef_assistant import choose
from database import refill_recipe_database, refill_product_database, refill_characteristic_database, delete_product, delete_recipe

class sumsTest(unittest.TestCase):
    """
    test function checks for the presence of all ingredients and all are mandatory\n
    тест функция проверяет на наличие всех ингредиентов и все являются обязательными
    """
    def test_1(self):
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Лунная каша", "Инопланетянская", "Обед")
        refill_recipe_database("Лунная каша", [["Лунитка", "0.02", "кг", "Обязательно"], ["Вода с Марса", "0.01", "кг", "Обязательно"]])
        refill_product_database("Лунитка", "1000000", "кг")
        refill_product_database("Вода с Марса", "500000", "кг")
        self.assertEqual(choose("Инопланетянская", "Обед", "12"), "Лунная каша (FULL)")
        db.remove(where('Блюдо') == 'Лунная каша')
        db_1.remove(where('Продукт') == 'Лунитка')
        db_1.remove(where('Продукт') == 'Вода с Марса')
        db_2.remove(where('Блюдо') == 'Лунная каша')
        db.close()
        db_1.close()
        db_2.close()

    def test_2(self):
        """
        test function with a lack of a sufficient amount of an optional ingredient\n
        тест функция с отсутствием достаточного количества необязательного ингредиента
        """
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Пирог из космической пыли", "Галактическая", "Завтрак Ужин")
        refill_recipe_database("Пирог из космической пыли", [["Пыль космическая", "0.12", "мг", "Обязательно"], ["Сок гибискуса", "0.1", "кг", "Необязательно"]])
        refill_product_database("Пыль космическая", "1000000", "мг")
        refill_product_database("Сок гибискуса", "0.1", "кг")
        self.assertEqual(choose("Галактическая", "Ужин", "2"), "Пирог из космической пыли (PART) Trouble:Сок гибискуса")
        db.remove(where('Блюдо') == 'Пирог из космической пыли')
        db_1.remove(where('Продукт') == 'Пыль космическая')
        db_1.remove(where('Продукт') == 'Сок гибискуса')
        db_2.remove(where('Блюдо') == 'Пирог из космической пыли')
        db.close()
        db_1.close()
        db_2.close()

    def test_3(self):
        """
        test function with lack of sufficient required ingredient\n
        тест функция с отсутствием достаточного количества обязательного ингредиента
        """
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Астероидный коктейль", "Солнечно-системная", "Обед")
        refill_recipe_database("Астероидный коктейль", [["Углеродная смесь", "0.3", "т", "Обязательно"],
                                                      ["Лёд", "1", "т", "Необязательно"]])
        refill_product_database("Углеродная смесь", "3", "т")
        refill_product_database("Лёд", "1000", "т")
        self.assertEqual(choose("Солнечно-системная", "Обед", "11"), "Блюд не найдено!\nПополните склад и \nвнесите новые рецепты в базу.")
        db.remove(where('Блюдо') == 'Астероидный коктейль')
        db_1.remove(where('Продукт') == 'Углеродная смесь')
        db_1.remove(where('Продукт') == 'Лёд')
        db_2.remove(where('Блюдо') == 'Астероидный коктейль')
        db.close()
        db_1.close()
        db_2.close()

    def test_4(self):
        """
        test function with the absence of a mandatory ingredient in the product database\n
        тест функция с отсутствием обязательного ингредиента в базе данных продуктов
        """
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Латунья Сатурнская", "Галактическая", "Завтрак Обед Ужин")
        refill_recipe_database("Латунья Сатурнская", [["Грунт сатурнский", "0.2", "г", "Обязательно"], ["Лёд сатурнский", "1", "кг", "Обязательно"]])
        refill_product_database("Грунт сатурнский", "55", "г")
        self.assertEqual(choose("Галактическая", "Обед", "12"), "Блюд не найдено!\nПополните склад и \nвнесите новые рецепты в базу.")
        db.remove(where('Блюдо') == 'Латунья Сатурнская')
        db_1.remove(where('Продукт') == 'Грунт сатурнский')
        db_2.remove(where('Блюдо') == 'Латунья Сатурнская')
        db.close()
        db_1.close()
        db_2.close()

    def test_5(self):
        """
        test function with the absence of an optional ingredient in the product database\n
        тест функция с отсутствием необязательного ингредиента в базе данных продуктов
        """
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Глинтвейн Чёрная дыра", "Орбитная", "Завтрак")
        refill_recipe_database("Глинтвейн Чёрная дыра", [["Чёрная материя", "3", "л", "Обязательно"], ["Струна космическая", "0.1", "г", "Обязательно"], ["Листик мяты", "2", "шт", "Необязательно"]])
        refill_product_database("Чёрная материя", "97.5", "л")
        refill_product_database("Струна космическая", "14", "г")
        self.assertEqual(choose("Орбитная", "Завтрак", "11"), "Глинтвейн Чёрная дыра (PART) Trouble:Листик мяты")
        db.remove(where('Блюдо') == 'Глинтвейн Чёрная дыра')
        db_1.remove(where('Продукт') == 'Чёрная материя')
        db_1.remove(where('Продукт') == 'Струна космическая')
        db_2.remove(where('Блюдо') == 'Глинтвейн Чёрная дыра')
        db.close()
        db_1.close()
        db_2.close()

    def test_6(self):
        """
        test function of checking the possibility of adding and removing an ingredient\n
        тест функция проверки возможно добавления и удаления ингридиента
        """
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Звёздный пломбир", "Галактическая", "Завтрак Обед Ужин")
        refill_recipe_database("Звёздный пломбир", [["Солнечный ветер", "0.2", "г", "Обязательно"]])
        refill_product_database("Солнечный ветер", "97.5", "г")
        delete_product("Солнечный ветер")
        self.assertEqual(choose("Галактическая", "Ужин", "1"), "Блюд не найдено!\nПополните склад и \nвнесите новые рецепты в базу.")
        delete_recipe("Звёздный пломбир")
        db.close()
        db_1.close()
        db_2.close()

    def test_7(self):
        """
        test function of checking the possibility of adding and removing a recipe\n
        тест функция проверки возможно добавления и удаления рецепта
        """
        import tinydb
        from tinydb import TinyDB, Query, where
        db = tinydb.TinyDB('recipes.db')
        db_1 = tinydb.TinyDB('products.db')
        db_2 = tinydb.TinyDB('characteristic.db')
        refill_characteristic_database("Желе Планета", "Планетарная", "Завтрак Ужин")
        refill_recipe_database("Желе Планета", [["Хвост кометы", "200", "г", "Необязательно"]])
        refill_product_database("Хвост кометы", "9700", "г")
        delete_recipe("Желе Планета")
        self.assertEqual(choose("Планетарная", "Ужин", "14"), "Блюд не найдено!\nПополните склад и \nвнесите новые рецепты в базу.")
        delete_product("Хвост кометы")
        db.close()
        db_1.close()
        db_2.close()

if __name__ == "__main__":
    unittest.main()
