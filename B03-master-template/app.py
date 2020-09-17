from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/about')
def about():
    return render_template('about.template.html')


@app.route('/our-vision')
def our_vision():
    return render_template('vision.template.html', title='byebye')

# trial error searching author (by database)


@app.route('/author/<first_name>/<last_name>')
def author(first_name, last_name):
    return render_template('authname.template.html',
                           fname=first_name, lname=last_name)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
