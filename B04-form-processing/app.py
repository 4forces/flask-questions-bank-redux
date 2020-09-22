from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html')

@app.route('/num-game')
def number_game():
    return render_template('input.template.html')

@app.route('/num-game', methods=['POST'])
def process_number():
    num = int(request.form.get('number'))
    return render_template('process_num.template.html', num=num)


# @app.route('/about')
# def about():
#     return render_template('about.template.html')

@app.route('/contact-us', methods=['GET'])
def contact():
    return render_template('form.template.html')


@app.route('/contact-us', methods=['POST'])
def process_contact():

    print(request.form)

    name = request.form.get('name')
    sex = request.form.get('sex')
    comment = request.form.get('comment')
    can_contact = request.form.get('can-contact')
    termscons = request.form.get('democheckbox')

    contactable = ""

    if can_contact == "1":
        contactable = True
    else:
        contactable = False

    if termscons == None:
        return render_template("form.template.html",
                               message="Please accept the checkbox")

    return render_template('form-return.template.html', 
                           name=name, 
                           sex=sex,
                           comment=comment,
                           contactable=contactable,
                           termscons=termscons)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
