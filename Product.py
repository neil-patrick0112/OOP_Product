class Product: # Product class manages inventory and product details
    inventory = []  # This is a List to store all products
    product_counter = 1  # This is a counter to auto-generate product IDs

    def __init__(self, name, category, quantity, price, supplier):
        self.product_id = Product.product_counter  
        Product.product_counter += 1
        self.name, self.category, self.quantity, self.price, self.supplier = name, category, quantity, price, supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier): # This adds a new product to the inventory
        
        product = cls(name, category, quantity, price, supplier)
        cls.inventory.append(product)
        return "Product added successfully"
    
    @classmethod
    def update_product(cls, product_id, quantity = 0, price = 0, supplier = 0): # This updates product details based on product_id

        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity != 0:
                    product.quantity = quantity
                if price != 0:
                    product.price = price
                if supplier != 0:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"
    
    @classmethod
    def delete_product(cls, product_id): # This deletes a product from the inventory by product_id
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"


class Order: # The Order class manages customer orders
    def __init__(self, order_id, product_id, quantity, customer_info):
        self.order_id, self.product_id, self.quantity, self.customer_info = order_id, product_id, quantity, customer_info

    def place_order(self):
        return f"Order placed successfully. Order ID: {self.order_id}" # Places the order and returns a confirmation message

# Sample calling of code to demonstrate functionality
print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
