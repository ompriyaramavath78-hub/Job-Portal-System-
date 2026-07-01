from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class JobForm(FlaskForm):
    title               = StringField('Job Title',        validators=[DataRequired(), Length(3, 200)])
    description         = TextAreaField('Job Description',validators=[DataRequired(), Length(min=20)])
    skills_required     = StringField('Skills Required',  validators=[Optional(), Length(max=500)])
    location            = StringField('Location',         validators=[Optional(), Length(max=150)])
    job_type            = SelectField('Job Type', choices=[
                            ('Full-Time','Full-Time'),('Part-Time','Part-Time'),
                            ('Contract','Contract'),('Internship','Internship'),('Remote','Remote')])
    experience_required = SelectField('Experience', choices=[
                            ('Fresher','Fresher'),('0-1 Years','0-1 Years'),
                            ('1-2 Years','1-2 Years'),('2-3 Years','2-3 Years'),
                            ('3-5 Years','3-5 Years'),('5-7 Years','5-7 Years'),
                            ('7-10 Years','7-10 Years'),('10+ Years','10+ Years')])
    salary_min          = IntegerField('Min Salary (LPA)', validators=[Optional(), NumberRange(0, 9999)])
    salary_max          = IntegerField('Max Salary (LPA)', validators=[Optional(), NumberRange(0, 9999)])
    vacancies           = IntegerField('Vacancies',        validators=[Optional(), NumberRange(1, 999)], default=1)
    submit              = SubmitField('Save Job')

class CompanyForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), Length(2, 200)])
    industry     = StringField('Industry',     validators=[Optional(), Length(max=100)])
    website      = StringField('Website',      validators=[Optional(), Length(max=255)])
    description  = TextAreaField('Description',validators=[Optional()])
    location     = StringField('Location',     validators=[Optional(), Length(max=150)])
    company_size = SelectField('Company Size', choices=[
                    ('','Select'),('1-10','1-10'),('11-50','11-50'),('51-200','51-200'),
                    ('201-500','201-500'),('501-1000','501-1000'),('1000+','1000+')])
    founded_year = IntegerField('Founded Year', validators=[Optional(), NumberRange(1800, 2030)])
    submit       = SubmitField('Save Profile')
