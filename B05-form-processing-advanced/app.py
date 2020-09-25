from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html', page_title="Home")

@app.route('/form')
def form():
    return render_template('form.template.html', page_title='Form')


@app.route('/form', methods = ['POST'])
def process_form():

    return "form received"

    print(request.form)

    name = request.form("")

    return "ok"



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
