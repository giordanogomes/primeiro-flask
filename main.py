from flask import Flask, render_template

app = Flask(__name__)


# criar a 1ª página do site
@app.route("/")
def homepage():
    return render_template("homepage.html")


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
