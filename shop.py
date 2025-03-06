class ShoppingCart:
    def __init__(self):
   
        self.items = {}
        self.discount = 0.0  
    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
  
        if product_name in self.items:
            return False

        if quantity <= 0 or price < 0:
            return False

        self.items[product_name] = {
            "price": price,
            "quantity": quantity
        }
        return True

    def remove_product(self, product_name: str) -> bool:
    
        if product_name in self.items:
            del self.items[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
     
        if product_name not in self.items:
            return False
        if new_quantity <= 0:
            return False  

        self.items[product_name]["quantity"] = new_quantity
        return True

    def get_products(self):
       
        return list(self.items.keys())

    def count_products(self) -> int:
      
        total_count = 0
        for product_data in self.items.values():
            total_count += product_data["quantity"]
        return total_count

    def get_total_price(self) -> int:
       
        total = 0
        for product_data in self.items.values():
            total += product_data["price"] * product_data["quantity"]

        if self.discount > 0.0:
            total = int(total * (1.0 - self.discount))

        return total

    def apply_discount_code(self, discount_code: str) -> bool:
      
        discount_codes = {
            "DISCOUNT10": 0.10,
            "DISCOUNT20": 0.20,
            "DISCOUNT50": 0.50
        }

        if discount_code in discount_codes:
            self.discount = discount_codes[discount_code]
            return True

        return False

    def checkout(self) -> bool:
       
        if not self.items:
            return False

        self.items.clear()
        self.discount = 0.0
        return True