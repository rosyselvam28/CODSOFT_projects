# CODSOFT - Recommendation System

movies = {
    "action": ["Avengers", "John Wick", "Batman"],
    "comedy": ["3 Idiots", "Jumanji", "Mr. Bean"],
    "horror": ["The Conjuring", "Annabelle", "Insidious"],
    "romance": ["Titanic", "The Notebook", "La La Land"],
    "science fiction": ["Interstellar", "Inception", "The Martian"]
}

print("========== Movie Recommendation System ==========")

while True:

    print("\nAvailable Categories:")

    for category in movies:
        print("-", category.title())

    choice = input(
        "\nEnter your favourite category (or type 'exit'): "
    ).strip().lower()

    if choice == "exit":
        print("\nThank you for using the Recommendation System.")
        break

    elif choice in movies:

        print("\nRecommended Movies:")

        for movie in movies[choice]:
            print("•", movie)

    else:
        print("\nInvalid category.")

        print("Please choose from the available categories.")