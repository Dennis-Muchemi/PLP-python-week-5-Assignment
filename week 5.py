#Question 1: Design Your Own Class! 🏗️
# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Display vehicle information."""
        return f"{self.year} {self.brand} {self.model}"

# Subclass: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, seats):
        # Call the parent class constructor
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.seats = seats

    def honk(self):
        """Car-specific method."""
        print(f"{self.display_info()} says 'Beep beep!'")

    def display_info(self):
        """Override to include car-specific details."""
        basic_info = super().display_info()
        return f"{basic_info}, Fuel: {self.fuel_type}, Seats: {self.seats}"

# Main program
if __name__ == "__main__":
    # Create a Car instance
    my_car = Car("Toyota", "Camry", 2023, "Gasoline", 5)
    
    # Display car details
    print(my_car.display_info())
    
    # Call the unique method
    my_car.honk()


#Question 2: Polymorphism Challenge! 🎭
# Base class: Animal
class Animal:
    def move(self):
        """Default move behavior."""
        print("This animal moves in its own way.")

# Subclass: Dog
class Dog(Animal):
    def move(self):
        """Dog-specific move method."""
        print("The dog is running. 🐕")

# Subclass: Bird
class Bird(Animal):
    def move(self):
        """Bird-specific move method."""
        print("The bird is flying. 🐦")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        """Fish-specific move method."""
        print("The fish is swimming. 🐟")

# Function to demonstrate polymorphism
def demonstrate_movement(animal):
    animal.move()

# Main program
if __name__ == "__main__":
    # Create instances of each class
    dog = Dog()
    bird = Bird()
    fish = Fish()
    
    # Demonstrate polymorphism
    print("--- Animal Movements ---")
    for animal in [dog, bird, fish]:
        demonstrate_movement(animal)
