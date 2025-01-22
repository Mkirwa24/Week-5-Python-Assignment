# Week-5-Python-Assignment

# Assignment 1: Design Your Own Class! 🏗️
1. Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).

2. Add attributes and methods to bring the class to life!.

3. Use constructors to initialize each object with unique values.

4. Add an inheritance layer to explore polymorphism or encapsulation.

# Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


## Assignment 1 (Smartphone Example) focuses on Encapsulation & Inheritance.

## Activity 2 (Vehicles Example) demonstrates Polymorphism with different implementations of the same method.


# Assignment 1: Design Your Own Class
This activity involves creating a class that represents an object of one's choice (e.g., a Smartphone, Book, or Superhero). For this case Class (Smartphone) is used and defined.

You must add attributes (data) and methods (functions) to define the class’s behavior.

## Concepts Used:
1. Class & Object Creation - A class (Smartphone) is defined and objects are created from it.

2. Encapsulation - The battery is marked private (__battery), preventing direct modification from outside the class.

3. Methods - Actions like make_call(), charge(), and battery_status() control behavior.

4. Inheritance - AdvancedSmartphone extends Smartphone by adding a take_photo() method.


# Activity 2: Polymorphism Challenge (Vehicles Moving Differently)
Polymorphism allows different objects to respond uniquely to the same method.

## Concepts Used:
1. Base Class & Subclasses - A generic Vehicle class is created, and Car, Plane, and Boat inherit from it.

2. Method Overriding - Each subclass redefines the move() method differently.

3. Polymorphism - A loop has been used to call move() on different vehicle objects, and they behave differently based on their class.