from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    msg = "Olá mundo!"
    return render_template('home.html', msg = msg)

if __name__== '__main__':
    app.run(debug=True)