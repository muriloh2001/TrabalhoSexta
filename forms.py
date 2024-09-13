from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address already in use.')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100, message="Title must be between 2 and 100 characters.")])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=5, max=500, message="Description must be between 5 and 500 characters.")])
    status = SelectField('Status', choices=[('pendente', 'Pendente'), ('em andamento', 'Em Andamento'), ('concluída', 'Concluída')], validators=[DataRequired()])
    users = SelectMultipleField('Users', coerce=int, validators=[DataRequired(message="Please select at least one user.")])  # Múltiplos usuários
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.users.choices = [(user.id, user.username) for user in User.query.all()]

    def validate_users(self, users):
        if not users.data:
            raise ValidationError('You must assign at least one user to the task.')
