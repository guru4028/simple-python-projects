class phone():
    chargertype = "C-Type"
    
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display(self):
        print("brand: ", self.brand)
        print("price:  ", self.price)

samsung = phone("samsung","15000")
samsung.display
