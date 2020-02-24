from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MacForm(FlaskForm):
    fullname = StringField('Name and surname', validators=[DataRequired()])
    submit = SubmitField('Send')