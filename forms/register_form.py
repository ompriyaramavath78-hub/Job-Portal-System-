from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models.user import User

class RegisterForm(FlaskForm):
    full_name        = StringField('Full Name',        validators=[DataRequired(), Length(2, 150)])
    email            = StringField('Email',            validators=[DataRequired(), Email(), Length(max=150)])
    phone            = StringField('Phone',            validators=[Length(max=20)])
    role             = SelectField('Register As',      choices=[('candidate','Job Seeker'),('recruiter','Recruiter')])
    password         = PasswordField('Password',       validators=[DataRequired(), Length(6, 50)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit           = SubmitField('Create Account')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower().strip()).first():
            raise ValidationError('Email already registered.')
