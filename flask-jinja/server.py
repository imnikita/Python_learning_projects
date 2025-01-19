from flask import Flask, render_template
from _datetime import datetime
from api_manager import APIManager

app = Flask(__name__)
manager = APIManager()

@app.route("/")
def start():
    some_int = 15
    now = str(datetime.now().year)
    return render_template("index.html", current_year=now, num=some_int, name=None)

@app.route("/<name>")
def basic_info(name):
    data = manager.rquest_info_by_name(name)
    print(data[0], data)
    return render_template("info.html", name=name, gender=data[0], age=data[1])

@app.route("/blog")
def go_blog():
    blogs = manager.request_blogs()
    return render_template("blog.html", blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)