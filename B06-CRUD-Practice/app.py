from flask import Flask, render_template, request, redirect, url_for

import json
import os
import random

app = Flask(__name__)

database = []
with open('data.json', 'r') as fp:
    database = json.load(fp)

@app.route("/")
def home():
    return render_template('home.template.html')

@app.route("/ufo-sightings")
def show_sightings():
    return render_template('sightings.template.html', database=database)

@app.route('/sightings/create')
def create_sightings():
    return render_template('form.template.html')

@app.route('/sightings/create', methods=["POST"])
def process_create_sightings():
    print(request.form)
    new_sighting = {
        "id": random.randint(100000,999999),
        "title": request.form.get("title"),
        "date": request.form.get("date"),
        "time": request.form.get("time"),
        "email": request.form.get("email"),
        "duration": request.form.get("duration"),
        "lat": request.form.get("lat"),
        "lon": request.form.get("lon"),
        "desc": request.form.get("desc")
        }
    database.append(new_sighting)

    with open('data.json', 'w') as fp:
        json.dump(database, fp)

    # return "form received"

    return redirect(url_for('show_sightings'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
