import unittest
from chef_assistant import choose
from database import refill_recipe_database, refill_product_database, refill_characteristic_database

class sumsTest(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()