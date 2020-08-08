from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import IntegerField, DecimalField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Categoria, TipoDocumento, Producto, Cliente
from app import db


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
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
    nombreCategoria = [('0', 'Seleccione...')]
    for item in Categoria.query.all():
        nombreCategoria.append((item.id ,item.nombre))
    categoria = SelectField('Categoria', validators=[DataRequired()], choices=nombreCategoria)
    submit = SubmitField('Guardar')


class AddCategoriaForm(FlaskForm):
    nombre = StringField('Nombre de Categoria', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddTipoDocumentoForm(FlaskForm):
    descripcion = StringField('Tipo de Documento', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddClienteForm(FlaskForm):
    nombre = StringField('Nombre de Cliente', validators=[DataRequired()])
    apellido_pat = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_mat = StringField('Apellido Materno', validators=[DataRequired()])
    tipodocumento = [('0', 'Seleccione...')]
    for item in TipoDocumento.query.all():
        tipodocumento.append((item.id, item.descripcion))
    documento = SelectField('Tipo de Documento', validators=[DataRequired()], choices=tipodocumento)
    numero_documento = StringField('Numero Documento', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class AddFacturaForm(FlaskForm):
    nombrecliente = [('0', 'Seleccione...')]
    for item1 in db.session.query(Cliente).all():
        nombrecliente.append((item1.id, (item1.nombre + " " + item1.apellido_pat + " " + item1.apellido_mat)))
    cliente = SelectField('Cliente', validators=[DataRequired()], choices=nombrecliente)
    submit = SubmitField('Siguiente')

class AddDetalleFacturaForm(FlaskForm):
    nombreproducto = [('0', 'Seleccione...')]
    for item in Producto.query.all():
        nombreproducto.append((item.id, item.nombre))
    producto = SelectField('Producto', validators=[DataRequired()], choices=nombreproducto)
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    enviar = SubmitField('Guardar')

class DetalleForm(FlaskForm):
    visualizar = SubmitField('Ver Facturas')