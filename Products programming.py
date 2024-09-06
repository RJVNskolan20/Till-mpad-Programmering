class product: 
    def __init__(self):
       self.products = [
            {
            "name": "Mobiltelefon",
            "desc": "en fin mobil",
            "price": 100000,
            "quantity": 2 
        },
        {
             "name": "Dator",
             "desc": "en fin dator",
             "price": 200000, 
             "quantity": 2
        }
        ] 
           
    
    def check_inventory(self):
          return self.products
    
get_products = product()
products = get_products.check_inventory()


def list_inventory():
    for i in range(products):
        print(products[i]["name"])

list_inventory()

def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to inventory.")

def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from inventory.")
                return
        print(f"Product '{product_name}' not found in inventory.")

def save_to_file(self, filename):
        with open(filename, 'w') as file:
            if not self.items:
                file.write("Inventory is empty.\n")
            else:
                file.write("Current Inventory:\n")
                for item in self.items:
                    file.write(f"{item}\n")
        print(f"Inventory saved to {filename}.")
     
       