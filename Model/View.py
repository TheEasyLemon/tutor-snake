import tkinter as tk
import time


class View(tk.Tk):
    def __init__(self, model):
        super().__init__()

        self.bind("<Key>", self.handle_keypress)

        self.model = model

        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack()

        self.cells = []

        self.gridsize = 600 / self.model.board_size

        for i in range(self.model.board_size):
            cell_row = []
            for j in range(self.model.board_size):
                topleft_x = self.gridsize * j
                topleft_y = self.gridsize * i
                bottomright_x = self.gridsize + topleft_x
                bottomright_y = self.gridsize + topleft_y

                cell = self.canvas.create_rectangle(topleft_x,
                                                    topleft_y,
                                                    bottomright_x,
                                                    bottomright_y,
                                                    outline="#fff",
                                                    fill="#000")

                cell_row.append(cell)
            self.cells.append(cell_row)

        self.after(1000, self.animation)

    def animation(self):
        while True:
            for i in range(self.model.board_size):
                for j in range(self.model.board_size):
                    if (i, j) in self.model.snake:
                        self.canvas.itemconfig(self.cells[i][j], fill="#fff")
                    elif (i, j) == self.model.apple:
                        self.canvas.itemconfig(self.cells[i][j], fill="#f00")
                    else:
                        self.canvas.itemconfig(self.cells[i][j], fill="#000")

            self.update()
            self.model.advance()

            if self.model.game_over:
                self.destroy()

            time.sleep(0.1)

    def handle_keypress(self, event):
        if event.char == 'q':
            self.destroy()
        elif event.char == 'w':
            self.model.snake_direction = "up"
        elif event.char == "a":
            self.model.snake_direction = "left"
        elif event.char == "s":
            self.model.snake_direction = "down"
        elif event.char == "d":
            self.model.snake_direction = "right"
