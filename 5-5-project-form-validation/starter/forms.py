from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, DateField
from wtforms.validators import  NumberRange,InputRequired, DataRequired

class HealthDataForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    exercise = IntegerField('Exercise (minutes)', validators=[InputRequired(), NumberRange(min=0, message="Please enter a non-negative value.")])
    meditation = IntegerField('Meditation (minutes)', validators=[InputRequired(), NumberRange(min=0, message="Please enter a non-negative value.")])
    sleep = IntegerField('Sleep (hours)',validators=[InputRequired(), NumberRange(min=0, max=24, message="Please enter a value between 0 and 24.")])
    submit = SubmitField('Submit')
