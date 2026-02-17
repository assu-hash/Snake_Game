# Snake_Game
🐍 Snake Game (Python Turtle)

A classic Snake Game built using Python and the Turtle graphics library.
The project is structured into multiple files to keep the code clean, readable, and modular.

📁 Project Structure
snake-game/
│
├── main.py          # Main game loop and controls
├── snake.py         # Snake movement and behavior
├── food.py          # Food generation logic
├── scoreboard.py   # Score and high-score handling
├── data.txt         # Stores the high score
└── README.md

🎮 How the Game Works

The snake moves continuously on the screen

Eat the blue food to:

Increase your score

Grow the snake

The game ends if:

The snake hits the wall

The snake collides with its own body

High score is saved automatically in data.txt

🕹️ Controls
Key	Action
⬆️ Up Arrow	Move Up
⬇️ Down Arrow	Move Down
⬅️ Left Arrow	Move Left
➡️ Right Arrow	Move Right
🧩 Files Explained
main.py

Sets up the game screen

Handles keyboard input

Runs the main game loop

Detects collisions (food, wall, tail)

snake.py

Creates the snake body

Controls movement and direction

Handles snake growth

food.py

Creates food at random positions

Refreshes food after collision

scoreboard.py

Displays current score and high score

Saves high score to data.txt

Shows GAME OVER message

▶️ How to Run the Game
Requirements

Python 3.x (Turtle comes pre-installed)

Run
python main.py

💾 High Score Saving

High score is stored in data.txt

Automatically updates when you beat the previous high score

🚀 Future Improvements (Optional Ideas)

Add sound effects 🎵

Add levels with increasing speed ⚡

Add restart button 🔄

Improve graphics/colors 🎨

🧑‍💻 Author

Created as a Python practice project to learn:

Object-Oriented Programming

Game loops

Collision detection
