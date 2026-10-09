# =============================================================================
# OOP (Object-Oriented Programming) basics in Python
# Four ideas you will see below: classes/objects, encapsulation, inheritance,
# polymorphism, and abstraction.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. CLASS AND OBJECT
# -----------------------------------------------------------------------------
# A class is a blueprint; an object is one real "thing" built from that blueprint.
# `self` means "this particular object" inside the class.
# `__init__` runs automatically when you create a new object (constructor).

class Car:
    # Constructor: runs when you call Car("Toyota", "Corolla", 2020)
    def __init__(self, brand, model, year):
        # Store values on this object so other methods can use them later
        self.brand = brand      # instance attribute (unique per car)
        self.model = model
        self.year = year

    # Instance methods: first parameter is always `self` (the current Car object)
    def start(self):
        return f"The {self.brand} {self.model} is starting."

    def stop(self):
        return f"The {self.brand} {self.model} is stopping."

    def drive(self):
        return f"The {self.brand} {self.model} is driving."

    def refuel(self):
        return f"The {self.brand} {self.model} is refueling."

    def park(self):
        return f"The {self.brand} {self.model} is parking."


# Create one object (instance) of class Car
my_car = Car("Toyota", "Corolla", 2020)
# Call methods on that object; each call uses my_car's brand/model/year
print(my_car.start())
print(my_car.stop())
print(my_car.drive())
print(my_car.refuel())
print(my_car.park())

# -----------------------------------------------------------------------------
# 2. ENCAPSULATION
# -----------------------------------------------------------------------------
# Hide sensitive data and control how it is read or changed.
# `__balance` (double underscore) is "name-mangled" — harder to access from outside
# by accident; use methods like deposit() and get_balance() instead.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # public attribute (OK to read from outside)
        self.__balance = balance     # "private" by convention (encapsulation)

    def get_balance(self):
        # Controlled way to see balance without touching __balance directly
        return f"Account Holder: {self.owner}. Current Balance: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:               # validation before changing internal state
            self.__balance += amount
            return f"Account Holder: {self.owner}. {amount} deposited successfully."
        return "Invalid amount!"


account = BankAccount("Asad", 1000)   # open account with 1000 balance
print(account.deposit(500))           # add 500 if amount is valid
print(account.get_balance())          # show owner name and updated balance

# -----------------------------------------------------------------------------
# 3. INHERITANCE
# -----------------------------------------------------------------------------
# Child class gets attributes and methods from parent class.
# Developer IS-A Employee, plus extra skills (programming_language, code()).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# Developer inherits from Employee — parentheses mean "extends Employee"
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Run parent's __init__ first so name and salary are set on self
        super().__init__(name, salary)
        # Extra attribute only Developers need
        self.programming_language = programming_language

    # New method only on Developer (Employee does not have code())
    def code(self):
        return f"{self.name} {self.programming_language} mein code kar raha hai."


dev = Developer("Asad", 25000, "Python")  # create a Developer object
print(dev.get_details())                  # inherited from Employee
print(dev.code())                           # defined on Developer

# -----------------------------------------------------------------------------
# 4. POLYMORPHISM ("many forms")
# -----------------------------------------------------------------------------
# Same method name `sound()`, different behavior in Dog vs Cat.
# Code that calls animal.sound() can work with any subclass of Animal.

class Animal:
    def sound(self):
        return "Animal sound"   # generic default (parent implementation)


class Dog(Animal):              # Dog is a kind of Animal
    def sound(self):            # override parent's sound()
        return "Woof"


class Cat(Animal):
    def sound(self):            # override again with Cat's behavior
        return "Meow"


dog = Dog()                     # no __init__ needed — uses Animal's default
cat = Cat()
print(dog.sound())              # uses Dog's version → Woof
print(cat.sound())              # uses Cat's version → Meow

# -----------------------------------------------------------------------------
# 5. ABSTRACTION
# -----------------------------------------------------------------------------
# Abstract class defines WHAT subclasses must do, not full payment logic here.
# You cannot create PaymentGateway() directly — only concrete classes like PayPal.

from abc import ABC, abstractmethod

# ABC = Abstract Base Class; marks this as a template for payment providers
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        # Subclass MUST implement pay(); `pass` is a placeholder in the base class
        pass # placeholder for pay method

    @abstractmethod
    def refund(self, amount):
        # Subclass MUST implement refund() too
        pass # placeholder for refund method


# Concrete class: full implementation of every abstract method
class PayPal(PaymentGateway):
    def pay(self, amount):
        return f"Amount Paid: ${amount} by PayPal."

    def refund(self, amount):
        return f"Amount Refunded: ${amount} by PayPal."


class Stripe(PaymentGateway):
    def pay(self, amount):
        return f"Amount Paid: ${amount} by Stripe."

    def refund(self, amount):
        return f"Amount Refunded: ${amount} by Stripe."


payment1 = PayPal()             # object that follows PaymentGateway contract
payment2 = Stripe()

# Same methods pay() on both objects — different strings (like polymorphism)
print(payment1.pay(100))
print(payment2.pay(250))
print(payment1.refund(50))
print(payment2.refund(100))