from flask import FlaskForm
from wtforms import IntegerField, SubmitField, DateField

class HealthDataForm(FlaskForm):
   date = DateField('Date', format='%Y-%m-%d')
   exercise = IntegerField('Exercises (minutes)')
   meditation = IntegerField('Meditation (minutes)')
   sleep = IntegerField('Sleep (hours)')
   submit = SubmitField('Submit')
   
   