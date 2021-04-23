"""Sign-up & log-in forms."""
import arrow
from flask_wtf import FlaskForm
from wtforms import SelectField, PasswordField, StringField, SubmitField, DecimalField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, IPAddress
from .models import BoatType, db
# from wtforms.ext.sqlalchemy.fields import QuerySelectField

"""
def boat_type_choices():
    output_list = []
    result = db.session.query(BoatType).all()
    for row in result:
        output_list.append((row.id, row.name))
    return output_list
"""

def get_now_time_plus_10():
    output = arrow.now().int_timestamp + 10
    return output


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    website = StringField(
        'Website',
        validators=[Optional()]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class NewRaceForm(FlaskForm):
    """Information required to start a new race"""
    name = StringField('name', validators=[DataRequired(), ])
    longitude = StringField('longitude', validators=[DataRequired(), ])
    latitude = StringField('latitude', validators=[DataRequired(), ])
    sw_corner = DecimalField('sw_corner', validators=[DataRequired(), ])
    ne_corner = DecimalField('ne_corner', validators=[DataRequired(), ])
    # boat_type = SelectField('boat_type', choices=boat_type_choices(), validators=[DataRequired(), ])
    boat_type = IntegerField('boat_type', validators=[DataRequired(), ])
    start_time = IntegerField('start_time', default=get_now_time_plus_10(), validators=[DataRequired(), ])
    private = BooleanField('private', validators=[DataRequired(), ])
    submit = SubmitField('Submit')

class NewBoatForm(FlaskForm):
    """Information required to start a new race"""
    name = StringField('name', validators=[DataRequired(), ])


class TestForm(FlaskForm):
    """This is a test form"""
    name = StringField('name',validators=[DataRequired(), ])
    email = StringField('Email', validators=[DataRequired(),  Email(message='Enter a valid email.')])
    submit = SubmitField('Log In')
