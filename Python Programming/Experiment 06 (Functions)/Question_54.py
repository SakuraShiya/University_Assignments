# Write a Python Program To Explain Keyword Arguments, Default Arguments & Variable Length Arguments Using Functions.

def greet(name: str, message: str) -> str:
    """ Return a Greeting, Called With Keyword Arguments To Show That Argument Order Does Not Matter """
    return f"{message}, {name}!"

def greet_with_default(name: str, message: str = "Hello") -> str:
    """ Return a Greeting Where The Message Falls Back To a Default Value When Not Given """
    return f"{message}, {name}!"

def greet_everyone(*names: str) -> list[str]:
    """ Return a Greeting For Any Number Of Names Passed As Variable Length Arguments """
    return [f"Hello, {name}!" for name in names]

def describe_student(name: str, **details: str) -> str:
    """ Return a Description Built From Any Number Of Variable Length Keyword Arguments """
    if not details:
        return name

    info = ", ".join(f"{key.title()} : {value}" for key, value in details.items())
    return f"{name} ({info})"

def main() -> None:
    print("Keyword Arguments :")
    print(greet(message="Hello", name="Alice"))

    print()
    print("Default Arguments :")
    print(greet_with_default("Haruto"))
    print(greet_with_default("Anos", "Welcome"))

    print()
    print("Variable Length Arguments (*args) :")
    for greeting in greet_everyone("Aishia", "Akari"):
        print(greeting)

    print()
    print("Variable Length Keyword Arguments (**kwargs) :")
    print(describe_student("Akari", course="B.Tech", semester="3", city="Delhi"))

if __name__ == "__main__":
    main()
