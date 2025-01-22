# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # Private attribute (Encapsulation)

    def make_call(self, number):
        if self.__battery > 0:
            print(f"Calling {number} from {self.brand} {self.model} 📞")
            self.__battery -= 10  # Battery decreases on call
        else:
            print("Battery empty! Please charge your phone.")

    def charge(self):
        self.__battery = 100
        print(f"{self.brand} {self.model} is now fully charged! 🔋")

    def battery_status(self):
        print(f"Battery level: {self.__battery}%")

# Derived class: AdvancedSmartphone (Inheritance)
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery, camera_mp):
        super().__init__(brand, model, battery)
        self.camera_mp = camera_mp

    def take_photo(self):
        print(f"📸 Taking a photo with {self.camera_mp}MP camera on {self.brand} {self.model}")

# Creating instances
phone1 = Smartphone("Samsung", "Galaxy S21", 50)
phone2 = AdvancedSmartphone("Apple", "iPhone 14", 80, 48)

# Using methods
phone1.make_call("0712345678")
phone1.battery_status()
phone2.take_photo()
phone2.charge()
