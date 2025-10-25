 # SUPER TIC TAC TOE
#### Video Demo:  [https://youtu.be/-AcsThEZinw](https://youtu.be/-AcsThEZinw)
#### Description:
This is a Python-based implementation of **Ultimate Tic Tac Toe**, an advanced version of the classic Tic Tac Toe game. It introduces new strategic depth by embedding 9 individual Tic Tac Toe boards (mini boards) inside a larger 3x3 grid (main board). The goal is to win the overall game by winning mini boards in a pattern that forms a standard Tic Tac Toe victory in the main grid.

This version is fully terminal-based, interactive, and runs directly from the command line with no dependencies beyond Python’s standard library.

---
## 🎮 Gameplay Overview

### 🧩 Rules

- The game consists of **9 mini boards**, numbered 1 through 9, arranged like a 3x3 grid.
- Players take turns making moves as 'X' and 'O'.
- On their turn, a player chooses a position (1–9) within a designated mini board and places their symbol.
- **The twist**: the position you play in determines which mini board your opponent must play in next.
  - For example, if you play in position 5 of mini board 3, your opponent must now play in mini board 5.
- If the destination mini board has already been won or drawn, the opponent may choose any mini board for their move.
- If a player wins a mini board (standard Tic Tac Toe rules), they "claim" that board in the main grid.
- The **main game** is won when a player claims 3 mini boards in a row (row, column, or diagonal) in the overall 3x3 structure.
- If all mini boards are full and no player wins the main game, it results in a **draw**.

---

## 🧪 Features

- ✅ Terminal-based interface
- ✅ Clean visual board display of all 9 mini boards
- ✅ Dynamic board selection and validation
- ✅ Win detection for mini boards and overall game
- ✅ Draw detection
- ✅ Animated feedback using `time.sleep`

---
## ▶️ How to Run

### 1. Requirements

- Python 3.x installed (no external libraries needed)

### 2. Run the Game

```bash
python ultimate_tic_tac_toe.py
```

### Game Flow
- The game starts with an empty board.

- Players are prompted for their move:

- If the required mini board is available, they must play in it.

- Otherwise, they may choose any mini board.

- After every move, the board is updated, and the system checks for mini board wins, main board wins, or draw conditions.

- The game continues until someone wins the main board or all boards are filled (draw).

### Code structure
- printBoard(board): Renders the 9 mini boards in a structured format. Returns None

- checkValidMove(board, movePos): Checks whether a move is legal. Returns boolean True or False

- updateBoard(board, movePos, turn): Updates a mini board with a player's move. Returns None

- playerInput(board, boardNo): Handles player input and validation. Returns None

- checkWin(board): Checks if a player won a mini board. Returns boolean True or False

- updateBoardAfterWin(board, turn): Marks a mini board as won. Returns None

- checkDraw(board): Detects if all mini boards are full (draw). Returns boolean True or False

- checkWinWin(arr): Checks if a player has won the overall game by winning 3 mini boards in a row. Returns boolean True or False

- main(): Runs the game loop, handles turns, input, win logic, and display.

### 🧪 Testing
This project includes a comprehensive test suite in the file test_super_tic_tac_toe.py that verifies the correctness of all major functions in the game logic.

There are 4 tests that are written using Python’s built-in unittest framework and cover:

1) Valid and invalid move detection (checkValidMove)

2) Win detection for rows, columns, and diagonals (checkWin)

3) Diagonal and row victories across mini boards (checkWinWin)

4) Detection of full/drawn boards (checkDraw)

#### ▶️ To Run Tests:
Make sure you have Python installed, then from the terminal, run:
```bash
pytest test_project.py
```
If everything is implemented correctly, you will see output like:
```bash
....
------------------- 4 test passed in X.XXs -------------------
```

Each dot (.) represents a successful test.

## Design Choices

I wanted to make it more fancy by adding bigger O and X when you won a mini board.
Something like this -
```bash
  ---  |  \   /
 /   \ |   \ /
 |   | |    \
 \   / |   / \
  ---  |  /   \
```
but I scrapped this idea because first of all it's difficult and lot of things would need to be hard coded for that to work. And it's not that good looking anyways.

 So I opted for a simple method of changing all the symbols in a mini board to the one who has won that board. Its simple and gets the message across.
## Authors

- [@ParthKGarg](https://www.github.com/ParthKGarg)

