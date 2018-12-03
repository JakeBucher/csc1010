# 9-1. Restaurant: Make a class called Restaurant .
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type .
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open .
# Make an instance called restaurant from your class .
# Print the two attributes individually, and then call both methods .

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the pizza lovers', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1 .
# Create three different instances from the class, and call describe_restaurant() for each instance .

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

the_pizza_lovers = Restaurant('the pizza lovers', 'pizza')
the_pizza_lovers.describe_restaurant()

captain_jack = Restaurant("captain jack buffet", 'seafood')
captain_jack.describe_restaurant()

apple_everything = Restaurant('apple everything', 'apple flavored food')
apple_everything.describe_restaurant()

# 9-3. Users: Make a class called User .
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile .
# Make a method called describe_user() that prints a summary of the user’s information .
# Make another method called greet_user() that prints a personalized greeting to the user .
# Create several instances representing different users, and call both methods for each user .

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

albert = User('albert', 'cambell', 'fat_albert', 'heyheyheyitsfatalbert@yahoo.com', 'hollywood')
albert.describe_user()
albert.greet_user()

willie = User('willie', 'silly', 'willie_silly', 'sillywillie@yahoo.com', 'Washington')
willie.describe_user()
willie.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166) .
# Add an attribute called number_served with a default value of 0 .
# Create an instance called restaurant from this class .
# Print the number of customers the restaurant has served, and then change this value and print it again .
# Add a method called set_number_served() that lets you set the number of customers that have been served .
# Call this method with a new number and print the value again .
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served .
# Call this method with any number you like that could represent,
# how many customers were served in, say, a day of business

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant('the pizza lovers', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1543)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(465)
print("Number served: " + str(restaurant.number_served))

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166) .
# Write a method called increment_ login_attempts() that increments the value of login_attempts by 1 .
# Write another method called reset_login_attempts() that resets the value of login_ attempts to 0 .
# Make an instance of the User class and call increment_login_attempts() several times .
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts() .
# Print login_attempts again to make sure it was reset to 0 .

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

willie = User('willie', 'silly', 'willie_silly', 'sillywillie@yahoo.com', 'Washington')
willie.describe_user()
willie.greet_user()

print("\nMaking 3 login attempts...")
willie.increment_login_attempts()
willie.increment_login_attempts()
willie.increment_login_attempts()
print("  Login attempts: " + str(willie.login_attempts))

print("Resetting login attempts...")
willie.reset_login_attempts()
print("  Login attempts: " + str(willie.login_attempts))

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166),
# or Exercise 9-4 (page 171) . Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors . Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


creamy_sensation = IceCreamStand('Creamy Sensation')
creamy_sensation.flavors = ['vanilla', 'chocolate', 'banana']

creamy_sensation.describe_restaurant()
creamy_sensation.show_flavors()

# 9-7. Admin: An administrator is a special kind of user .
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166),
# or Exercise 9-5 (page 171) .
# Add an attribute, privileges, that stores a list of strings like "can add post",
# "can delete post", "can ban user", and so on . Write a method called show_privileges() that lists,
# the administrator’s set of privileges . Create an instance of Admin, and call your method .

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


willie = Admin('willie', 'silly', 'willie_silly', 'sillywillie@yahoo.com', 'Washington')
willie.describe_user()

willie.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

willie.show_privileges()

# 9-8. Privileges: Write a separate Privileges class .
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7 .
# Move the show_privileges() method to this class . Make a Privileges instance as an attribute in the Admin class .
# Create a new instance of Admin and use your method to show its privileges .

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


willie = Admin('willie', 'silly', 'willie_silly', 'sillywillie@yahoo.com', 'Washington')
willie.describe_user()

willie.privileges.show_privileges()

print("\nAdding privileges...")
willie_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
willie.privileges.privileges = willie_privileges
willie.privileges.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section .
# Add a method to the Battery class called upgrade_battery() .
# This method should check the battery size and set the capacity to 85 if it isn’t already .
# Make an electric car with a default battery size, call get_range() once,
# and then call get_range() a second time after upgrading the battery .
# You should see an increase in the car’s range .

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model 3', 2017)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module .
# Make a separate file that imports Restaurant .
# Make a Restaurant instance, and call one of Restaurant’s methods,
# to show that the import statement is working properly .

"""A class representing a restaurant."""

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


clubhouse_club = Restaurant('the clubhouse club', 'steak and seafood')
clubhouse_club.describe_restaurant()
clubhouse_club.open_restaurant()

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178) .
# Store the classes User, Privileges, and Admin in one module .
# Create a separate file, make an Admin instance,
# and call show_privileges() to show that everything is working correctly .

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])


class Privileges():
    """Stores privileges associated with an Admin account."""

    def __init__(self, privileges):
        """Initialize the privileges object."""
        self.privilege = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        for privilege in self.privileges:
            print("- " + privilege)

willie = Admin('willie', 'silly', 'willie_silly', 'sillywillie@yahoo.com', 'Washington')
willie.describe_user()

willie_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
willie.privileges.privileges = willie_privileges

print("\nThe admin " + willie.username + " has these privileges: ")
willie.privileges.show_privileges()

# 9-12. Multiple Modules:
# Store the User class in one module, and store the Privileges and Admin classes in a separate module .
# In a separate file,
# create an Admin instance and call show_privileges() to show that everything is still working correctly .

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])


class Privileges():
    """Stores privileges associated with an Admin account."""

    def __init__(self, privileges):
        """Initialize the privileges object."""
        self.privilege = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        for privilege in self.privileges:
            print("- " + privilege)

albert = Admin('albert', 'cambell', 'fat_albert', 'heyheyheyitsfatalbert@yahoo.com', 'hollywood')
albert.describe_user()

albert_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
albert.privileges.privileges = albert_privileges

print("\nThe admin " + albert.username + " has these privileges: ")
albert.privileges.show_privileges()

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108),
# where you used a standard dictionary to represent a glossary .
# Rewrite the program using the OrderedDict class and make sure the order of the output matches the order,
# in which key-value pairs were added to the dictionary .

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

# 9-14. Dice: The module random contains functions that generate random numbers in a variety of ways .
# The function randint() returns an integer in the range you provide .
# The following code returns a number between 1 and 6:
# from random import randint x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default value of 6 .
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has .
# Make a 6-sided die and roll it 10 times .

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)