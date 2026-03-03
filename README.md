# Hangman
# Python Hangman Game 🎮

A classic **Hangman** game implemented in Python. Test your vocabulary by guessing the hidden word before the gallows are complete!

📝 Game Rules

The game displays underscores _ representing each letter of the hidden word.
Input one letter at a time.
Correct guess: The letter reveals its position in the word.
Wrong guess: A part of the hangman is drawn. You have 7 lives in total.
Duplicate guess: A warning is shown, but no lives are lost.
Win by guessing all letters, or lose if the hangman is fully displayed!

🤝 Contributing

Contributions are welcome! If you'd like to add new features (like difficulty levels or a score system), feel free to fork the repo and submit a pull request.

⭐ If you liked this project, feel free to give it a star!

## 🚀 Features
- **Random Word Selection:** Automatically picks a challenge from a predefined word list.
- **ASCII Art Visuals:** Displays the hangman status dynamically using ASCII graphics.
- **Smart Validation:** Detects duplicate guesses so you don't lose lives for the same mistake twice.
- **Clean UI:** Utilizes terminal clearing after each input to keep the game interface neat and readable.

## 🛠 Prerequisites
To run this game, ensure you have the following file in the same directory:
- `hangman_art.py`: Contains the `words` list and the `HANGMANPICS` list.

## 📂 Project Structure
- `main.py`: The core game logic and loop.
- `hangman_art.py`: Graphics and word database.

If you found this helpful, consider giving it a ⭐!

## 🕹 How to Play
1. Clone this repository:
   ```bash
   git clone https://github.com
