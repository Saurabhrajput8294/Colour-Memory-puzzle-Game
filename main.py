
## memory game
import tkinter as tk
import random
# Constants
GRID_SIZE = 4  # 4x4 grid (16 cards)
CARD_WIDTH = 8
CARD_HEIGHT = 4
COLORS = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "pink"] * 2  # 8 pairs
random.shuffle(COLORS)  # Shuffle the cards
class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        self.first_card = None  # Store the first selected card
        self.buttons = {}  # Store button widgets for easy reference

        # Create the grid of buttons
        self.create_grid()

    def create_grid(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                # Create a button for each card, initially blank
                button = tk.Button(
                    self.root,
                    text="",
                    width=CARD_WIDTH,
                    height=CARD_HEIGHT,
                    command=lambda r=row, c=col: self.on_card_click(r, c),
                    bg="lightgrey",
                )
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def on_card_click(self, row, col):
        button = self.buttons[(row, col)]
    # Ignore clicks on already revealed cards
        if button["text"] != "":
            return
        # Show the card's color
        color = COLORS[row * GRID_SIZE + col]
        button.config(text=color, bg=color)

        if self.first_card is None:
            # Store the first card clicked
            self.first_card = (row, col)
        else:
            # Check if the second card matches the first
            first_row, first_col = self.first_card
            first_button = self.buttons[(first_row, first_col)]
            second_button = button

            if COLORS[first_row * GRID_SIZE + first_col] == COLORS[row * GRID_SIZE + col]:
                # Match found, keep both cards revealed
                self.first_card = None
            else:
                # No match, hide both cards after a short delay
                self.root.after(500, lambda: self.hide_cards(first_button, second_button))
                self.first_card = None
    def hide_cards(self, first_button, second_button):
        first_button.config(text="", bg="lightgrey")
        second_button.config(text="", bg="lightgrey")
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
