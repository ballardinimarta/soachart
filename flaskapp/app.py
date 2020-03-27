from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import Form
from wtforms.fields import DateTimeField, SubmitField
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQL_ALCHEMY_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
Bootstrap(app)
app.secret_key = 'SHH!'

class times(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime)
    stoptime = db.Column(db.DateTime)

class dateform(Form):
    start = DateTimeField(id = 'startpick', format='%m/%d/%Y %H:%M %p')
    stop =DateTimeField(id = 'stoppick', format='%m/%d/%Y %H:%M %p')
    submit = SubmitField('Submit')
    default = SubmitField('Default')

@app.route("/", methods=['POST', 'GET'])
def home():
    error = None
    form = dateform()
    if form.validate_on_submit():
        if form.start.data == form.stop.data:
            error ='starttime and stoptime cannot be the same time'
        elif form.start.data > form.stop.data:
            error ='the stoptime has to be later than the starttime'
        else:
            flash('Start Date is : {} End Date is : {}'.format(form.start.data, form.stop.data))
            #return redirect(url_for('soa'))
    return render_template('index.html', form=form, error=error)


@app.route("/soa")
def soa():
    return render_template('soa.html')

if __name__ == "__main__":
    app.run(debug=True)
