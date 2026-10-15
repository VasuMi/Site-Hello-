from flask import Flask, render_template, request, flash

app= Flask(__name__)
app.secret_key = "sdgyujkdhj"

app.debug = True

@app.route('/hello')
def index():
    flash("what's you name????")
    return render_template('index.html')

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("hi "+ str(request.form['name_input']) + ", great to see you....welcome to my website")
    return render_template('index.html')

