from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0
        self.goto(x=0, y=270)
        self.write(arg=f"Score = {self.score}", align='center', font=('OCR-B 10 BT', 13, 'normal'))

    def refresh(self):
        """Score display"""
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}", align='center', font=('OCR-B 10 BT', 13, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over", align='center', font=('OCR-B 10 BT', 13, 'normal'))