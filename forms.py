from flask_wtf import Form
from models import User
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
								Length, EqualTo)

def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError('User of that name already exists')

def email_exists(form, field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('User with that email address already exists')

class RegisterForm(Form):
	username = StringField(
		'Username', 
		validators=[
			DataRequired(), 
			Regexp(r'^[a-zA-Z0-9_]+$',
			message=("Username should be one world, letters, numbers only")
			),
			name_exists
		])
	email = StringField('Email', 
		validators=[
			DataRequired(), 
			Email(), 
			email_exists
		])
	password = PasswordField('Password',
		validators=[
			DataRequired(),
			Length(min=5),
			EqualTo('password2', message='Passwords must match')
		])
	password2 = PasswordField('Confirm Password',
		validators=[
			DataRequired()
		])


class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])

class PostForm(Form):
	content = TextAreaField("What is going on?", validators=[DataRequired()])
