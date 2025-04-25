# 🎬 Watchlist App v1.0

A simple Python console application that helps users keep track of movies they want to watch in the future. This project was created as part of a programming task, focusing on object-oriented programming, data serialization, and user interaction.

## 📌 Features

- ✅ Add a new movie to your watchlist  
- ✅ View all previously added movies  
- ✅ Save movie details permanently using serialization  
- ✅ Simple, menu-driven interface  
- ✅ Runs in the console (terminal)

## 🎥 Movie Details

Each movie includes the following information:

- **Title** – The name of the movie  
- **Release Year** – The year the movie was released  
- **Genre(s)** – One or more genres, separated by commas  
- **IMDB URL** – A link to the movie’s page on IMDb

## 💾 Data Persistence

All movies are saved permanently using Python's `pickle` module. Even after closing the application, your watchlist is preserved and can be viewed the next time you run the program.

## 🧠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Serialization (`pickle` module)
- Console-based input/output

## 🚀 How It Works

1. When the app starts, users are presented with three options:
   - Add a new movie
   - View all movies
   - Exit the program
2. Movie data is entered manually and saved immediately.
3. Users can view all saved movies at any time.
4. The program runs in a loop until the user chooses to exit.

## 🛠 How to Run

1. Make sure you have Python 3 installed.
2. Clone the repository or download the `.zip` file.
3. Open a terminal in the project directory.
4. Run the program with:

```bash
python main.py
