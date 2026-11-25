from movies import add_movie, show_movies
from halls import add_hall




while True:
    print("1. Add a movie")
    print("2. Show all movies")
    print("3. Add a hall")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie(movies)
    elif choice == "2":
        show_movies(movies)
    elif choice == "3":
        add_hall(halls)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")