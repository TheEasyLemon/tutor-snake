import random


class Model:
    def __init__(self, board_size):
        self.board_size = board_size

        self.snake = self.make_snake()

        self.snake_length = 1
        self.snake_direction = "left"

        self.game_over = False
        self.apple = self.make_apple()

    def make_snake(self):
        """
        Create snake in the center of the board
        :return:
        """
        row = self.board_size // 2
        col = self.board_size // 2

        return [(row, col)]

    def make_apple(self):
        """
        Create apple any where on the board except on the snake
        :return:
        """
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)

        while (row, col) in self.snake:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)

        return row, col

    def wall_collision(self):
        """
        Sets the game to be over if the snake collides with the wall
        :return:
        """
        i, j = self.snake[0]

        # Compare x-coordinate
        if i >= self.board_size or i < 0:
            self.game_over = True

        # Compare y-coordinate
        if j >= self.board_size or j < 0:
            self.game_over = True

    def snake_collision(self):
        """
        Sets the game to be over if it collides with itself
        :return:
        """
        head = self.snake[0]
        body = self.snake[1:]
        if head in body:
            self.game_over = True

    def advance(self):
        """
        move the model forward 1 time step
        :return:
        """
        # dictionary
        directions = {"left": (0, -1),
                      "right": (0, 1),
                      "up": (-1, 0),
                      "down": (1, 0)}
        # get direction
        row_change, col_change = directions[self.snake_direction]
        current_row, current_col = self.snake[0]

        # Update the head of the snake
        self.snake.insert(0, (current_row + row_change, current_col + col_change))

        # Check collision
        self.wall_collision()

        # Check eating apple
        if self.snake[0] == self.apple:
            self.apple = self.make_apple()
            return

        # Pop off the end of the snake
        self.snake.pop()

        # Collision detection with itself
        self.snake_collision()

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.snake])
