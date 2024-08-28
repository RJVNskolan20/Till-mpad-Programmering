import os 

class car:  #en klass har alltid stor bokstav 
    def  __init__ (self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def view_cars(self):
        return f"{self.make} - {self.model} ({self.color})"


os.system("cls") 

cars = [] #lista

cars.append(car("Toyota", "corolla", "Orange"))
cars.append(car("BMW", "M8", "Teal"))
cars.append(car("Audi", "A5", "Blue"))

for car in cars : 
    print(car.view_cars()) 

def display_cars(cars_list):
    if not cars_list:
        print("Inga bilar tillgängliga.")
    else:
        for car in cars_list:
            print(car.view_car())

while True: 
      print("\nADD A CAR")
      make = input("Enter make: ")
      model = input("Enter model: ")
      color = input("Enter color (Type nothing to quit): ")

      if color == "":
        break 

     # Create a new car instance and add it to the list 
        Cars.append(Car(make, model, color))

     # View all cars added 
        display_cars()