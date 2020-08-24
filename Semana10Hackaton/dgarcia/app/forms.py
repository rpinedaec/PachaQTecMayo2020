from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TimeField
from wtforms import IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Categoria, Producto, Cliente, TipoDocumento
from app import db


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contreseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField(
        'Repita contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuario regstrado usa otro nombre')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-mail registrado usa otro email')

class AddProductoForm(FlaskForm):
    nombre = StringField('Nombre de Producto', validators=[DataRequired()])
    stock = IntegerField('Stock Inicial', validators=[DataRequired()])
    precio = DecimalField('Precio Inicial',places=2, validators=[DataRequired()])
    categoria_id =IntegerField('Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddCategoriaForm(FlaskForm):
    nombre = StringField('Nombre de Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddTipoDocumentoForm(FlaskForm):
    descripcion = StringField('Tipo de Documento', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    documento =IntegerField('TipoDocumento', validators=[DataRequired()])
    numero_documento = StringField('Numero Documento', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddFacturaForm(FlaskForm):
    fecha = TimeField(label='Time', validators=None)
    cliente_id =IntegerField('Cliente', validators=[DataRequired()])
    submit = SubmitField('Siguiente')

class AddDetalleFacturaForm(FlaskForm):
    producto_id =IntegerField('Producto', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    enviar = SubmitField('Guardar')

class DetalleForm(FlaskForm):
    visualizar = SubmitField('Ver Facturas')