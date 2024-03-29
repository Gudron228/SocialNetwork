from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Users

class AddPostForm(FlaskForm):
    name = StringField('Название статьи:', validators=[DataRequired()])
    post = TextAreaField('Текст статьи:', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    email = EmailField('Логин:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Запомни меня')
    submit = SubmitField('Авторизоваться')


class RegisterForm(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, email):
        user = Users.query.where(Users.email == email).first()
        if user is not None:
            raise ValidationError('Пожалуйста используйте несуществующий email.')