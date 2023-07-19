from flask import Flask
import random

app = Flask(__name__)
print(__name__)

number = random.randint(0, 9)
print(number)


@app.route('/')
def home():
    return "<title>HIGHR-LOWER-GAME</title>" \
           "<h1><b>GUESS THE NUMBER BETWEEN 0 TO 9</b></h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route('/<int:guess>')
def checking(guess):
    if guess < number:
        return "<h3 style'color: red'>Too low, try again!</h3>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess > number:
        return "<h3 style'color: red'>Too high, try again!</h3>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h3 style'color: green'>You Found it</h3>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run()
