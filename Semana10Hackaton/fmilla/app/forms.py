from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, DecimalField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contreseña', validators=[DataRequired()])
    remember_me = BooleanField('recuerdame')
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repita el Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuario regstrado usa otro nombre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Mail registrado usa otro email.')

class AddProductoForm(FlaskForm):
    nombre = StringField('Nombre de Producto', validators=[DataRequired()])
    stock = IntegerField('Stock Inicial', validators=[DataRequired()])
    precio = DecimalField('Precio Inicial',places=2, validators=[DataRequired()])
    categoria_id =IntegerField('Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class DeleteProductoForm(FlaskForm):
    nombre = StringField('Nombre de Producto', validators=[DataRequired()])
    submit = SubmitField('Eliminar')

class UpdateProductoForm(FlaskForm):
    nombre = StringField('Nombre de Producto', validators=[DataRequired()])
    nuevoNombre = StringField('Nuevo Producto', validators=[DataRequired()])
    nuevoStock = IntegerField('Nuevo Stock', validators=[DataRequired()])
    nuevoPrecio = DecimalField('Nuevo Precio',places=2, validators=[DataRequired()])
    nuevaCategoria_id =IntegerField('Categoria', validators=[DataRequired()])
    submit = SubmitField('Actualizar')

class AddCategoriaForm(FlaskForm):
    nombre = StringField('Nombre de Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class DeleteCategoriaForm(FlaskForm):
    nombre = StringField('Nombre de Categoria', validators=[DataRequired()])
    submit = SubmitField('Eliminar')

class UpdateCategoriaForm(FlaskForm):
    nombre = StringField('Nombre de Categoria', validators=[DataRequired()])
    nuevoNombre = StringField('Nueva Categoria', validators=[DataRequired()])
    submit = SubmitField('Actualizar')

class AddFacturaForm(FlaskForm):
    fecha = DateField('Fecha de emision', validators=[DataRequired()])
    tipoPago = StringField('Tipo de pago', validators=[DataRequired()])
    submit = SubmitField('Realizar Factura')

class AddPedidoForm(FlaskForm):
    producto_id = IntegerField('Producto', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Agregar Producto')
    submit1 = SubmitField('Finalizar')
