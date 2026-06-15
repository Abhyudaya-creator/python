# def greet():
#     print("Hello, World!")
#     print("Welcome to the program.")

# greet()

# def greetwithname(name, location):
#     print(f"hello {name}")
#     print(f"welcome to {location}")

# greetwithname(location="Ayodhya", name="Abhi")

def calculate_love_score(name1, name2):
    combinednames = (name1 + name2).lower()

    true_score = (
        combinednames.count("t") +
        combinednames.count("r") +
        combinednames.count("u") +
        combinednames.count("e")
    )

    love_score = (
        combinednames.count("l") +
        combinednames.count("o") +
        combinednames.count("v") +
        combinednames.count("e")
    )

    score = int(str(true_score) + str(love_score))
    print(score)
