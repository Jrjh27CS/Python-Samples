cars = 100 # Defining variable cars with integer 100
space_in_a_car = 4.0 # Defining variable with float
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # Defining variable with math
cars_driven = drivers # Defining variable with another variable
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.") # Printing variable inside of a string
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
