from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class MaxesForm(FlaskForm):
    msq = IntegerField('Max Squat',
                        validators=[DataRequired(), Length(min=2, max=4)])
    mbe = IntegerField('Max Press',
                        validators=[DataRequired(), Length(min=2, max=4)])
    mdl = IntegerField('Max Deadlift',
                        validators=[DataRequired(), Length(min=2, max=4)])
    mainliftchoice = RadioField('Volume',
                                choices=[('high', 'High'),('low', 'Low')],
                                validators=[DataRequired()]
                                )
    submit = SubmitField('Submit')