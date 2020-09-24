from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html')

@app.route('/')
def number_game():
    return render_template('input.template.html')

@app.route('/num-game', methods=['POST'])
def process_number():
    num = int(request.form.get('number'))
    return render_template('process_num.template.html', num=num)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
