import random
import tkinter as tk
import numpy as np
import pandas as pd

# Game Configuration
WIDTH = 20  # Grid columns
HEIGHT = 20  # Grid rows
CELL_SIZE = 25  # Size of each cell in pixels
SPEED_MS = 120  # Game speed in milliseconds (lower = faster)


class SnakeGameTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("NumPy & Pandas Snake Game")
        self.root.resizable(False, False)

        # Status Label for Score
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14, "bold"), bg="#18181c", fg="#f0f0f0")
        self.score_label.pack(fill=tk.X)

        # Canvas for Game Board
        self.canvas = tk.Canvas(root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="#18181c",
                                highlightthickness=0)
        self.canvas.pack()

        # Key bindings
        self.root.bind("<KeyPress>", self.handle_keypress)

        self.reset_game()
        self.update_game()

    def reset_game(self):
        # NumPy grid initialization
        self.grid = np.zeros((HEIGHT, WIDTH), dtype=int)

        # Pandas DataFrame initialization for snake tracking
        initial_y, initial_x = HEIGHT // 2, WIDTH // 2
        self.snake_df = pd.DataFrame([
            {'y': initial_y, 'x': initial_x},
            {'y': initial_y, 'x': initial_x - 1},
            {'y': initial_y, 'x': initial_x - 2}
        ])

        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        self.spawn_food()

    def spawn_food(self):
        while True:
            fy = random.randint(0, HEIGHT - 1)
            fx = random.randint(0, WIDTH - 1)
            if not ((self.snake_df['y'] == fy) & (self.snake_df['x'] == fx)).any():
                self.food = {'y': fy, 'x': fx}
                break

    def handle_keypress(self, event):
        key = event.keysym.lower()
        if key == 'up' and self.direction != 'DOWN':
            self.next_direction = 'UP'
        elif key == 'down' and self.direction != 'UP':
            self.next_direction = 'DOWN'
        elif key == 'left' and self.direction != 'RIGHT':
            self.next_direction = 'LEFT'
        elif key == 'right' and self.direction != 'LEFT':
            self.next_direction = 'RIGHT'
        elif key == 'r' and self.game_over:
            self.reset_game()

    def update_game(self):
        if not self.game_over:
            self.direction = self.next_direction
            head = self.snake_df.iloc[0].copy()

            # Move head coordinates
            if self.direction == 'UP':
                head['y'] -= 1
            elif self.direction == 'DOWN':
                head['y'] += 1
            elif self.direction == 'LEFT':
                head['x'] -= 1
            elif self.direction == 'RIGHT':
                head['x'] += 1

            # Check wall collision
            if not (0 <= head['y'] < HEIGHT and 0 <= head['x'] < WIDTH):
                self.game_over = True

            # Check self collision (ignoring tail)
            body_without_tail = self.snake_df.iloc[:-1]
            if not self.game_over and (
                    (body_without_tail['y'] == head['y']) & (body_without_tail['x'] == head['x'])).any():
                self.game_over = True

            if not self.game_over:
                # Check food collision
                ate_food = (head['y'] == self.food['y'] and head['x'] == self.food['x'])

                # Prepend new head in Pandas DataFrame
                new_row = pd.DataFrame([head])
                self.snake_df = pd.concat([new_row, self.snake_df], ignore_index=True)

                if ate_food:
                    self.score += 10
                    self.spawn_food()
                else:
                    self.snake_df = self.snake_df.iloc[:-1].reset_index(drop=True)

        self.render()
        self.root.after(SPEED_MS, self.update_game)

    def render(self):
        self.canvas.delete("all")

        # Draw Food
        fx, fy = self.food['x'] * CELL_SIZE, self.food['y'] * CELL_SIZE
        self.canvas.create_oval(fx + 3, fy + 3, fx + CELL_SIZE - 3, fy + CELL_SIZE - 3, fill="#e74c3c", outline="")

        # Draw Snake
        for i, row in self.snake_df.iterrows():
            sx, sy = int(row['x']) * CELL_SIZE, int(row['y']) * CELL_SIZE
            color = "#27ae60" if i == 0 else "#2ecc71"  # Darker green for head
            self.canvas.create_rectangle(sx + 2, sy + 2, sx + CELL_SIZE - 2, sy + CELL_SIZE - 2, fill=color, outline="")

        # Update Score Display
        if self.game_over:
            self.score_label.config(text=f"GAME OVER! Score: {self.score} (Press 'R' to Restart)")
        else:
            self.score_label.config(text=f"Score: {self.score}")x`


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#18181c")
    game = SnakeGameTkinter(root)
    root.mainloop()