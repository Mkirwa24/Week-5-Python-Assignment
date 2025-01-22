# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder method for polymorphism

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on water")

# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for vehicle in vehicles:
    vehicle.move()
