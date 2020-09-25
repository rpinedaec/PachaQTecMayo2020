from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remind me')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat password please', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('[REPEATED USERNAME] Choose another please')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('[REPEATED EMAIL] Choose another please')

class AddProductoForm(FlaskForm):
    nombre = StringField('Product name', validators=[DataRequired()])
    stock = IntegerField('Inicial Stock', validators=[DataRequired()])
    precio = DecimalField('Inicial Price',places=2, validators=[DataRequired()])
    categoria_id =IntegerField('Category', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteProductoForm(FlaskForm):
    nombre = StringField('Product name', validators=[DataRequired()])
    stock = IntegerField('Inicial Stock', validators=[DataRequired()])
    precio = DecimalField('Inicial Price',places=2, validators=[DataRequired()])
    categoria_id =IntegerField('Category', validators=[DataRequired()])
    submit = SubmitField('Delete')

class addFacturaForm(FlaskForm):
    date = IntegerField('Date', validators=[DataRequired()])
    products = StringField('Products', validators=[DataRequired()])
    total = DecimalField('Total',places=2, validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteFacturaForm(FlaskForm):
    date = IntegerField('Date', validators=[DataRequired()])
    products = StringField('Products', validators=[DataRequired()])
    total = DecimalField('Total',places=2, validators=[DataRequired()])
    submit = SubmitField('Delete')

class addCategoriaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteCategoriaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Delete')