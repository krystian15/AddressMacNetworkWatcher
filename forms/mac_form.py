from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email"})
    submit = SubmitField('Send')
