import unittest
from shop import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    

    def setUp(self):
       
        self.cart = ShoppingCart()

    def test_add_product_success(self):
     
        result = self.cart.add_product("Apple", 10, 2)
        self.assertTrue(result, "Dodanie nowego produktu powinno zwrócić True.")
        self.assertEqual(len(self.cart.items), 1, "Koszyk powinien zawierać 1 produkt.")
        self.assertIn("Apple", self.cart.items, "Produkt 'Apple' powinien znajdować się w koszyku.")

    def test_add_product_duplicate(self):
        
        self.cart.add_product("Apple", 10, 2)
        result = self.cart.add_product("Apple", 12, 3)  # Ta sama nazwa produktu
        self.assertFalse(result, "Dodanie produktu o tej samej nazwie powinno zwrócić False.")
        self.assertEqual(len(self.cart.items), 1, "W koszyku dalej powinien być tylko 1 produkt (Apple).")

    def test_add_product_invalid_price_or_quantity(self):
      
        result_negative_price = self.cart.add_product("Banana", -5, 3)
        result_zero_quantity = self.cart.add_product("Orange", 10, 0)
        self.assertFalse(result_negative_price, "Dodanie produktu z ujemną ceną powinno zwrócić False.")
        self.assertFalse(result_zero_quantity, "Dodanie produktu z zerową ilością powinno zwrócić False.")
        self.assertEqual(len(self.cart.items), 0, "Koszyk powinien nadal być pusty.")

    def test_remove_product_success(self):
        
        self.cart.add_product("Apple", 10, 2)
        result = self.cart.remove_product("Apple")
        self.assertTrue(result, "Usunięcie istniejącego produktu powinno zwrócić True.")
        self.assertEqual(len(self.cart.items), 0, "Po usunięciu produkt nie powinien znajdować się w koszyku.")

    def test_remove_product_nonexistent(self):
        
        self.cart.add_product("Apple", 10, 2)
        result = self.cart.remove_product("Banana")
        self.assertFalse(result, "Próba usunięcia nieistniejącego produktu powinna zwrócić False.")
        self.assertEqual(len(self.cart.items), 1, "W koszyku wciąż powinien znajdować się produkt 'Apple'.")

    def test_update_quantity_success(self):
        
        self.cart.add_product("Apple", 10, 2)
        result = self.cart.update_quantity("Apple", 5)
        self.assertTrue(result, "Aktualizacja istniejącego produktu powinna zwrócić True.")
        self.assertEqual(self.cart.items["Apple"]["quantity"], 5, "Ilość produktu 'Apple' powinna być zaktualizowana do 5.")

    def test_update_quantity_nonexistent(self):
        
        self.cart.add_product("Apple", 10, 2)
        result = self.cart.update_quantity("Banana", 5)
        self.assertFalse(result, "Aktualizacja nieistniejącego produktu powinna zwrócić False.")
        self.assertNotIn("Banana", self.cart.items, "Produkt 'Banana' nadal nie powinien pojawiać się w koszyku.")

    def test_update_quantity_invalid_value(self):
        
        self.cart.add_product("Apple", 10, 2)
        result_zero = self.cart.update_quantity("Apple", 0)
        self.assertFalse(result_zero, "Ustawienie ilości 0 powinno zwrócić False.")
        self.assertEqual(self.cart.items["Apple"]["quantity"], 2, "Ilość produktu nie powinna się zmienić po nieudanej aktualizacji.")

    def test_get_products(self):
        
        self.cart.add_product("Apple", 10, 2)
        self.cart.add_product("Banana", 5, 5)
        products = self.cart.get_products()
        self.assertEqual(len(products), 2, "Powinny być 2 produkty w koszyku.")
        self.assertIn("Apple", products, "Produkt 'Apple' powinien być na liście.")
        self.assertIn("Banana", products, "Produkt 'Banana' powinien być na liście.")

    def test_count_products(self):
        
        self.cart.add_product("Apple", 10, 2)   # 2 sztuki
        self.cart.add_product("Banana", 5, 5)  # 5 sztuk
        count = self.cart.count_products()
        self.assertEqual(count, 7, "Łączna liczba sztuk w koszyku powinna wynosić 7.")

    def test_get_total_price(self):
        
        self.cart.add_product("Apple", 10, 2)   # 2 * 10 = 20
        self.cart.add_product("Banana", 5, 3)   # 3 * 5 = 15
        total = self.cart.get_total_price()
        self.assertEqual(total, 35, "Łączna cena powinna wynosić 35.")

    def test_apply_discount_code(self):
        
        self.cart.add_product("Apple", 10, 2)   # 2 * 10 = 20
        # Zastosujmy kod DISCOUNT10, który obniża cenę o 10%
        result = self.cart.apply_discount_code("DISCOUNT10")
        self.assertTrue(result, "Prawidłowy kod rabatowy powinien zwrócić True.")
        self.assertAlmostEqual(self.cart.discount, 0.10, places=2, msg="Rabat w koszyku powinien wynosić 0.10 (10%).")

        total_after_discount = self.cart.get_total_price()  # powinno być 2 * 10 = 20, minus 10% -> 18
        self.assertEqual(total_after_discount, 18, "Łączna cena powinna zostać obniżona do 18 po zastosowaniu rabatu.")

    def test_apply_invalid_discount_code(self):
        
        result = self.cart.apply_discount_code("BADCODE")
        self.assertFalse(result, "Niepoprawny kod rabatowy powinien zwrócić False.")
        self.assertEqual(self.cart.discount, 0.0, "Rabat nie powinien się zmienić.")

    def test_checkout_success(self):
        
        self.cart.add_product("Apple", 10, 2)
        self.cart.add_product("Banana", 5, 3)
        result = self.cart.checkout()
        self.assertTrue(result, "Przy pełnym koszyku zamówienie powinno zostać zrealizowane (True).")
        self.assertEqual(len(self.cart.items), 0, "Koszyk powinien zostać wyczyszczony po finalizacji.")
        self.assertEqual(self.cart.discount, 0.0, "Rabat również powinien zostać zresetowany.")

    def test_checkout_empty_cart(self):
        
        result = self.cart.checkout()
        self.assertFalse(result, "Finalizacja pustego koszyka powinna zwracać False.")

    # assertRaises jeżeli klasa ShoppingCart miałaby rzucać wyjątek, np. ValueError
    # W obecnej implementacji ShoppingCart zwraca wartości logiczne, więc ten test jest tylko przykładowy.
    #
    # def test_remove_product_raises(self):
    #     with self.assertRaises(ValueError):
    #         # Załóżmy, że remove_product rzuca ValueError, gdy nie ma takiego produktu
    #         self.cart.remove_product("NonExistentProduct")

    def tearDown(self):
       
        self.cart.items.clear()
        self.cart.discount = 0.0

