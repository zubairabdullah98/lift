# © 2025 Zubair Abdullah Sadiq. All rights reserved.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserRegistrationForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    full_name = StringField('Full Name', validators=[DataRequired()])
    skill = StringField('Skill', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Register')
