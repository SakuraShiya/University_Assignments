# Write a Python Program To Create a Class To Implement Method Overriding.

from typing import override

class Parent:
    """ Base Class With a Method That The Child Class Overrides """

    def display(self) -> str:
        return "This Is The Parent Class."

class Child(Parent):
    """ Child Class That Replaces display() But Can Still Reach The Parent Version Through super() """

    @override
    def display(self) -> str:
        return "This Is The Child Class."

    def parent_display(self) -> str:
        return super().display()

def main() -> None:
    parent = Parent()
    child = Child()

    print(f"Parent Object Calls display() : {parent.display()}")
    print(f"Child Object Calls display() : {child.display()}")
    print(f"Child Object Calls The Parent Version Using super() : {child.parent_display()}")

    print()
    print("Same Method Call On Both Objects (Polymorphism) :")
    for item in (parent, child):
        print(f"{type(item).__name__} : {item.display()}")

if __name__ == "__main__":
    main()
