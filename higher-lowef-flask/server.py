from random import randint

from flask import Flask

app = Flask(__name__)

chosen_number = randint(0,11)

@app.route("/")
def welcome():
    image_url = "https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif"
    text = "Guess a number between 0 and 9"
    return f"""
    <html>
        <body>
            <img src="{image_url}" width="200" height="200" alt="Welcome GIF">
            <h1 style="color: blue;">{text}</h1>
        </body>
    </html>
    """

@app.route("/<int:number>")
def make_guess(number):
    if number > chosen_number:
        color = "red"
        image_url = "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"
        message = "Too high!"
    elif number < chosen_number:
        color = "orange"
        image_url = "https://media.giphy.com/media/3o7TKLHFr4mjzG2Yh2/giphy.gif"
        message = "Too low!"
    else:
        color = "green"
        image_url = "https://media.giphy.com/media/3o7TKU8RvQuomFfUUU/giphy.gif"
        message = "You got it right!!!"

    return f"""
    <html>
        <body>
            <img src="{image_url}" width="200" height="200" alt="Guess Result GIF">
            <h1 style="color: {color};">{message}</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)