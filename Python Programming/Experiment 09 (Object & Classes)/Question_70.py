# Write a Python Program To Implement Different Types Of Inheritance Using Classes.

class Vehicle:
    """ Base Class For Single Inheritance """

    def vehicle_method(self) -> str:
        return "This Is The Vehicle Method (Base Class)."

class Car(Vehicle):
    """ Single Inheritance : One Child (Car) Inherits From One Parent (Vehicle) """

    def car_method(self) -> str:
        return "This Is The Car Method."

class Grandparent:
    """ Top Level Class For Multilevel Inheritance """

    def grandparent_method(self) -> str:
        return "This Is The Grandparent Method."

class Parent(Grandparent):
    """ Middle Level Class, Which Is Both a Child & a Parent """

    def parent_method(self) -> str:
        return "This Is The Parent Method."

class Child(Parent):
    """ Multilevel Inheritance : Child Inherits From Parent, Which Inherits From Grandparent """

    def child_method(self) -> str:
        return "This Is The Child Method."

class Shape:
    """ Common Parent For Hierarchical Inheritance """

    def shape_method(self) -> str:
        return "This Is The Shape Method (Shared Parent)."

class Circle(Shape):
    """ Hierarchical Inheritance : First Child Of Shape """

    def circle_method(self) -> str:
        return "This Is The Circle Method."

class Square(Shape):
    """ Hierarchical Inheritance : Second Child Of Shape """

    def square_method(self) -> str:
        return "This Is The Square Method."

class Father:
    """ First Parent For Multiple Inheritance """

    def father_method(self) -> str:
        return "This Is The Father Method."

class Mother:
    """ Second Parent For Multiple Inheritance """

    def mother_method(self) -> str:
        return "This Is The Mother Method."

class Son(Father, Mother):
    """ Multiple Inheritance : One Child Inherits From Two Parents """

    def son_method(self) -> str:
        return "This Is The Son Method."

class Animal:
    """ Base Class For Hybrid Inheritance """

    def animal_method(self) -> str:
        return "This Is The Animal Method (Base Class)."

class Mammal(Animal):
    """ Hierarchical Part Of The Hybrid : First Child Of Animal """

    def mammal_method(self) -> str:
        return "This Is The Mammal Method."

class Bird(Animal):
    """ Hierarchical Part Of The Hybrid : Second Child Of Animal """

    def bird_method(self) -> str:
        return "This Is The Bird Method."

class Bat(Mammal, Bird):
    """ Hybrid Inheritance : Multiple Inheritance From Mammal & Bird, Which Share The Animal Base """

    def bat_method(self) -> str:
        return "This Is The Bat Method."

def main() -> None:
    car = Car()
    print("Single Inheritance (Vehicle -> Car) :")
    print(car.vehicle_method())
    print(car.car_method())

    child = Child()
    print()
    print("Multilevel Inheritance (Grandparent -> Parent -> Child) :")
    print(child.grandparent_method())
    print(child.parent_method())
    print(child.child_method())

    circle = Circle()
    square = Square()
    print()
    print("Hierarchical Inheritance (Shape -> Circle & Square) :")
    print(circle.shape_method())
    print(circle.circle_method())
    print(square.shape_method())
    print(square.square_method())

    son = Son()
    print()
    print("Multiple Inheritance (Father & Mother -> Son) :")
    print(son.father_method())
    print(son.mother_method())
    print(son.son_method())

    bat = Bat()
    print()
    print("Hybrid Inheritance (Animal -> Mammal & Bird -> Bat) :")
    print(bat.animal_method())
    print(bat.mammal_method())
    print(bat.bird_method())
    print(bat.bat_method())
    print(f"Method Resolution Order Of Bat : {' -> '.join(cls.__name__ for cls in Bat.__mro__)}")

if __name__ == "__main__":
    main()
