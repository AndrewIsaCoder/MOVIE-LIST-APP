import pickle
import os


# Class for movies
class Movie:
    def __init__(self, title, release_year, genre, imdb_url):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.imdb_url = imdb_url

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Release Year: {self.release_year}\n"
                f"Genre: {self.genre}\n"
                f"IMDB URL: {self.imdb_url}\n")


# Function to load movies (deserialization)
def load_movies():
    if os.path.exists("movies.pkl"):
        with open("movies.pkl", "rb") as file:
            return pickle.load(file)
    return []


# Function to save movies (serialization)
def save_movies(movies):
    with open("movies.pkl", "wb") as file:
        pickle.dump(movies, file)


# Function to add a movie
def add_movie(movies):
    print("\n-------------ADD A NEW MOVIE-------------")
    title = input("Title: ")
    release_year = int(input("Release Year: "))
    genre = input("Genre: ")
    imdb_url = input("IMDB URL: ")

    movie = Movie(title, release_year, genre, imdb_url)
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully!\n")


# Function to view all movies
def view_movies(movies):
    print("\n-------------VIEW ALL MOVIES-------------")
    if not movies:
        print("No movies available!")
    else:
        for movie in movies:
            print(movie)


# Main function to run the application
def main():
    movies = load_movies()

    while True:
        print("-------------MAIN MENU-------------")
        print("1. ADD A NEW MOVIE")
        print("2. VIEW ALL MOVIES")
        print("3. EXIT")
        choice = input("Please choose 1, 2, or 3: ")

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            print("Thank you for using the Movie App!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == '__main__':
    main()