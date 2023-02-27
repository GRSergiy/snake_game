from turtle import Turtle

file = open("data.txt")
data = file.read()
file.close()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = int(data)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
    #save high score for the future games in the data.txt file

        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt",mode = "w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.score_board()


    def increase_score(self):
    #add a point to the score

        self.score += 1
        self.score_board()










