from turtle import Turtle

FONT = ("Courier", 20, "normal")
COLOR = "White"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.player_score = 0
        self.goto(-40,350)
        self.write_score()

    def write_score(self):
        """The player's current score is displayed at the top of the game screen"""
        self.clear()
        self.write(arg=f"Score: {self.player_score}", font=FONT)

    def increase_score(self):
        """The player's current score is increased by 1."""
        self.player_score += 1
        self.write_score()

    def game_over(self):
        """If the snake collides with the wall or the snake body, then the game over sequence is triggered. The words GAME OVER are displayed on the game screen."""
        self.goto(-120, 0)
        self.write(arg="GAME OVER", font=("Courier", 40, "bold"))
